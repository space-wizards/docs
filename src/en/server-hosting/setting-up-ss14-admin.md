# Setting up SS14.Admin
[SS14.Admin](https://github.com/space-wizards/SS14.Admin/) is a web-based panel for administration of SS14 servers, providing various [features](../community/admin/admin-tooling.md#ss14admin) critical for serious servers.

This document will explain what you will need to set yourself up with your own instance of SS14.Admin.

## Overview

SS14.Admin connects directly to your game server's database, allowing it to view all data on players, bans, admins, etc. This is then accessible to game server administrators via their web browser. Admins log into SS14.Admin directly with their SS14 account, via [OAuth](../server-hosting/oauth.md).

## Prerequisites

- Your game server must be set up to use **PostgreSQL** as a database engine. It is not possible to use SS14.Admin with SQLite.
- A domain name to host SS14.Admin under.
- A reverse proxy server like Nginx or Caddy.

## Installation

We provide official container images of SS14.Admin via GitHub Container Registry. Otherwise, we also have instructions for manually building the project via the .NET SDK.

### Container image

The latest stable image of SS14.Admin is `ghcr.io/space-wizards/ss14.admin:1`. Information about the container:

* Listens on port 8080
* Default UID/GID is 1654
* Important volumes to mount:
  * `/app/appsettings.yml`: primary config file.

Here is an example `docker-compose.yml`, please modify it to your needs.

```
services:
  ss14_admin:
    image: ghcr.io/space-wizards/ss14.admin:1
    container_name: ss14_admin
    user: 1654:1654
    volumes:
      - ./appsettings.yml:/app/appsettings.yml
    ports:
      - 8080:8080
    restart: unless-stopped
```
### Manual compilation

If you hate containers, you can manually publish SS14.Admin and deploy the files yourself. For this you will need Git and the .NET 10 SDK. The server that will run the build needs the matching ASP.NET Core Runtime installed, but does not need the SDK itself.

Clone the git repo, then publish:

```sh
git clone https://github.com/space-wizards/SS14.Admin.git --recurse-submodules
cd SS14.Admin
dotnet publish -c Release -r linux-x64 --no-self-contained
```

The finished build will be dropped in `SS14.Admin/bin/Release/net9.0/linux-x64/publish`. You can copy these into some random location you fancy like `/opt` and run `SS14.Admin` from there. For example:

```
/opt/ss14_admin/
├── appsettings.yml
├── bin
│   ├── SS14.Admin
│   ├── SS14.Admin.dll
    .
```

The actual program files go in a subfolder, and we run it from the parent directory so you don't bulldoze the config files with updates or something.

You can then run SS14.Admin automatically with the following systemd service definition:

```ini
# /etc/systemd/system/ss14-admin.service
[Unit]
Description=SS14.Admin

[Service]
Type=notify
WorkingDirectory=/opt/ss14_admin/
ExecStart=/opt/ss14_admin/bin/SS14.Admin
User=ss14_admin

[Install]
WantedBy=multi-user.target
```

## Configuration

SS14.Admin is an ASP.NET Core app, so it supports configuration both via config file and other sources such as environment variables. You can see [ASP.NET Core's documentation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-9.0) for a more in-depth overview.

Most configuration of SS14.Admin is done via the `appsettings.yml` config file. Here is a complete reference of its contents:

```yaml
Serilog:
    Using: [ "Serilog.Sinks.Console" ]
    MinimumLevel:
        Default: Information
        Override:
            SS14: Debug
            Microsoft: "Warning"
            Microsoft.Hosting.Lifetime: "Information"
            Microsoft.AspNetCore: Warning
            IdentityServer4: Warning
    WriteTo:
        - Name: Console
          Args:
              OutputTemplate: "[{Timestamp:HH:mm:ss} {Level:u3} {SourceContext}] {Message:lj}{NewLine}{Exception}"

    Enrich: [ "FromLogContext" ]

    #Loki:
    #    Address: "http://localhost:3102"
    #    Name: "centcomm"

ConnectionStrings:
    # Connect this to the same PostgreSQL database as your SS14 server
    DefaultConnection: "Server=127.0.0.1;Port=5432;Database=ss14;User Id=ss14-admin;Password=foobar"

# Set this to the domain name you will be hosting SS14.Admin under.
AllowedHosts: "ss14-admin.spacestation14.com"

# If you like to change the port of the webserver change it here, I recommend you reverse proxy this for SSL
urls: "http://localhost:27689/"

# Subpath that the site will be hosted on.
# You can leave this out if you are hosting it behind its own subdomain.
# PathBase: "/admin"

# Make sure this points to the wwwroot, it should be in the same directory as the executable
WebRootPath: "/opt/ss14_admin/bin/wwwroot"

# IP addresses that are allowed to reverse proxy the site.
# Change this if your reverse proxy isn't coming in from localhost,
# for example if SS14.Admin is running in a container,
# you should add the IP of the host in the container network here.
ForwardProxies:
    - 127.0.0.1

# OAuth client information to be able to authenticate admins see below.
Auth:
    Authority: "https://account.spacestation14.com/"
    ClientId: "9e2ce26f-EDIT-THIS-b4d9-8cc08993b33e"
    ClientSecret: "foobar"

authServer: "https://auth.spacestation14.com"
```

```admonish warning
Due to how oauth works, you will require an SSL/HTTPS connection for the login to succeed. It does not matter if it's from a cert authority like Let's Encrypt or self signed. You just need it to be trusted so your browser will actually send over the necessary data.
```

## Authentication config

For admins to be able to log in directly with their SS14 account, you need to register an [OAuth client](../server-hosting/oauth.md) as follows:

1. Log in into and go to https://account.spacestation14.com/Identity/Account/Manage/Developer and click on "New OAuth App".
2. Type in an app name, this can be anything.
3. Set "Authorization callback URL" to the address of your instance with `/signin-oidc` appended. Examples:
  * If your instance is accessible under `https://admin.example.com`, make it `https://admin.example.com/signin-oidc`.
  * If your instance is accessible under `https://example.com/admin`, make it `https://example.com/admin/signin-oidc`.
4. Set "Homepage URL" to the main address that your instance is available at, for example `https://admin.example.com` or `https://example.com/admin`.
5. Copy the **Client ID** to `ClientId` in the config file.
6. Press "Generate new secret" and copy it to `ClientSecret` in the config file.

```admonish warning
Your client secret will only be shown once, if you lose it: make a new one.
```

## Web server config

You will most likely want to run SS14.Admin behind a reverse proxy like Nginx or Caddy to provide TLS 
termination, and to allow you to run multiple services from the same IP address. Here are some examples and 
instructions for some web servers.

Note that SS14.Admin will likely not work without HTTPS, due to cookie security issues.

### Caddy

Caddy is recommended if you don't already have a web server installed, as it is very easy to configure and provides functionality like Let's Encrypt certificates built-in.

```caddy
admin.example.com {
    log {
        output file /var/log/caddy/access-ss14-admin.log
    }

    reverse_proxy 127.0.0.1:<CHANGE TO YOUR PORT>
}
```

### Nginx

```nginx
location / {
    proxy_pass          http://localhost:<CHANGE TO YOUR PORT>;
    proxy_http_version  1.1;
    proxy_set_header    Upgrade $http_upgrade;
    proxy_set_header    Connection keep-alive;
    proxy_set_header    Host $host;
    proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header    X-Forwarded-Proto https;
    proxy_cache_bypass  $http_upgrade;

    # Necessary to avoid errors from too large headers thanks to large cookies.
    proxy_buffer_size        128k;
    proxy_buffers            4 256k;
    proxy_busy_buffers_size  256k;
}
```

## Troubleshooting

### Auth-side "An error occurred while processing your request." on login

*See also: [troubleshooting in the main OAuth page](./oauth.md#auth-side-an-error-occurred-while-processing-your-request).*

This is a generic error code if the OAuth configuration is messed up. See the article linked above for the possible reasons why. If the redirect URI is indeed wrong, please check below.

### Incorrect redirect URI

The redirect URI being wrong is often caused by incorrect reverse proxy config, either on the proxy or app side:

* Make sure your reverse proxy is sending all the required headers, as shown in the configuration examples above.
* If your reverse proxy isn't sending to `localhost`, such as if you are running in a container, make sure to set `ForwardProxies` in SS14.Admin's config file properly.
