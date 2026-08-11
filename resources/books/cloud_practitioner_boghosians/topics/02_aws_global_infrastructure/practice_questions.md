---
title: "Chapter 2: AWS Global Infrastructure - Practice Questions"
tags: [chapter_02, global_infrastructure, practice_questions]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Practice Questions

Source: written by the assistant based on your notes, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Scoped to the book's core content only - see `deeper_dive_questions.md` for questions on topics that went beyond the book (once that content exists). Answers are in the Answer Key at the bottom, so you can try answering first.

## Core Concepts Questions

1. What is the relationship between an AWS Region and an Availability Zone?
   - A) A Region is a single data center; an AZ is a group of Regions
   - B) Regions and Availability Zones are the same thing
   - C) An Availability Zone spans multiple Regions
   - D) A Region is made up of multiple Availability Zones

2. Why does AWS physically separate Availability Zones from each other within a region?
   - A) To ensure a local disaster affecting one AZ doesn't take down the others
   - B) To reduce internet latency for global customers
   - C) To comply with international data transfer laws
   - D) To reduce the cost of electricity

3. What is the primary function of an AWS Edge Location?
   - A) Running EC2 instances closer to customers
   - B) Storing primary copies of a company's database
   - C) Caching content (like videos and images) close to end users for faster delivery
   - D) Hosting an entire AWS Region's worth of services

4. Which AWS service manages content delivery through edge locations?
   - A) Amazon S3
   - B) Amazon CloudFront
   - C) AWS Local Zones
   - D) Amazon EC2

5. What is a key difference between an Edge Location and an AWS Local Zone?
   - A) Edge Locations can run compute workloads, Local Zones cannot
   - B) There is no meaningful difference between the two
   - C) Edge Locations are always larger than Local Zones
   - D) Local Zones can run compute workloads, Edge Locations only cache/deliver content

6. Under the Shared Responsibility Model, who is responsible for patching an EC2 instance's operating system after you launch it?
   - A) The customer
   - B) AWS, as part of infrastructure security
   - C) Neither party - this is automatic
   - D) It depends on the region

7. What does "fault tolerance" mean in AWS's infrastructure design?
   - A) The system never experiences any failures
   - B) Failures are detected but not automatically handled
   - C) Redundancy is already in place so a failure doesn't take the system down
   - D) Only paid support tiers get fault-tolerant infrastructure

8. Why can AWS fail over from one Availability Zone to another almost instantly during an outage?
   - A) Failover only works between different Regions, not AZs
   - B) AZs within a region are connected through private, always-on networks
   - C) AWS pauses all traffic until a human manually switches AZs
   - D) It cannot - failover takes several hours

## Answer Key

1. D - A region is made up of multiple Availability Zones.
2. A - Physical separation means a local disaster hitting one AZ doesn't take down the others.
3. C - Edge locations cache content close to users; they don't process/compute anything.
4. B - Amazon CloudFront is AWS's CDN, delivering content through edge locations.
5. D - Local Zones can run compute workloads; edge locations only cache and deliver content.
6. A - Patching the OS on an instance you launched is the customer's responsibility under the Shared Responsibility Model.
7. C - Fault tolerance means redundancy is already built in, so a failure doesn't take the system down.
8. B - AZs within a region are connected through private, always-on networks, enabling near-instant failover.
