---
title: "Chapter 2: AWS Global Infrastructure - Deeper Dive Notes"
tags: [chapter_02, global_infrastructure, deeper_dive]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Deeper Dive Notes

Source: written by the assistant based on a reinforcement conversation and general AWS architecture knowledge - not pulled directly from the book. Covers topics that go beyond what Chapter 2's core content explains.

## The "Close But Not Too Close" Tradeoff (Regions/AZs)

Availability Zones being far enough apart to avoid a shared local disaster, and close enough together to fail over between almost instantly, are not two separate design goals - they come from the same underlying design choice. Being far enough apart is what buys fault isolation and redundancy; being close enough together is what makes near-instant failover and physical proximity to customers possible. AWS's specific choice of AZ spacing is what threads that needle.

## CloudFront Is a Router, Not a Compute Service

Easy mix-up: CloudFront is a checker/router for already-cached content - it decides whether a request can be served from a nearby edge location or needs to go back to the origin server. It does not run application code. The "milliseconds matter, real-time gaming/compute" use case belongs to Local Zones, which can actually run compute - not to CloudFront or edge locations, which only cache and deliver.

## Region/AZ, Edge Locations, and Local Zones Are Two Separate Systems, Not One Hierarchy

Easy mistake: treating Region/AZ, Edge Locations, and Local Zones as one nested hierarchy. They're actually two separate systems that connect to each other, not one system inside another.

- **System 1 - the infrastructure backbone:** Region -> Availability Zones. This is where your actual servers, compute, and data *live*. A handful of AZs per region.
- **System 2 - the caching layer:** Edge Locations, run by CloudFront. Hundreds of them globally, *not* organized by or nested inside any AZ - a completely separate, much larger network layered on top, whose only job is caching content closer to users.
- **Local Zones** are a third, distinct thing: an extension of a *specific region*, placed in another city, for actual compute (not caching) that needs to sit very close to users - e.g. live streaming, real-time gaming.

Worked example (a global video streaming service): the source video and backend logic live in a region, spread across its AZs, for durability and redundancy. CloudFront separately pushes cached copies of that video out to edge locations everywhere, unrelated to AZ boundaries. Local Zones only enter the picture if the service needs actual low-latency *compute* near users, like live streaming - a separate decision from where content gets cached.

## Fault Tolerance Is the Mechanism, High Availability Is the Outcome

These two terms get used almost interchangeably, but they describe different things:

- **Fault tolerance** - the mechanism. A redundant backup is already in place before something breaks, ready to take over instantly with zero customer-noticeable impact.
- **High availability** - the outcome. The system as a whole stays up and accessible. Fault tolerance (e.g. redundancy across AZs) is one of the main tools used to achieve high availability - they're not two independent, parallel properties; one produces the other.

## Multi-AZ Redundancy Is a Customer Decision, Not Automatic

AWS guarantees the infrastructure itself is redundant - the other Availability Zones in a region exist, are powered, connected, and ready. That does not mean any single application automatically benefits from that redundancy.

Whether a specific application fails over to another AZ during an outage depends entirely on whether the customer architected it to run across multiple AZs in the first place - for example, multiple instances behind a load balancer spanning AZs, or a Multi-AZ database configuration. If an application is only deployed in one AZ, and that AZ goes down, the application goes down too - AWS having other healthy AZs sitting right next to it does not help, because nothing was ever deployed there.

This is squarely part of the Shared Responsibility Model: AWS secures and maintains the underlying infrastructure (the AZs exist and are reliable), but architecting an application to actually use that redundancy is the customer's job - "reliability in the cloud," the same bucket as permissions and patching.

**Real example from this project:** `CCP_app`'s EC2 instance runs in a single, specific Availability Zone. If that exact AZ went down, the app would go offline - it has no load balancer, no second instance in another AZ, and no auto-scaling group. Recovering it would currently require the same terminate-and-relaunch process used earlier tonight, just triggered by an AZ outage instead of a code update. Building real automatic failover would mean deliberately deploying across multiple AZs - not something this project has done, or currently needs, for a small learning app.

## Auto Scaling (What Actually Handles Traffic Spikes)

Availability Zones provide redundancy and fault isolation - not built-in capacity elasticity. An AZ does not sit there holding a giant pile of idle spare capacity "just in case" traffic spikes.

What actually handles a sudden traffic spike (e.g. a flash sale) is a separate AWS service called **Auto Scaling** (via an Auto Scaling Group): it automatically launches new compute instances when demand increases, and terminates them again when demand drops, rather than relying on pre-provisioned idle capacity. It's commonly paired with a load balancer that distributes traffic across whatever instances currently exist, which can span multiple AZs at once.

Note on scope: Auto Scaling is more properly Compute Services material (a later chapter), not core Global Infrastructure content - it's filed here because it came up naturally while reinforcing this chapter's traffic-spike question, not because it belongs to Chapter 2's own subject matter.

## Elastic Load Balancing (The Missing Piece for Multi-AZ Redundancy)

Deploying instances in multiple Availability Zones isn't enough by itself - something has to actually distribute incoming traffic across those instances, and detect when one goes unhealthy so it stops sending traffic there. That's the job of an **Elastic Load Balancer (ELB)**.

