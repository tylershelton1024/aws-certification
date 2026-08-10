---
title: "Chapter 1: AWS Cloud Fundamentals - Deeper Dive Notes"
tags: [chapter_01, cloud_fundamentals, deeper_dive, notes]
updated: 2026-08-09
---

# Chapter 1: AWS Cloud Fundamentals - Deeper Dive Notes

Topics that came from questions asked beyond what the book covers directly - kept separate from `notes.md`, which stays scoped to the book's own content.

## Choosing a Service Model: Pros, Cons, and Tradeoffs

**IaaS - when you'd actually use it:**
- You need a specific OS or software that only works with full server-level access.
- Migrating an old/legacy system to the cloud - forcing it into PaaS's constraints can be risky if it doesn't fit the platform's supported setup.
- Your team already has the skills to manage servers themselves.
- Tradeoff: you build and maintain everything yourself, from the OS up.

**PaaS - tradeoffs:**
- Pro: hand off your code and AWS runs it - fast, low operational overhead.
- Con: you're limited to what the platform supports; anything outside that isn't possible.
- Con: harder to migrate away from later - your app grows dependent on that platform's specific deployment model, environment variables, and platform-managed behaviors (scaling, health checks, etc.), not just on a feature you can't use.

**SaaS - tradeoffs:**
- Pro: instant access, usable from anywhere.
- Con: no customization - you get what the vendor built.
- Con: full dependency on the vendor - if they change something or go down, you have no say.

## The Virtualization Layer

- Splits a single physical computer into multiple virtual computers, walled off from each other.
- Analogy: like a building's supervisor/designer, deciding how the building is divided into apartments. It guarantees tenants can't get into - or even see - each other's apartments, even though everyone shares the same underlying building and utilities.
- A single physical host, through virtualization, runs multiple EC2 instances - each EC2 instance is itself a virtual machine. (Correction from my draft notes: it's one physical host running many EC2 instances, not the other way around.)
- This is why customers don't need their own dedicated hardware - it's shared physical hardware, but each customer's slice is locked off from everyone else's. That sharing-with-isolation is what virtualization means.
- Note: EC2's current virtualization is built around AWS's Nitro System. Confidence flag: I haven't verified how deeply CLF-C02 actually tests this specific detail - worth a source check before treating it as guaranteed exam content.

## Runtime

What actually executes your code. Running a Java app requires the Java Runtime Environment; running Node.js code requires the Node runtime. This is what lets the OS know how to run your code at all.

## Middleware

Software that sits between the OS and your application - the "waiter" that carries requests back and forth. Handles things like queuing and prioritizing work so the app and OS can talk to each other.

## Configuration-Level Networking and Security

- **VPC (Virtual Private Cloud)** - your own private slice of AWS's network.
- **Subnets** - smaller pieces a VPC is divided into.
- **Route tables** - control how data moves between subnets.
- **Security groups** - a firewall on an individual instance.
- **Network ACLs** - a firewall at the subnet level.
- **Internet/NAT gateway** - controls whether and how your private resources can reach the internet.

## CIDR Notation

CIDR (Classless Inter-Domain Routing) is a compact way to write a whole range of IP addresses, instead of listing each one individually. A block like `10.0.0.0/16` describes both a starting address and how many addresses are in that range.

**The bit math:**
- An IPv4 address is 32 bits, written as 4 octets of 8 bits each (e.g. `10.0.0.0`).
- The number after the slash is how many of those 32 bits are locked as the fixed network prefix - the rest are free to vary, and each combination of the free bits is one address in the block.
- Fewer locked bits means more room to vary - so counterintuitively, a *smaller* number after the slash means a *bigger* block, not a smaller one.

**Sizing shortcut (works cleanly for /8, /16, /24, /32 - numbers that are multiples of 8):**
- Divide the CIDR number by 8 to get how many whole octets are locked.
- Subtract from 4 total octets to get the free octets.
- Each free octet is a factor of 256, so total addresses = 256^(free octets).
- `/24` -> 3 locked, 1 free -> 256 addresses.
- `/16` -> 2 locked, 2 free -> 256 x 256 = 65,536 addresses.
- `/8` -> 1 locked, 3 free -> 256 x 256 x 256 = 16,777,216 addresses.
- This shortcut only works because those numbers land exactly on octet boundaries. Other common subnet sizes (like /20 or /27) split an octet in half and need actual bit math instead - not covered here.

**Where 256 comes from:** an octet is 8 bits, and each bit is either 0 or 1 (2 states). Every additional bit doubles the possible combinations, so 8 bits = 2^8 = 256 combinations, read as decimal 0-255.

**It's binary underneath:** `10.0.0.0` is really `00001010.00000000.00000000.00000000` - the decimal, dotted format is just a human-friendly translation of the actual 32-bit binary number. Dots are inserted every 8 bits purely for readability.

**Private IP ranges:** `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` are reserved specifically for internal/private networks and are never used directly on the public internet - which is why VPCs conventionally use them. The VPC built for this chapter's hands-on project uses `10.0.0.0/16`, a small slice of the much larger `10.0.0.0/8` reserved space.
