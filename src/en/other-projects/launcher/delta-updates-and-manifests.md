# Delta Updates & Manifests

```admonish info
It's merged now 🎉
```

## Fundamentals

To connect to a server, we need to have all the content files the server specifies. These are all the textures, prototypes, code assemblies, and anything else that need to be loaded by the engine. 

The server provides us with the following info about the build it needs. This info is given via [`/info` on the HTTP status API](../../robust-toolbox/server-http-api.md). The info currently provided by servers is as follows.

* Fork ID & Version: Used purely as heuristics to determine which old versions to evict first from the launcher's content DB. Not used for anything security critical (always verified with cryptographic hashes of actual game content). Fork ID is basically the "codebase name" and fork version is the version identifier.
* Engine version: engine version to use when launching this and resolving engine modules.
* Zip information: Used for zip-based content downloads:
	* Zip download URL: URL to download a zip file from that contains the whole server content.
  * Zip SHA-256[^sha] hash: expected SHA-256 hash of the specified zip file.
* Manifest information: Used for manifest-based content downloads:
  * Manifest URL: URL to fetch the content manifest at.
  * Manifest BLAKE2b hash: hash of the manifest.
  * Manifest download URL: URL to request content downloads from.

There are two fundamental modes of operation for the launcher, when managing and downloading content: zip-based and manifest-based. Zip-based is the legacy model. It does not support any sort of delta updates and is there for backwards compatibility and simplicity. Manifest-based can support delta updates (i.e. only downloading changed files).

[^sha]: Yes, zip hashes are SHA-256, all the other hashes are 256-bit BLAKE2b. BLAKE2b is *much* faster to calculate and this does add up for real use cases, so is used for new stuff. Zips are SHA-256 for backwards compatibiltiy.

## Launcher ContentDB

Game content files tracked by the launcher are stored as blobs in an SQLite DB on WAL mode. File identity is compared purely by BLAKE2b hash of the contents, and ZSTD compression may optionally be applied if it saves space. These blobs are tracked in the `Content` table.

Each "version" of content that the launcher has downloaded and is currently keeping is stored in the `ContentVersion` table. The entire `ContentManifest` (= file list) is stored per version, holding the resource file path and which `Content` blob to use. These `ContentVersion`s also store the manifest hash (see below) always to identify their content. They may optionally store a zip SHA-256 hash for backwards compatibility with zip downloads. 

By indexing actual resource blobs by BLAKE2b hash and only storing paths per-manifest, we can deduplicate resource blobs both within a single version and between many different versions and even forks. Yay space savings!

