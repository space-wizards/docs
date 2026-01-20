# Setting up High Bandwith Transfer

As of [Robust Toolbox Version 271.1.0](https://github.com/space-wizards/RobustToolbox/blob/40b10f0dccfe568ccd7dc3c6f6ee87a63bad97ee/RELEASE-NOTES.md#27110) the engine supports a high bandwith transfer mode using websockets.

This feature is used in resource upload/download allowing game admins to upload bigger prototypes quicker while allowing players to also download them as fast. But can also be implemented to do anything else you may want via `ITransferManager` that requires sending and receiving big traffic.

While Lidgren (The main networking netcode) is the main fallback for the transfer system. To get the full speed benefits, some additional options need to be configured on the server.

A reverse proxy is highly recommended to be used here to allow you to encrypt the websocket traffic, but is not required. We will assume you know how to configure your web server with SSL/Know how to handle yourself if you do not wish to encrypt the data.

### Game server config
The main [CVars](https://github.com/space-wizards/RobustToolbox/blob/40b10f0dccfe568ccd7dc3c6f6ee87a63bad97ee/Robust.Shared/CVars.cs#L409-L448) are located here (Note this is a permalink, more CVars may exist by the time this documention was written).

The main one to worry about is `transfer.http_endpoint`, this needs to point to the servers HTTP API (The thing with the `/status` and `/info` if you ever queried that). In most cases this will be the same value as `hub.server_url` but instead replacing `ss14://` with `http://` and `ss14s://` with `https://`.

```admonish info "Straight to prod!!!"
You can set these directly on a live server by editing the CVars via the `sudo cvar` command.

Note only players connecting after you enable the http transfer system will actually be using high bandwith systems while the already connected players will stay on the lidgren fallback until they reconnect.

Obviously for the changes to persist, you will need to also set it in your config.
```

```toml
[transfer]
http = true
http_endpoint = "https://leviathan.spacestation14.com/vulture"
```

If you do not wish to use encryption or wish to use an IP instead, your config may look like this instead:

```toml
[transfer]
http = true
http_endpoint = "http://203.0.113.125:1212"
```

If you are not using a reverse proxy... this should just work now! Try to (re)connect and see if you are sucessfully managing to connect!

If you are, keep reading.

```admonish warning "Be sure to reload and not restart!"
Most web servers support reloading the config instead of needing to fully restart. You should do this  **especially** after you setup websockets, as the connection getting closed will disconnect all players.
And restarting the web server will cause it to close all connections.

So instead of `systemctl restart nginx` use `systemctl reload nginx` (Or whatever you have in place for your web server.)

If you are using something non standard look up how to reload its config in place.
```

### Nginx example
Websockets in nginx require you to pass the `Upgrade` and `Connection` headers, we follow nginx's example config for websockets per their [documention](https://nginx.org/en/docs/http/websocket.html).

```
http {
    map $http_upgrade $connection_upgrade {
        default upgrade;
        ''      close;
}

server {
    ...

    location / {
        proxy_set_header    Host $host;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto https;
        proxy_set_header    Upgrade $http_upgrade;
        proxy_set_header    Connection $connection_upgrade;
        proxy_pass http://localhost:1212/;
    }
}
```


### Caddy example
Caddy should just automatically forward the right headers by just using the usual [`reverse_proxy` directive](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy).

Although be careful, as reloading the config will close active websockets connections by default [(I am not sure why this is the default)](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy#streaming) which will cause your players to get disconnected from the server, so we recommend setting `stream_timeout` and `stream_close_delay`.

```
example.com {
    reverse_proxy localhost:1215 {
            # Yes this does technically mean that if a player stays connected on the server
            # for 12 hours in a single session they will get disconnected. 
            # But honestly... they should be getting a life and touching grass.
            stream_timeout 12h
            stream_close_delay 12h
    }
}
```
