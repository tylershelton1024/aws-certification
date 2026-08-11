---
title: "Chapter 2: AWS Global Infrastructure - Flashcards"
tags: [chapter_02, global_infrastructure, flashcards]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Flashcards

Source: written by the assistant from notes.md. This is the source of truth for the cards - `flashcards.html` (this chapter) and `../../../../../all_flashcards.html` (whole book) are generated from files like this one and need to be regenerated if cards here change.

## Region

A broad geographic area where AWS resources can live. Fully isolated from every other region. Customers choose which region their resources run in.

## Availability Zone (AZ)

One or more data centers within a region, isolated enough to survive a local disaster on its own, but close enough to other AZs in the same region to work together effectively. A region is made up of multiple AZs.

## Edge Location

A small AWS data center that caches content (video, images, other data) close to end users, so requests don't have to travel all the way to the origin server. Cannot process/compute anything - caching and delivery only.

## Amazon CloudFront

AWS's CDN (Content Delivery Network). Delivers content through edge locations, checking whether requested data is already cached nearby before going back to the origin. Also handles dynamic content (e.g. real-time dashboards, personalized recommendations), not just static files.

## AWS Local Zone

A physical extension of a region, placed in another city to bring AWS infrastructure closer to a specific population of users. Still fully managed by AWS. Used for latency-sensitive workloads (real-time gaming, live production, virtual desktops) where milliseconds matter. Unlike an edge location, a Local Zone can actually process/compute workloads.

## Shared Responsibility Model (Region/AZ context)

AWS secures the physical infrastructure, network hardware, power, and cooling, and keeps core services like EC2 and S3 reliable. The customer is responsible for permissions, firewalls, security *in* the cloud, and patching whatever they deploy (e.g. an EC2 instance they spin up). Most security incidents come from the customer's side of this line, not AWS's.

## Fault Tolerance

Redundancy - a backup is already in place before something breaks, so a failure doesn't take the system down.

## High Availability

The property of a system continuing to run even when part of it goes down - enabled by spreading infrastructure across multiple Availability Zones connected by private networks, so traffic can fail over almost instantly.
