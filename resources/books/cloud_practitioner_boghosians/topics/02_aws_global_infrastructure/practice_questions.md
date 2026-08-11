---
title: "Chapter 2: AWS Global Infrastructure - Practice Questions"
tags: [chapter_02, global_infrastructure, practice_questions]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Practice Questions

Source: written by the assistant based on your notes, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Scoped to the book's core content only - see `deeper_dive_questions.md` for questions on topics that went beyond the book. Questions are grouped under `###` headings matching notes.md's sections, so they can eventually be filtered by section. Answers are in the Answer Key at the bottom, so you can try answering first.

## Core Concepts Questions

### Regions and Availability Zones

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

9. What is an Availability Zone physically made up of?
   - A) A single, massive data center
   - B) One or more data centers, close enough to work together but far enough apart to avoid a shared local disaster
   - C) A collection of entire Regions
   - D) A single server rack shared by multiple companies

10. In AWS's global infrastructure, what is a Region?
    - A) A single data center dedicated to one customer
    - B) A synonym for Availability Zone
    - C) A broad geographic area where AWS resources can be deployed, fully isolated from every other Region
    - D) A caching layer for static content

11. Why does choosing the right AWS Region matter for data compliance?
    - A) Some data must legally stay within specific geographic areas, and Region selection controls where it physically lives
    - B) AWS Regions have no effect on data compliance requirements
    - C) Data compliance only applies to Availability Zones, not Regions
    - D) Compliance is automatically handled regardless of Region choice

12. What does "fast failover" refer to in the context of Availability Zones?
    - A) AWS taking days to restore a failed AZ
    - B) A customer manually rebuilding their application from scratch after an outage
    - C) Failover that only works between Regions, never between AZs
    - D) The ability to shift workloads to a healthy AZ almost immediately when one AZ has a problem, without losing data

13. How does AWS's Region/AZ design contribute to speed for end users?
    - A) It doesn't - speed is unrelated to Region/AZ placement
    - B) Putting data and resources physically closer to customers reduces the distance data has to travel, making access faster
    - C) Speed only comes from CloudFront, never from Region placement
    - D) AWS artificially throttles speed in regions with fewer customers

### Edge Locations and CloudFront (CDN)

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

14. What does it mean that CloudFront "handles dynamic content"?
    - A) CloudFront can also deliver content that changes per request, like real-time dashboards or personalized recommendations, not just static cached files
    - B) CloudFront only serves static files and cannot handle content that changes per request
    - C) Dynamic content is a synonym for cached content
    - D) Dynamic content can only be served by Local Zones, never by CloudFront

### AWS Local Zones

15. Which of the following is a good use case for an AWS Local Zone?
    - A) Serving static images to reduce page load time
    - B) Storing infrequently accessed backup files
    - C) Real-time gaming or live video production where milliseconds of latency matter
    - D) Long-term data archival

16. When using an AWS Local Zone, who manages the underlying infrastructure?
    - A) The customer takes over full infrastructure management, same as an on-premises data center
    - B) A third-party partner manages Local Zones, not AWS directly
    - C) Local Zones are unmanaged and require the customer to install their own hypervisor
    - D) AWS still fully manages it - same services and experience, just physically closer to a specific set of users

17. What is an AWS Local Zone?
    - A) A backup copy of an entire AWS Region
    - B) A physical extension of a region, placed in another city, to bring AWS infrastructure closer to a specific population of users
    - C) A type of Availability Zone reserved for government customers
    - D) A virtual, non-physical caching layer with no real infrastructure

### AWS Shared Responsibility Model (the rental car analogy)

6. Under the Shared Responsibility Model, who is responsible for patching an EC2 instance's operating system after you launch it?
   - A) The customer
   - B) AWS, as part of infrastructure security
   - C) Neither party - this is automatic
   - D) It depends on the region

18. Under the AWS Shared Responsibility Model, which of these is AWS's responsibility, not the customer's?
    - A) Setting up firewall rules for an application
    - B) Deciding who has access to a company's data
    - C) Physical security of the data center
    - D) Patching an application's own code

19. What does the rental car analogy illustrate about the AWS Shared Responsibility Model?
    - A) AWS and the customer split ownership of the vehicle (infrastructure) equally
    - B) AWS maintains the underlying infrastructure (the car), while the customer controls and is responsible for how they use it (driving) once deployed
    - C) The customer must maintain the physical car themselves before AWS will rent it out
    - D) The analogy shows that AWS has no responsibilities once a resource is deployed

### High Availability and Fault Tolerance

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

20. What is the "net effect" of AWS's fault tolerance and high availability design working together?
    - A) Services become slower but more secure
    - B) Customers must manually restart services after every failure
    - C) Fault tolerance and high availability cancel each other out
    - D) Services stay available even when something goes wrong, reinforced by infrastructure being physically closer to users

21. What does "high availability" mean in AWS's infrastructure design?
    - A) The system keeps running even when something does go down
    - B) The system never requires maintenance
    - C) Availability is only high during business hours
    - D) High availability means data is available to everyone publicly by default

## Answer Key

1. D - A region is made up of multiple Availability Zones.
2. A - Physical separation means a local disaster hitting one AZ doesn't take down the others.
3. C - Edge locations cache content close to users; they don't process/compute anything.
4. B - Amazon CloudFront is AWS's CDN, delivering content through edge locations.
5. D - Local Zones can run compute workloads; edge locations only cache and deliver content.
6. A - Patching the OS on an instance you launched is the customer's responsibility under the Shared Responsibility Model.
7. C - Fault tolerance means redundancy is already built in, so a failure doesn't take the system down.
8. B - AZs within a region are connected through private, always-on networks, enabling near-instant failover.
9. B - An Availability Zone is one or more data centers, close enough together to work as a team but far enough apart to survive a shared local disaster.
10. C - A Region is a broad geographic area where AWS resources can be deployed, fully isolated from every other Region.
11. A - Some data must legally stay within specific geographic areas; Region selection controls where it physically lives.
12. D - Fast failover means shifting workloads to a healthy AZ almost immediately when one has a problem, without losing data.
13. B - Putting data and resources physically closer to customers reduces the distance data has to travel, making access faster.
14. A - CloudFront can deliver content that changes per request (real-time dashboards, personalized recommendations), not just static cached files.
15. C - Local Zones are for latency-sensitive use cases where milliseconds matter, like real-time gaming or live video production.
16. D - AWS still fully manages a Local Zone's infrastructure - it's just physically closer to a specific set of users.
17. B - A Local Zone is a physical extension of a region, placed in another city, to bring AWS infrastructure closer to a specific population of users.
18. C - Physical security of the data center is AWS's responsibility, not the customer's.
19. B - The rental car analogy illustrates that AWS maintains the underlying infrastructure while the customer is responsible for how they use it once deployed.
20. D - The net effect is that services stay available even when something goes wrong, reinforced by infrastructure being physically closer to users.
21. A - High availability means the system keeps running even when something does go down.
