---
title: "Chapter 2: AWS Global Infrastructure - Deeper Dive Flashcards"
tags: [chapter_02, global_infrastructure, deeper_dive, flashcards]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Deeper Dive Flashcards

Source: written by the assistant from deeper_dive_notes.md. Source of truth for the cards - `flashcards.html` (this chapter) and `../../../../../all_flashcards.html` (whole book) are generated from files like this one and need to be regenerated if cards here change.

## AZ Spacing Tradeoff

AZs being far enough apart (fault isolation, redundancy) and close enough together (near-instant failover, physical proximity to customers) aren't separate design goals - both come from the same underlying spacing choice AWS makes.

## CloudFront (Router, Not Compute)

CloudFront checks whether a request can be served from a nearby cached copy or needs to go back to the origin - it does not run application code. Latency-sensitive compute (real-time gaming, live production) is a Local Zone job, not CloudFront's.

## Region/AZ vs. Edge Locations (Two Separate Systems)

Region/AZ is the infrastructure backbone where servers and data live. Edge Locations (run by CloudFront) are a separate, much larger caching network layered on top, not nested inside any AZ. Local Zones are a third, distinct extension of a region for actual compute near users.

## Fault Tolerance vs. High Availability

Fault tolerance is the mechanism - a redundant backup ready to take over with zero noticeable impact. High availability is the outcome - the system as a whole stays up. Fault tolerance is one of the main tools used to achieve high availability, not a separate parallel property.

## Multi-AZ Redundancy (Customer Responsibility)

AWS's Availability Zones being redundant does not automatically make your application redundant. An application only fails over to another AZ if the customer deliberately architected it to run across multiple AZs (e.g. a load balancer plus instances in multiple AZs, or a Multi-AZ database). This is part of the customer's side of the Shared Responsibility Model, not something AWS does for you automatically.

## Auto Scaling

The AWS service that automatically launches new compute instances when demand increases and terminates them again when demand drops, instead of relying on an Availability Zone holding pre-provisioned idle capacity. Often paired with a load balancer distributing traffic across the resulting instances, potentially across multiple AZs. AZs provide redundancy and fault isolation - Auto Scaling is what actually provides capacity elasticity for traffic spikes.

## Elastic Load Balancing (ELB)

The missing piece that makes multi-AZ redundancy real: an ELB sits in front of an application, spans multiple AZs, and distributes incoming traffic across whichever instances are currently healthy. It continuously checks instance health - if one instance or an entire AZ goes down, it stops routing traffic there automatically. Instances in multiple AZs without a load balancer means no automatic redirection; a load balancer without instances in more than one AZ means nothing to fail over to. Both pieces are required together.

## Multi-Region vs. Multi-AZ Redundancy

Multi-AZ redundancy protects against a single Availability Zone going down, but every AZ used is still inside one Region - it does not protect against a problem affecting the whole Region. Protecting against a full Region outage requires deploying into a second Region as well, a bigger step up in complexity and cost than multi-AZ, and a separate decision from it.

## TTL (Time To Live)

How long a cached object is allowed to sit at an edge location before it's considered stale. Once it expires, the next request for that object automatically triggers a fresh fetch from the origin - no action needed from anyone.

## Invalidation

An explicit CloudFront feature that manually forces a specific cached path to be dropped everywhere immediately, instead of waiting for its TTL to expire naturally. Useful when you can't wait - e.g. a broken image was just fixed and shouldn't keep serving the old cached version.

## Cache Refresh: TTL vs. Invalidation

Two different ways stale cached content gets refreshed, and when each applies: TTL expiration happens automatically and passively - you don't do anything, it just eventually happens. Invalidation is manual and immediate - you actively request it, for the specific case where you can't afford to wait for the TTL. Same end result (fresh content), different triggers.

## CDN (Content Delivery Network)

The general industry term for a network of distributed servers that cache and deliver content close to end users. CloudFront is AWS's specific implementation of a CDN.

## SSL/TLS (Encryption)

The encryption technology behind HTTPS - scrambles data in transit so it can't be read if intercepted. TLS is the modern, more accurate name for the same underlying technology; SSL is the older name people still commonly use, and the two terms are used interchangeably in practice.

## VPN (Virtual Private Network)

Routes a device's internet traffic through a server in a different location before it reaches its destination, making requests appear to originate from that server's location instead of the device's real one. This is exactly why a VPN can circumvent geoblocking - the check only sees the VPN server's apparent location.

## Geoblocking

CloudFront can allow or block requests based on which country they appear to come from, using the requester's IP geolocation - commonly used to enforce content-licensing restrictions. Real limitation: it only checks the apparent source IP, not true physical location, so a VPN or proxy (which makes a request genuinely appear to originate elsewhere) can circumvent it.

## AWS Shield

Automatically included at no extra cost with CloudFront, providing DDoS protection. Works alongside CloudFront's naturally distributed edge network, which already spreads a flood of malicious traffic across hundreds of locations instead of overwhelming one single origin server.

## AMI (Amazon Machine Image)

The template an EC2 instance boots from: an OS plus whatever software is pre-installed on it. AWS provides standard AMIs; you can also build and save your own customized one.

## Instance Type

Defines an EC2 instance's hardware: CPU, memory, and network performance. Named like `t3.micro` - the family letter signals what it's optimized for (general purpose, compute, memory, etc.), the number is the generation, and the size scales the resources up.

## EBS (Elastic Block Store)

The virtual hard drive attached to an EC2 instance. Persists independently of the instance's own lifecycle - an EBS volume (and its data) can outlive the instance it was attached to, unlike temporary instance store storage, which is deleted when the instance stops or terminates.

## On-Demand (EC2 Pricing)

The default EC2 pricing model: pay per hour or second, with no commitment.

## Reserved Instances

An EC2 pricing model where you commit to 1-3 years of usage in exchange for a steep discount - appropriate when you know something will run long-term.

## Spot Instances

An EC2 pricing model where you bid on AWS's unused spare compute capacity for very cheap - but AWS can reclaim that capacity with little notice. Good for interruptible workloads only, bad for anything that must stay up continuously.
