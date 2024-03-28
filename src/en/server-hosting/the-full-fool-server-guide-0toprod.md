# Going from nothing to full production (A server hosting guide)

So you seem to have decided to take the task of hosting your own fork server? Well this is the guide for you!

This guide will assume the following:
- You have basic knowledge of Git
- You have basic knowledge of Linux
- You have a basic knowledge of dotnet
- You got a ready Linux box ready to go (I will be using Rocky Linux, which is RHEL based distro)
- Some stuff will need a reverse proxy/web server. (I will be using Caddy and I'm providing examples in it. But nginx works too if you figure out the configs)
- Time

This guide will also have two parts. Requirements and recommended stuff.

```admonish info
Of course you don't have to do all this. But if your intend is to have a full on production server
with the intend that it will be public then having these ready should make sure you and your players have a good expirience.
```

## Required
This section includes tool that are required (or at least VERY recommended) to be setup. 

This may need to be setup before you even start your server or will at least require extensive server downtime.

### SS14.Watchdog
Watchdog is one of the most important tools for your server. It will ensure your server stays online and restart it for when it's time to update.

The guide for setting up is [here](/en/server-hosting/setting-up-ss14-watchdog.html)

```admonish note
I will strongly recommend you don't use git method in watchdog. And if you are planning to record replays you will REQUIRE manifest.

Git while easier to setup is
1. Quite unmaintained already and may break. Needing you to come in to fix it.
2. When your server does restart to update. Your servers downtime will be as long as it takes for your server to build. 
This depends on the cpu of your server. And will leave your players waiting for way longer for the server to start up... time of which they could decide to get into another server.
And thats assuming the update succeeds even and there were no build errors.
```

# Robust.Cdn
Robust.Cdn will store the built client (usually built by an action on github) to provide to your players. 

ESPECIALLY important if you are planning to host replays as clients will need to be able to download an older version of your fork to be able to load it.

# Manifest Update for your server
Manifest update will download a release of your server directly built from an action in github to use.

Like mentioned above. This is the solution to not using git method on watchdog. As the build would have already been made by the time your server updates. Thus restart will be faster

### PostgreSQL
PostgreSQL is the external database we use to store information (The other being SQLite)

Setup will be as simple as installing PostgreSQL and then setting up the right cvars as described [here](/en/general-development/setup/server-hosting-tutorial.md#postgresql-setup)

Installing PostgreSQL should be as simple as using your package manager. In RHEL based distros like Rocky it should be as simple as

```sudo dnf install postgresql```

Of course this is diffrent for every OS. So do your research.

```admonish note
While you can definitely run a server with SQLite. I would recommended against it for the following reasons
1. You will be unable to use tools like SS14.Admin or be able to share a database with two or more servers if you require to expand.
2. If you ever want to move to PostgreSQL from SQLite. It will require you to manually doctor the SQLite database before you even have a chance of importing it. (and there is no documantion we have for this) 
3. In case you need to modify something in the database. You will be able to just connect to the database instead of needing to take the sqlite file. Modify it and reupload it.
4. While not proven, some people claim that SQLite will has a performance hit.
```

### SS14.Admin
SS14.Admin is an online web panel that allows admins to perform administrative actions without logging into the server.

TECHNICLY this is not required. However your admins will be able to perform much better and faster with this as they don't have to login to investigate something.

The setup documentation for SS14.Admin is [here](/en/server-hosting/setting-up-ss14-admin.md)

### SS14.Changelog

SS14.Changelog is a tool that will receive webhooks from github. And once a pr is merged will take the changelog entries the commiter put and add them to the changelogs file to be displayed.

ALSO not required but recommended if you are wishing to be receiving pr's into your fork.

The setup documantion for SS14.Changelog is on the github [here](/en/server-hosting/setting-up-ss14-changelog.md)

## Recommended
This section includes tools that are recommended to setup. Most of these can be install even after you have started your server.

### Redbot (Discord bot)
Redbot will allow you to have your own personal discord bot. 

By install wizard-cogs as well you will be able to use our cogs. 

For example an easy way to reboot your in case something breaks. Or for your players to check how many people are online.

It will also make your server look a little more professional

The setup documentation for RedBot is [here](/en/server-hosting/setting-up-redbot.html)

### Reverse proxy the server api
This is pretty optional. But it takes seconds to setup. And gives you a little bit of trust.

First, get your favourite reverse proxy. I'm gonna use caddy as it will handle SSL with Let's Encrypt for me plus it's easier to configure (unlike nginx)

```caddyfile
example.com 
{
	reverse_proxy localhost:1212
}
```

After you will need to fix up some cvars on the server

```status.connectaddress``` should be a raw udp address to your server.

```hub.server_url``` should be your ``ss14s`` address. Make sure to start it off with ``ss14s`` and not ``ss14`` since you are now using SSL

Here is a config example. Assuming your server port is the default 1212. And that you have not set a subpath in your server url:
```toml
[status]
connectaddress = "udp://example.com:1212"

[hub]
server_url = "ss14s://example.com"
```

### Replays

Replays will allow you to replay a round again after it has ended. 

This is nice for your players as they will be able to replay a round and expirience something again.

And your admins will greatly enjoy this so that they can replay a round that they are investigating.

First setup the relevent cvar from the guide here [here](/en/server-hosting/server-replay-recording.md)

Ensure you configure ```replay.auto_record_temp_dir``` so that people can't download the replay while in the middle of a round.

It's also recommended that ```replay.auto_record_name``` includes your server name kind of like this ```servername-{year}_{month}_{day}-{hour}_{minute}-round_{round}.zip```

After you confirmed replays are being taken. Then all you will need to do is expose them to the internet to be downloaded! Once again i will be using Caddy.

```
example.com
{
	handle_path /replays* {
        root * /path/to/your/servers/replays
        file_server browse
    }
}
```

Now if you visit example.com/replays you should have a file browser!

(yeah im gonna be honest the "Served with Caddy" watermark is a little annoying... but you can replace the templete with the browse directive for ```file_server``` [Caddy docs for browse here](https://caddyserver.com/docs/caddyfile/directives/file_server))

# Grafana (and prometheus and loki)
Grafana (combined with prometheus and loki) will allow you to have a fancy stats panel where you can quickly view the performance of the server and logs at a quick glance.

# Map Server
The map server is a website intended for your players to be able to view the latest version of a station/map.

A demo is here [https://maps14.tanukij.dev/](https://maps14.tanukij.dev/)

Recommended especially if you have custom maps