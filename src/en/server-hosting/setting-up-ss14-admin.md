# Setting up SS14.Admin
[SS14.Admin](https://github.com/space-wizards/SS14.Admin/) is a useful web-based admin tool with various [features.](../community/admin/admin-tooling.md)

This document will explain what you will need to set yourself up with your own instence of SS14.Admin

## Prerequisites

- .NET 9 SDK (If you're running a server, you should already have this. If not, get it [here](https://dotnet.microsoft.com/en-us/download/dotnet/9.0))
- A PostgreSQL database already set up with your server(s). ([Some details to that are here](../general-development/setup/server-hosting-tutorial.md))
- A domain name or at least a DDNS domain.
- A web server to do a reverse proxy, like Caddy or Nginx. I am assuming you know how to set this up yourself. (To save your sanity I included the nginx config below though)

## Building

Clone the code, then recursive the latest SS14 which can be easily done with `git submodule update --init --recursive`. Alternatively you can copy in your own codebase too. But it's most likely not needed.

After that you can compile it with `dotnet publish -c Release -r linux-x64 --no-self-contained`.

The files will be dropped in `SS14.Admin/bin/Release/net9.0/linux-x64/publish`. 

`SS14.Admin` is the executable to run, I would recommend copying those files somewhere else like `/opt/SS14.Admin`.

## Configuration

Now for the fun part, create a new file named `appsettings.yml` and paste this example config. I provided some comments for what everything is

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

# Set this to your domain name
AllowedHosts: "central.spacestation14.io"

# If you like to change the port of the webserver change it here, I recommend you reverse proxy this for SSL
urls: "http://localhost:27689/"

# Endpoint for the webpanel, this should be fine
PathBase: "/admin"

# Make sure this points to the wwwroot, it should be in the same directory as the executable
WebRootPath: "/opt/ss14_admin/wwwroot"

# Add your proxy here
ForwardProxies:
    - 127.0.0.1

# Your way of authenticating accounts, the docs will set it up with an ss14 account 
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
This is a pretty important one, it will be your way of authenticating with the webpanel. Anyone with administrator permissions on your server automaticly gets access to the webpanel. We will use Space Station 14 Accounts for this.

1. Log in into and go to https://account.spacestation14.com/Identity/Account/Manage/Developer and click on "New OAuth App"
2. Type in an app name, this can be anything
3. For an Callback url should be `PathBase/signin-oidc`. Should look like this `https://YOURDOMAIN.TLD/admin/signin-oidc`
4. Homepage url should be wherever your pathbase is. Like `https://YOURDOMAIN.TLD/admin/`

Once you pass all that you should get a **Client ID**, that value will go into ``ClientId`` in the config. For your client secret click on **Generate new secret** and put the result into ``ClientSecret``.

```admonish warning
Your client secret will only be shown once, if you lose it make a new one.
```

## Finishing up
Now try running `SS14.Admin` and you should have a working SS14.Admin instance after you visit it on your browser. If everything is looking right to you then all thats left is to set it to start in the background. To actually be able to login (as mentioned two warnings above) you will need to setup SSL on your domain usually with the help of a reverse proxy software. If you use caddy this is probably done for you. For nginx you can use something like [certbot](https://certbot.eff.org/instructions) to generate one with Let's Encrypt.

## Systemd Unit

Here is an example systemd unit for this:

```ini
[Unit]
Description=SS14.Admin

[Service]
Type=notify
WorkingDirectory=/opt/SS14.Admin/
ExecStart=/opt/SS14.Admin/SS14.Admin
User=SS14.Admin
Group=SS14.Admin

[Install]
WantedBy=multi-user.target
```
Of course modify it to your needs first and use `systemctl` to start it up.

## Nginx config
If you want to use nginx, to save your sanity I have provided a config
```json
    location /admin/ {
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
