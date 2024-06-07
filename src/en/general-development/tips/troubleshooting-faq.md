# Troubleshooting FAQ

This is a long list of different issues and hopefully their solutions. If you need any further help, feel free to reach out in the Discord.

## General

### `System.DllNotFoundException` on ARM (e.g. M1) macs

We do not currently support running SS14/Robust natively on ARM macs. Install x64 .NET and run the client with that instead, it should work via Rosetta 2 emulation.

### Only Some Projects Are Loading

Make sure that you've completed [Git For The SS14 Developer](../setup/git-for-the-ss14-developer.md)!

You likely are missing some of the submodules.

### Something Is Wonky With Python

See: [Development Environment#Troubleshooting](../setup/development-environment.md#troubleshooting).

## Server

### Port Binding Failures At Server Startup

If you get an error like:
- `“An attempt was made to access a socket in a way forbidden by its access permissions`
- `“Only one usage of each socket address (protocol/network address/port) is normally permitted`

You likely already have something bound to the ports that SS14 needs to run.

By default, the game server needs ports `1212/UDP` and `1212/TCP` to start. 

You might already be running an SS14 server which uses the ports.

### Windows Port Issues

Installing **Docker for Windows** or something related seems to completely screw up the default dynamic port range on your system.

This means that even when Docker isn’t running it, or any app on your system can randomely decide to register port 1212 for general purpose stuff. 

If you want to verify that this is what is happening, run:
```bash
netsh int ipv4 show dynamicportrange tcp
```

Which should return (if it is all working fine):
```bash
Protocol tcp Dynamic Port Range
---------------------------------
Start Port      : 49152
Number of Ports : 16384
```

If your system is broken, you starting port is something like `1024`.

To fix this, you can try to run this in an elevated command prompt, then restart:
```bash
netsh int ipv4 set dynamicportrange tcp startport=49152 numberofports=16384
```