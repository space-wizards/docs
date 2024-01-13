# Wizard's Den Infrastructure

This is a reference for how the official Wizard's Den game server infrastructure works. It may help you make educated decisions about hardware required or how to set up your infrastructure. This is not an endorsement of any technique or provider, it's just what we use.

## Hardware

If I don't list something like network bandwidth it's cuz I'm too lazy to check. You're not gonna run out, don't worry.

### Moon

Moon is our NEW central server. When done, it'll host all non-critical infrastructure and game server database and so on. Hosted by Hetzner in Germany. 

Specs: (AX41-NVMe from Hetzner)

### Centcomm

Centcomm is our OLD central server that hosts both the central SS14 infrastructure like authentication, aswell as Wizard's Den infrastructure like the game database, wiki, forum, etc... It is hosted in US East.

Specs:
* **CPU:** Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz
* **RAM:** 16 GB
* **SSD:** 256 GB
* **HDD:** 2 TB
* **Network:** 150 TB bandwidth, gigabit

This serves all CDN downloads and it comes up to less than 2 TB/month bandwidth.

### Lizard

Hosts Wizard's Den Lizard and Wizard's Den Salamander in US West.

Specs:
* **CPU:** AMD Ryzen 5 5600X 6-Core Processor
* **RAM:** 16 GB
* **SSD:** 256 GB
* **Network:** 150 TB bandwidth, gigabit

This is our most loaded server, and it comes out to 5 TB/month bandwidth max.

### Miros

Auctioned server rented from Hetzner, hosted in Germany.

* **CPU:** Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz
* **RAM:** 64 GB
* **SSD:** 512x2 GB (RAID 1)

### Noodle

Noodle acts as a hypervisor and runs two separate systems, Leviathan and OpenDream1. Hosted in Miami.

* **CPU:** AMD Ryzen 5 5600X 6-Core Processor
* **RAM:** 64GB
* **SSD:** 512 GB

Each VM guest has 6 CPUs and 16 GB RAM assigned.



