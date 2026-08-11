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
