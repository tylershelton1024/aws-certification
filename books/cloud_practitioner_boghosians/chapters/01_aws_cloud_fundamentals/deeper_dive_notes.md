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
- **Internet gateway** - the door between a VPC and the public internet. One per VPC. See "The Internet Gateway, In Depth" below - this is a different thing from a NAT gateway, even though they sound similar.
- **NAT gateway** - a separate resource, used by *private* subnets that need outbound-only internet access (e.g. to download updates) without being directly reachable from the internet. Unlike an internet gateway, a NAT gateway has an hourly charge plus per-GB data fees - one of the "hidden cost" traps flagged early on.

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

## The Internet Gateway, In Depth

- Analogy: the internet gateway is the front gate of a gated neighborhood (the VPC) - the only way in or out to the public road (the internet).
- Just attaching it isn't enough by itself. A route table still needs a rule pointing traffic at it - like a street sign telling cars "if you're leaving the neighborhood, go this way." Without that route, the gate exists but nothing knows to use it.
- One internet gateway attaches to one VPC - a 1-to-1 relationship.
- It does two jobs: gives the route table something to point at for internet-bound traffic, and translates between an instance's private IP (used inside the VPC) and its public IP (seen by the outside world) - a form of NAT.
- Cost: unlike a NAT gateway, an internet gateway has **no hourly charge**. You only pay for actual data transfer out, same as usual. Attaching one doesn't add anything new to a billing alarm's radar by itself.

## Security Groups Are Stateful (and the Full Request/Response Path)

This is the full chain of what actually happens when someone reaches a deployed app, using every piece built for the hands-on project:

1. Browser sends a request to the EC2 instance's **public IP**.
2. It hits the **internet gateway** first - the only door in. The gateway NAT-translates the destination from public IP to private IP.
3. The **route table**'s `0.0.0.0/0 -> internet gateway` rule is what makes the subnet "public" in the first place - without it, there's no path in at all.
4. The **security group** checks the request against its inbound rules (e.g. an HTTP rule allowing port 80).
5. The request reaches the instance and gets handed to whatever's listening on that port (e.g. a Flask app).

For the response going back out: **security groups are stateful** - if a request was allowed in, the matching response is automatically allowed back out, with no separate outbound rule needed. This is different from Network ACLs, which are stateless and need explicit rules in both directions (not something this project needed, since only the default, allow-all NACL was used).

## Public vs. Private IP Addresses (and How "My IP" Is Found)

- Every request sent over a network includes a return address (the source IP) - otherwise a response could never find its way back. That's the whole mechanism behind an AWS console feature like "My IP" when creating a security group rule: it just reports whatever source IP a request arrived from.
- This detects your **public** IP - the address your home router presents to the internet - not the private IP of your actual laptop (something like `192.168.1.5`) on your home network. Home networks use the same private IP ranges covered above.
- Your home router does its own NAT translation, the same underlying concept as what the internet gateway does for the VPC: translating a private, internal address into one shared public address before traffic leaves the network.

## HTTP vs. HTTPS: Different Default Ports

- HTTPS is not "layered on top of" HTTP in a stacking sense - it's the same HTTP messages, wrapped in encryption (TLS/SSL) so they can't be read in transit.
- The part that actually matters operationally: **HTTP and HTTPS use different default ports.** HTTP defaults to port 80. HTTPS defaults to port 443 - a completely separate "door" on a server.
- Real bug this caused: a security group only had port 80 open. Typing a bare IP address into some browsers causes an automatic upgrade to `https://`, which tries port 443 instead - a port with no rule allowing it through. Result: a silent connection timeout, with a completely different root cause than "the security group is wrong" (which had already been fixed by that point). Explicitly typing `http://` avoided the auto-upgrade.

## SSH Key Pairs

- An EC2 key pair is a public/private key pair, not a password. AWS keeps the public half; you download and keep the private half (a `.pem` file) - whoever holds that file can log into the server.
- Created during EC2 launch, in the "Key pair (login)" step - before the instance ever launches.
- Should live outside any git repo (e.g. a `.ssh` folder in the user directory), never committed - `.gitignore` in this repo excludes `*.pem` as a hard safeguard.
- Troubleshooting note: a "Permission denied" error when connecting means the network connection itself worked (so security groups/routing/gateway are all fine) - it's specifically the key that was rejected. That narrows the problem down to the key file, its permissions, or the username, not the network path.
- Default SSH username for Amazon Linux AMIs: `ec2-user`.

## Debugging Methodology

The general approach used to debug the hands-on app not loading, in order - worth remembering as a pattern, not just the specific fixes:

1. **Rule out the simplest explanation first.** Before assuming something is broken, check if enough time has even passed (the setup script needs a couple minutes to run).
2. **Check indirect evidence next.** The system/boot log shows what happened during startup - useful, but can be noisy and not always show the specific thing you're looking for.
3. **Go straight to the most direct evidence available.** Instead of guessing from logs, SSH in and ask the actual service directly (`systemctl status`) whether it's running and why.
4. **Use what already works to narrow down what doesn't.** SSH (port 22) working over the same public IP proved the network path (gateway, route table, public IP) was fine - which meant the problem had to be the security group specifically, not the whole network stack.

This same escalation pattern - simple check, then indirect evidence, then direct evidence, then use what works to isolate what doesn't - applies far beyond AWS.
