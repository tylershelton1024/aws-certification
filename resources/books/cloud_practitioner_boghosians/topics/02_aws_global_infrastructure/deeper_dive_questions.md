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
   - B) The application goes offline, since it was never deployed to more than one Availability Zone
   - C) AWS automatically relaunches the instance in the same Availability Zone within seconds
   - D) The application's data is lost permanently

2. What determines whether AWS's Availability Zone spacing provides both fault isolation AND fast failover at the same time?
   - A) They are two unrelated properties that happen to both be true
   - B) Both come from the same underlying design choice - far enough apart for isolation, close enough for near-instant failover
   - C) Only fault isolation is real; fast failover is a marketing claim
   - D) AWS uses a different set of AZs for each property

3. What is CloudFront's actual job, and what is it explicitly NOT designed to do?
   - A) It runs your application code at the edge; it does not cache content
   - B) It checks for and serves cached content from nearby edge locations; it does not run application code
   - C) It stores your primary database; it does not handle any caching
   - D) It replaces the need for a Region entirely

4. Which statement correctly describes the relationship between Region/AZ and Edge Locations?
   - A) Edge Locations are nested inside specific Availability Zones
   - B) Region/AZ and Edge Locations are two separate systems that connect to each other, not one nested inside the other
   - C) A Region is just a large collection of Edge Locations
   - D) Edge Locations replace the need for Availability Zones

5. Which statement best captures the relationship between fault tolerance and high availability?
   - A) They are the same thing, just different names for it
   - B) Fault tolerance is a mechanism (redundancy with zero noticeable impact); high availability is the outcome that mechanism helps produce
   - C) High availability requires no redundancy at all
   - D) Fault tolerance only applies to databases, high availability only applies to compute

## Answer Key

1. B - AWS's Availability Zones being redundant doesn't automatically make a specific application redundant - that requires the customer to architect their app to run across multiple AZs (e.g. a load balancer plus instances in more than one AZ). A single-AZ deployment has no automatic failover.
2. B - Fault isolation and fast failover both come from the same "close but not too close" AZ spacing choice, not two separate design decisions.
3. B - CloudFront checks for and serves cached content from nearby edge locations; it does not run application code, unlike a compute service.
4. B - Region/AZ (infrastructure backbone) and Edge Locations (caching layer, run by CloudFront) are two separate systems that connect to each other, not one nested inside the other.
5. B - Fault tolerance is the mechanism (redundancy, zero noticeable impact); high availability is the outcome that mechanism helps produce - they aren't two independent, parallel properties.