- Sits in front of the application, spanning multiple AZs.
- Distributes incoming traffic across whichever instances are currently healthy.
- Continuously checks instance health - if one instance (or an entire AZ) goes down, the load balancer simply stops routing traffic there and sends everything to the remaining healthy instances instead.
- This is the actual mechanism that makes "multi-AZ redundancy" real for an application - instances in multiple AZs *plus* a load balancer routing across them, together. Neither piece alone is sufficient: instances without a load balancer means no automatic traffic redirection when one fails; a load balancer without instances in more than one AZ means there's nothing to fail over to.
- Often paired with Auto Scaling: as Auto Scaling adds or removes instances based on demand, the load balancer automatically starts or stops routing traffic to them as they come online or get terminated.

Note on scope: same as Auto Scaling above - Elastic Load Balancing is more properly Compute/Networking Services material from a later chapter, filed here because it directly completes the multi-AZ redundancy picture this chapter's reinforcement conversation was building toward.

## Multi-AZ Redundancy Does Not Protect Against a Region-Wide Outage

Multi-AZ redundancy (multiple AZs plus a load balancer) protects against a single Availability Zone going down. It does not protect against a problem affecting an entire Region, because every AZ used is still inside that one Region - and regions are fully isolated from each other, which cuts both ways: nothing bad in one region spreads to another, but redundancy built inside one region doesn't cross that boundary either.

Protecting against a full Region outage requires deploying into a **second Region** as well - multi-region architecture, not just multi-AZ. This is a materially bigger step up in complexity and cost than multi-AZ, and is a separate decision from it.

## Cache Refresh: TTL Expiration vs. Invalidation

Cached content at an edge location does not stay there forever. Two ways stale cached content gets refreshed:

- **TTL (Time To Live) expiration** - each cached object has a TTL. Once it expires, the next request for that object causes a fresh fetch from the origin automatically, with no action needed from anyone.
- **Invalidation** - an explicit CloudFront feature that lets you manually force a specific cached path to be dropped everywhere immediately, rather than waiting for the TTL to expire naturally. Useful when you can't wait - e.g. a broken image was just fixed and shouldn't keep serving the old cached version for the rest of its TTL.

## CDN Security Features: Geoblocking, SSL, and DDoS Protection

CloudFront provides three distinct security features beyond its core caching job:

- **Geoblocking** - allows or blocks requests based on which country they appear to come from, using the requester's IP geolocation. Common use case: enforcing content-licensing restrictions, which is why some streaming shows are only available in certain countries.
- Real limitation: geoblocking only checks the *apparent* source IP, not a person's true physical location. A VPN or proxy routes traffic through a server in a different country, making the request genuinely appear to originate there - CloudFront has no way to see through that. This is the same mechanism people use to access another country's Netflix library.
- SSL encryption is actually two separate hops, not one continuous tunnel: CloudFront decrypts the viewer's request at the edge location, and - only on a cache miss - opens a *separate* encrypted connection to the origin. Encrypting the viewer-to-edge leg does not automatically encrypt the edge-to-origin leg; each hop needs its own encryption.
- The viewer-to-edge leg matters most for protecting the user specifically, since it happens on every single request (cache hit or miss) and travels over whatever network the viewer is actually on (public WiFi, their ISP) - the most exposed stretch of the journey.
- Edge-to-origin encryption is itself a Shared Responsibility Model matter: AWS provides the capability (CloudFront's origin protocol policy can require HTTPS), but the customer must configure it correctly - setting the policy to require HTTPS, and installing a valid SSL certificate on their own origin server. Left misconfigured, that leg can stay unencrypted even though AWS offered the tool to prevent it. Same "AWS provides the tool, customer configures it correctly" pattern already seen with multi-AZ redundancy and load balancing.
- **AWS Shield** (Standard tier) is automatically included at no extra cost with CloudFront, providing DDoS protection. CloudFront's edge network spans hundreds of locations globally, so a flood of malicious traffic gets absorbed and spread across that whole network rather than overwhelming one single origin server - Shield adds further automatic protection on top of that natural spread.

## EC2 Overview (Compute Services Preview)

Note on scope: this is more properly Compute Services material (a later chapter), not core Global Infrastructure content - filed here because Tyler flagged EC2 as a topic he wanted a real deeper dive on while working through this chapter.

- **AMI (Amazon Machine Image)** - the template an instance boots from: an OS plus whatever software is pre-installed on it. AWS provides standard AMIs (like the Amazon Linux 2023 image `CCP_app` uses); you can also build and save your own customized one.
- **Instance type** - defines an instance's hardware: CPU, memory, and network performance. Named like `t3.micro` - the family letter signals what it's optimized for (general purpose, compute-optimized, memory-optimized, etc.), the number is the generation, and the size scales the resources up.
- **EBS (Elastic Block Store)** - the virtual hard drive attached to an instance. Persists independently of the instance's own lifecycle - an EBS volume (and its data) can outlive the instance it was attached to, unlike temporary "instance store" storage, which is deleted when the instance stops or terminates.
- **On-Demand** - the pricing model of paying per hour/second, with no commitment. What `CCP_app` uses.
- **Reserved Instances** - committing to 1-3 years of usage for a steep discount, appropriate when you know something will run long-term.
- **Spot Instances** - bidding on AWS's unused spare compute capacity for very cheap, but AWS can reclaim that capacity with little notice - good for interruptible workloads only, bad for anything that must stay up continuously.
