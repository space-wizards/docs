# Robust Generic Attribution

The **RGA** (Robust Generic Attribution) standard is intended to be a flexible, open, and readable way <!--Insert more marketing bull that sounds good here!--> to define various metadata such as licensing and attribution for an arbitrary collection of files of many types such as sound effects or prototypes. An RGA file contains metadata for all of the files in the same directory as the RGA file (not including subdirectories). The entries in an RGA file contain specific metadata such as the author of the file(s) or a description of any modifications made to them (in compliance with many Creative Commons licenses).

An RGA is a YAML file with the name `attributions.yml`, and contains an arbitrary number of entries as defined below.

Typically whenever new files are being added, a new entry will be added as it likely won't contain the same metadata as existing entries. However, one may append files to an existing entry if the metadata is otherwise identical.

## YAML

An RGA file must be named `attributions.yml`. All values within entries are wrapped in double-quotes (`""`).

The YAML contains an arbitrary number of entries, covering all files in the same directory as the RGA file. An entry is defined as follows:

Key | Meaning
--- | -------
`files` | An array of filenames (with extensions) that this entry applies to. The filename order is arbitrary. The `*` wildcard glob is supported (i.e. `*.ogg` denotes all OGG files in the directory).
`copyright` | The copyright holder and other relevant info. Any disclosure of modifications to comply with certain licenses should also go in this field.
`license` | A valid [SPDX License Identifier](https://spdx.org/licenses/) applying to all files within an entry. If a license does not have a valid SPDX identifier, `Custom` may be used but a link to the license should be provided in the `copyright` field.
`source` |  A valid URL pointing to a location where the file can be downloaded. If you are the creator of the work and don't have an alternate download location (e.g. bandcamp), provide the link to the pull request that added the file to the game. If this is a derivative work, this should be mentioned in the copyright field. If the file has only been lightly modified, just link to the original file. If the file has been heavily modified, link the modified version but provide links to any original files in the copyright field.

### Example YAML

```yaml
- files: ["thunderdome.ogg"]
  license: "CC-BY-NC-SA-3.0"
  copyright: "-Sector11 by MashedByMachines. Converted from MP3 to OGG."
  source: "https://www.newgrounds.com/audio/listen/312622"
- files: ["endless_space.ogg"]
  license: "CC-BY-3.0"
  copyright: "Endless Space by SolusLunes. Converted from MP3 to OGG."
  source: "https://www.newgrounds.com/audio/listen/67583"
```

## Design Goals

* Editing an RGA must be possible without proper tooling. This means no binary metadata.
* It must be easily diffable on GitHub.
* It must not bloat Git history too much when changes are made (prevent large file rewrites).