We also track which robust version and modules (incl their exact version) are necessary for each version, in the `ContentEngineDependency` table. This is slightly awkward for the launcher because the actual content version (primarily identified by some sort of hash) is actually unrelated from the engine version to use: after all, the engine version is specified by the server via the status API. It is *not* contained in the content download (but the list of [modules](../../robust-toolbox/robust-modules.md) to use *is*, since it's stored in [the content manifest](../../robust-toolbox/content-manifests.md)). The solution here is that we make the launcher duplicate the version and manifest if the same content version is attempted to be used with a different engine version. We also have to re-resolve module versions when we do this. 

## Manifest downloads

Under manifest-based, the server reports a "content manifest" which contains hashes of all files in the content files, and their path. This manifest is then in turn hashed again and this hash is a final source of truth to identify a certain content pack.

This manifest is downloaded and compared when trying to connect to connect. If we do not have this manifest, we fetch the manifest from the server. We then find all blobs we do not have yet (by hash) and request them from the server via the manifest download URL it reports.

This manifest downloading uses a simple binary request/response format over HTTP POST[^httpquery] for performance reasons. As I am writing this SS14 has about 13k files in its resource pack (I want to cut RSIs down which would help but still). Doing something like individual HTTP requests for each individual file would be ridiculous, even with request pipelining or whatever madness you may have. The binary protocol is described below.

[^httpquery]: Ideally this would use something like [HTTP QUERY](https://www.ietf.org/id/draft-ietf-httpbis-safe-method-w-body-02.html) instead of POST, since it's just a GET-with-request-body. As I am writing this QUERY is not standardized yet however and probably completely unsupported everywhere.

### Manifest Format

The format of content manifest files is as follows:

```
Robust Content Manifest 1
<uppercase hex BLAKE2b 256-bit hash> <file path>
<uppercase hex BLAKE2b 256-bit hash> <file path>
<uppercase hex BLAKE2b 256-bit hash> <file path>
<uppercase hex BLAKE2b 256-bit hash> <file path>
...
```

Yeah it's just that easy. Single new lines please, no CRLF crap. The header at the top is just a version header. Trailing newline please. Sort entries by full file path ordinally.

Python code to generate this manifest from a zip file:

```py
import codecs
import hashlib
import io
import zipfile

def generate_manifest_hash(file: str) -> str:
    zip = zipfile.ZipFile(file)
    infos = zip.infolist()
    infos.sort(key=lambda i: i.filename)

    bytesIO = io.BytesIO()
    writer = codecs.getwriter("UTF-8")(bytesIO)
    writer.write("Robust Content Manifest 1\n")

    for info in infos:
        if info.filename[-1] == "/":
            continue

        bytes = zip.read(info)
        hash = hashlib.blake2b(bytes, digest_size=32).hexdigest().upper()
        writer.write(f"{hash} {info.filename}\n")

    manifestHash = hashlib.blake2b(bytesIO.getbuffer(), digest_size=32)

    return manifestHash.hexdigest().upper()
```

The BLAKE2b hash of this file is used as the single truth identifier to determine identity of a resource pack.

### Download Request Protocol Details

Alright yeah it's a little more complicated than a simple HTTP POST.

The client will HTTP GET the content manifest from the URL the server specifies. The server **should**[^rfclanguage] support content compression via HTTP `Accept-Encoding`/`Content-Encoding`: The launcher will accept `zstd`, `brotli`, `gzip` and `deflate`. ZSTD is recommended because it's actually modern technology. The manifest is just the text file construction above.

To do the actual content download, we first do a HTTP OPTIONS on the URL provided by the server. This OPTIONS **must** return a `X-Robust-Download-Min-Protocol` and `X-Robust-Download-Max-Protocol` response header that the launcher can use in the future for backwards and forwards compatibility. I am probably overengineering this.

The current "protocol version" is **1**.

After this HTTP OPTIONS, the launcher will send a POST request to the same URL. The request contains an `X-Robust-Download-Protocol` request header with the current protocol version to allow the server to understand it. In the request body is the full list of files to request, following the protocol down below. The `Content-Type` must be `application/octet-stream`. The client also again sends `Accept-Encoding` to allow for compression of the whole HTTP response body: the server **may** choose to follow this if it deems the tradeoff worth it.[^streamcompress]

The request body is simply a sequence of 32-bit LE 0-indexes into the content manifest, each specifying a blob in the manifest to download.[^manifestindices] Indices must not be requested twice in a single request.

The response body is more complicated and currently follows the following format:

```
<stream header>:
		int32 LE stream header flags field:
	  		bit 0 (pre-compress): if set, stream blobs are individually pre-compressed with ZSTD.
FOR every file in the request body: 
    <file header>:
        int32 LE blob size: Uncompressed size of the file blob
        IF pre-compress is set:
            int32 LE compressed size: Compressed size of the blob.
                                      If zero, the blob is not compressed and the uncompressed size should be used instead.
    <file contents>:
        N bytes for the file contents, see file header above for size
```


[^rfclanguage]: Look at me being fancy and using RFC-like language.
[^streamcompress]: Stream compression reduces bandwidth usage at the cost of increased server and launcher CPU load during transfer. Generally if the server does stream compression, it will not use individual-compressed blobs. Because of this, the blobs will also be stored less compactly in the launcher Content DB once the download is done.
[^manifestindices]: These are indexes into the manifest instead of direct raw blob hashes, because hashes would take far too much bandwidth too send.


#### Binary Format


## Zip-based downloads

Zip-based is partially intended to be lower complexity, and is the older update model. The server specifies a zip file and SHA256 hash for it. This hash is checked and compared, and the zip file downloaded if necessary. The local files are loaded from the zip file into the launcher's content DB.

A manifest hash is automatically generated and stored. This is to provide forwards-compatibility with manifest-based updating methods.

## Delta Update Techniques

In-file deltas (diffs): we could use zstd here with its file deltaing support. 

## Future Ideas

Right now manifests are quite large, even when compressed. A lot of this just comes down to the fact that 32-byte hashes by design are incompressible, and there are tons of files.

A more advanced system might make better use of Merkle Trees to reduce the amount of manifest that would need to be sent. This would make it so small updates to YAML files could be downloads in the single-digit kilobytes instead of 450+ KiB it would currently be, without needing an explicit version-to-version delta system.

Veloren provides their incremental updates by using HTTP range requests on stock CDNs. This is probably less efficient on raw bandwidth but the ability to use plain CDNs cannot be understated, since our system requires an active server. It's something to explore for the future if we need to scale up perf.