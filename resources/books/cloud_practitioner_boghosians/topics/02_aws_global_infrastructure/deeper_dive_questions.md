---
title: "Chapter 2: AWS Global Infrastructure - Deeper Dive Questions"
tags: [chapter_02, global_infrastructure, deeper_dive, practice_questions]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Deeper Dive Questions

Source: written by the assistant based on `deeper_dive_notes.md` and our conversation - not pulled from an official AWS question bank. Covers topics that went beyond the book's core content - see `practice_questions.md` for questions on the book material itself. Answers are in the Answer Key at the bottom, so you can try answering first.

## Questions

1. A company deploys their application on a single EC2 instance in one Availability Zone. That Availability Zone experiences an outage. What happens to the application?
   - A) AWS automatically fails it over to another Availability Zone with no interruption
   - B) AWS automatically relaunches the instance in the same Availability Zone within seconds
   - C) The application goes offline, since it was never deployed to more than one Availability Zone
   - D) The application's data is lost permanently

2. What determines whether AWS's Availability Zone spacing provides both fault isolation AND fast failover at the same time?
   - A) Both come from the same underlying design choice - far enough apart for isolation, close enough for near-instant failover
   - B) They are two unrelated properties that happen to both be true
   - C) Only fault isolation is real; fast failover is a marketing claim
   - D) AWS uses a different set of AZs for each property

3. What is CloudFront's actual job, and what is it explicitly NOT designed to do?
   - A) It runs your application code at the edge; it does not cache content
   - B) It stores your primary database; it does not handle any caching
   - C) It replaces the need for a Region entirely
   - D) It checks for and serves cached content from nearby edge locations; it does not run application code

4. Which statement correctly describes the relationship between Region/AZ and Edge Locations?
   - A) Edge Locations are nested inside specific Availability Zones
   - B) Region/AZ and Edge Locations are two separate systems that connect to each other, not one nested inside the other
   - C) A Region is just a large collection of Edge Locations
   - D) Edge Locations replace the need for Availability Zones

5. Which statement best captures the relationship between fault tolerance and high availability?
   - A) They are the same thing, just different names for it
   - B) High availability requires no redundancy at all
   - C) Fault tolerance is a mechanism (redundancy with zero noticeable impact); high availability is the outcome that mechanism helps produce
   - D) Fault tolerance only applies to databases, high availability only applies to compute

6. What actually allows a system to handle a sudden 10x traffic spike, like a flash sale?
   - A) Auto Scaling dynamically launches new compute instances in response to demand, rather than relying on pre-provisioned idle capacity
   - B) Availability Zones automatically provide extra idle capacity for this purpose
   - C) CloudFront runs additional compute to absorb the extra load
   - D) Regions automatically merge their capacity during high-traffic events

7. A company deploys instances in three different Availability Zones, but does not use a load balancer - traffic goes directly to one specific instance's address. What happens when that specific instance's AZ goes down?
   - A) Traffic automatically reroutes to an instance in a healthy AZ
   - B) The other AZs automatically take over the exact IP address of the failed instance
   - C) AWS merges the three AZs into one during the outage
   - D) The application becomes unreachable, since nothing was routing traffic across the multiple AZs in the first place

8. A startup deploys its app across three Availability Zones with a load balancer, all within a single Region, and claims they're now protected against "any AWS outage." What's the gap in that claim?
   - A) There is no gap - this setup protects against everything
   - B) The setup only protects against an AZ-level failure; a Region-wide problem would still affect all three AZs, since they're all in the same Region
   - C) Load balancers don't actually work across more than one AZ
   - D) Three AZs is not enough - AWS requires at least five for redundancy

9. A company fixes a broken image on their site, but CloudFront keeps serving the old broken version to some users. Which two things would resolve this?
   - A) Restarting the origin server, or waiting a full day
   - B) Switching to a different Region, or disabling CloudFront entirely
   - C) The cached copy's TTL expiring naturally, or manually triggering an invalidation to force it to refresh immediately
   - D) Nothing can fix this until the next deployment

## Answer Key

1. C - AWS's Availability Zones being redundant doesn't automatically make a specific application redundant - that requires the customer to architect their app to run across multiple AZs (e.g. a load balancer plus instances in more than one AZ). A single-AZ deployment has no automatic failover.
2. A - Fault isolation and fast failover both come from the same "close but not too close" AZ spacing choice, not two separate design decisions.
3. D - CloudFront checks for and serves cached content from nearby edge locations; it does not run application code, unlike a compute service.
4. B - Region/AZ (infrastructure backbone) and Edge Locations (caching layer, run by CloudFront) are two separate systems that connect to each other, not one nested inside the other.
5. C - Fault tolerance is the mechanism (redundancy, zero noticeable impact); high availability is the outcome that mechanism helps produce - they aren't two independent, parallel properties.
6. A - Availability Zones provide redundancy and fault isolation, not elastic capacity. Auto Scaling is the service that actually adds compute capacity on demand.
7. D - Having instances in multiple AZs isn't enough by itself; without a load balancer actively distributing and rerouting traffic, there's nothing detecting the failure or redirecting requests away from it.
8. B - Multi-AZ redundancy only protects against an AZ going down; every AZ is still inside one Region, so a Region-wide problem affects all of them. Protecting against that requires a second Region.
9. C - Cached content refreshes either automatically once its TTL expires, or immediately via a manually triggered invalidation.
