# Публичные скрипты

Это дерьмо-скрипты, которые мы используем для размещения официальных сборок SS14. Сейчас понимаю, что наверное мне следовало опубликовать их раньше. Не могу сказать, что они работают на славу, я не говорю, что вы должны следовать моему примеру. Они приведены для ознакомления с тем, как работает наша спагетти-путаница, это не официальный поддерживаемый способ делать вещи. **Вы должны внимательно всё прочесть и понять, прежде чем использовать**.

`/home/robust-build-push/push.ps1`
```ps1
#!/usr/bin/env pwsh

$buildsBaseDir = "/home/wizards-build-push/builds_dir/"
$buildsJson = join-path $buildsBaseDir "manifest.json"
$buildsHtml = join-path $buildsBaseDir "builds.html"
$buildsDir = join-path $buildsBaseDir builds
$urlFmt = "https://cdn.centcomm.spacestation14.com/builds/wizards/builds/{0}/{1}"

$version = $args[0]

$versionBuildsDir = join-path $buildsDir $version

$clientFile = join-path $versionBuildsDir "SS14.Client.zip"

$build = @{
        "time" = (Get-Date -Format "o");
        "server" = @{};
        "client" = @{
                "url" = $urlFmt -f ($version, "SS14.Client.zip");
                "sha256" = Get-FileHash -Algorithm SHA256 $clientFile | Select-Object -ExpandProperty Hash
        }
}

get-childitem $versionBuildsDir | % {
        Write-Host $_
        $match = [regex]::Match($_.Name, "SS14.Server_(.+)\.zip");
        if (-not $match.Success) {
                return;
        }

        $rid = $match.Groups[1].Value
        $url = $urlFmt -f ($version, $_.Name)
        $sha256 = Get-FileHash -Algorithm SHA256 $_ | Select-Object -ExpandProperty Hash

        $build["server"][$rid] = @{
                "url" = $url;
                "sha256" = $sha256
        }
}

$build | convertto-json -depth 10 | Write-Host

$jsonDat = (get-content $buildsJson | convertfrom-json -AsHashtable) ?? @{"builds" = @{}}
$jsonDat["builds"][$version] = $build
$jsonDat | convertto-json -compress -depth 10 | set-content $buildsJson

./notify_update.sh
./update_last_build_page.py $buildsJson $buildsHtml
```

`/home/robust-build-push/notify_update.sh`
```bash
#!/bin/bash

# Robust.Cdn
curl -X POST -d "" -H 'Authorization: Bearer <token>' "http://localhost:27690/control/update"
# Game servers
curl -X POST -d "" -H "Authorization: Basic <token>" "https://lizard.spacestation14.io/watchdog/instances/wizards_den_lizard/update"
curl -X POST -d "" -H "Authorization: Basic <token>" "https://lizard.spacestation14.io/watchdog/instances/salamander/update"
curl -X POST -d "" -H "Authorization: Basic <token>" "https://mommi.spacestation14.io/watchdog/instances/wizards_den_eu_west/update"
curl -X POST -d "" -H "Authorization: Basic <token>" "https://miros.spacestation14.io/watchdog/instances/wizards_den_eu_west_2/update"
curl -X POST -d "" -H "Authorization: Basic <token>" "https://centipede.spacestation14.io/watchdog/instances/centipede/update"
```

`/home/robust-build-push/delete_old.ps1`
```ps1
#!/usr/bin/env pwsh

$buildsBaseDir = "/home/wizards-build-push/builds_dir"
$buildsJson = join-path $buildsBaseDir "manifest.json"
$buildsDir = join-path $buildsBaseDir builds

$jsonDat = (get-content $buildsJson | convertfrom-json -AsHashtable)
$interval = [System.TimeSpan]::FromDays(30)
$delBefore = [System.DateTimeOffset]::Now - $interval

$toDel = $jsonDat["builds"].GetEnumerator() | where {[DateTimeOffset]::Parse($_.Value["time"]) -lt $delBefore} | select -exp Key

$toDel | % { $jsonDat["builds"].Remove($_) }
$toDel | % { rm -r $(Join-Path $buildsDir $_) }

$jsonDat | convertto-json -compress -depth 10 | set-content $buildsJson
```

`/home/robust-build-push/update_last_build_page.py`
```python
#!/usr/bin/env python3
import json
import sys
from datetime import timezone
from dateutil.parser import parse
from html import escape

TEMPLATE = """
<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>SS14 Server Builds</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            p {
                margin-top: 0;
            }

            .commitHashInfo {
                font-size: 0.75rem;
            }

            .versionNumber {
                font-family: 'Courier New', Courier, monospace;
            }

            @media (prefers-color-scheme: dark) {
                body {
                    background-color: #25252A;
                    color: white;
                }

                a {
                    color: rgb(88, 166, 255);
                }
            }
        </style>
    </head>
    <body>
        <p>
            Here you can find the latest server build available for <a href="https://spacestation14.io/">Space Station 14</a>.
        </p>
        <p>
            The latest build is from <strong>$BUILDDATE</strong>. Pick whatever build suits the operating system you're trying to host on:
        </p>

        <ul>
            $BUILDS
        </ul>

        <p class="commitHashInfo">
            The version is <span class="versionNumber">$VERSION</span>
        </p>

        <p>
            If you somehow ended up here without reading the <a href="https://docs.spacestation14.io/en/getting-started/hosting">Server Hosting Tutorial</a>, go read that first. It tells you how to actually host a server.
        </p>
    </body>
</html>
"""

RIDMAP = {
    "linux-x64": "Linux x64",
    "linux-arm64": "Linux ARM64",
    "win-x64": "Windows x64",
    "osx-x64": "macOS x64"
}

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <manifest> <output>")
    exit(1)

manifestPath = sys.argv[1]
outputPath = sys.argv[2]

with open(manifestPath, "r") as f:
    manifest = json.load(f)

last_build = max(
    manifest["builds"].items(),
    key=lambda x: parse(x[1]["time"]))

print(f"Last build: {last_build[0]}: {last_build[1]['time']}")

buildVersion = last_build[0]
buildInfo = last_build[1]

buildDate = parse(buildInfo["time"])
buildDateUtc = buildDate.astimezone(timezone.utc)
buildDateFmt = f"{buildDateUtc:%A, %d %B %Y at %H:%M UTC}"

listHtml = ""

for (rid, info) in sorted(buildInfo["server"].items(), key=lambda x: RIDMAP.get(x[0], x[0])):
    url = info["url"]
    listHtml += f"<li><a href='{escape(url)}'>{RIDMAP.get(rid, rid)}</a></li>"

finalHtml = TEMPLATE \
    .replace("$BUILDS", listHtml) \
    .replace("$VERSION", buildVersion) \
    .replace("$BUILDDATE", buildDateFmt)

with open(outputPath, "w") as f:
    f.write(finalHtml)
```

## Ч.А.В.О.

### С какого хера кто-то будет использовать Powershell

Он лучше Bash'a.
