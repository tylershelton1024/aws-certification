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

## Cache Refresh (TTL vs. Invalidation)

Cached content at an edge location doesn't stay forever. It refreshes either automatically once its TTL (Time To Live) expires, or immediately via an invalidation - an explicit request to drop a specific cached path everywhere right away, useful when you can't wait for the TTL to naturally expire.
