# Troubleshooting FAQ

## General

### `System.DllNotFoundException` on ARM (e.g. M1) macs

We do not currently support running SS14/Robust natively on ARM macs. Install x64 .NET and run the client with that instead, it should work via Rosetta 2 emulation.

## Client

## Server

### Port binding failures trying to start server.

Some written out error codes you may have, for ctrl+f'ing: "An attempt was made to access a socket in a way forbidden by its access permissions.", "Only one usage of each socket address (protocol/network address/port) is normally permitted."

By default, the game server needs ports 1212/UDP and 1212/TCP to start. Common occurence here can be *already running an SS14 server which uses the ports*.

#### Windows users

Installing **Docker for Windows** or something related seems to completely screw up the default dynamic port range on your system, and on top of that reserve a ton of ports via an always-running service. This means that *even when Docker isn't running* it, or *any app on your system* can randomely decide to register port 1212 for general purpose stuff. 

If you want to verify this is the case, run `netsh int ipv4 show dynamicportrange tcp`. This *should* default to the following:

```
Protocol tcp Dynamic Port Range
---------------------------------
Start Port      : 49152
Number of Ports : 16384
```

If the `Start Port` lower range of this is like 1024, your system is screwed up AFAICT. This can be fixed by running `netsh int ipv4 set dynamicportrange tcp startport=49152 numberofports=16384` in an elevated command prompt to unfuck the dynamic port range back to IANA recommendations, and then restarting.