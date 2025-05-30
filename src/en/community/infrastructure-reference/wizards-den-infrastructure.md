# Wizard's Den Infrastructure

This is a reference for how the official Wizard's Den game server infrastructure works. It may help you make educated decisions about hardware required or how to set up your infrastructure. This is not an endorsement of any technique or provider, it's just what we use.

## Hardware

If I don't list something like network bandwidth it's cuz I'm too lazy to check. You're not gonna run out, don't worry.

### Moon

Moon is our central server. It hosts all non-critical infrastructure like the game server database, Forums, Wiki, Robust.CDN and so on. (The hub/auth are considered critical and hosted on another machine.)

Specs: AX41-NVMe from Hetzner in Germany

### Lizard

Hosts Wizard's Den Lizard and Wizard's Den Salamander in US West.

Specs:
* **CPU:** AMD Ryzen 5 5600X 6-Core Processor
* **RAM:** 16 GB
* **SSD:** 256 GB
* **Network:** 150 TB bandwidth, gigabit

This is our most loaded server, and it comes out to 5 TB/month bandwidth max.

### Noodle (Hypervisor for Leviathan)

Noodle acts as a hypervisor and runs two separate systems, Leviathan and OpenDream1. Hosted in Miami.

Leviathan hosts Wizard's Den Leviathan and Wizard's Den Vulture in US East.

* **CPU:** AMD Ryzen 5 5600X 6-Core Processor
* **RAM:** 64GB
* **SSD:** 512 GB

Each VM guest has 6 CPUs (Dedicated to the VM) and 16 GB RAM assigned.



