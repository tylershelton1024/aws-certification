---
title: "Chapter 2: AWS Global Infrastructure - Deeper Dive Questions"
tags: [chapter_02, global_infrastructure, deeper_dive, practice_questions]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Deeper Dive Questions

Source: written by the assistant based on `deeper_dive_notes.md` and our conversation - not pulled from an official AWS question bank. Covers topics that went beyond the book's core content - see `practice_questions.md` for questions on the book material itself. Questions are grouped under `###` headings matching deeper_dive_notes.md's sections. Answers are in the Answer Key at the bottom, so you can try answering first.

## Questions

### The "Close But Not Too Close" Tradeoff (Regions/AZs)

2. What determines whether AWS's Availability Zone spacing provides both fault isolation AND fast failover at the same time?
   - A) Both come from the same underlying design choice - far enough apart for isolation, close enough for near-instant failover
   - B) They are two unrelated properties that happen to both be true
   - C) Only fault isolation is real; fast failover is a marketing claim
   - D) AWS uses a different set of AZs for each property

10. According to the AZ spacing tradeoff, what would happen if AWS made Availability Zones too close together?
    - A) A single local disaster could potentially take out multiple AZs at once, undermining fault isolation
    - B) Nothing would change - distance has no effect
    - C) Failover would become slower, not faster
    - D) Data compliance would be easier to achieve

11. What would happen if AWS made Availability Zones too far apart from each other?
    - A) Fault isolation would improve with no downside
    - B) Near-instant failover and physical proximity to customers would become harder to achieve
    - C) AWS would stop connecting them with private networks
    - D) Regions would merge into a single Availability Zone

### CloudFront Is a Router, Not a Compute Service

3. What is CloudFront's actual job, and what is it explicitly NOT designed to do?
   - A) It runs your application code at the edge; it does not cache content
   - B) It stores your primary database; it does not handle any caching
   - C) It replaces the need for a Region entirely
   - D) It checks for and serves cached content from nearby edge locations; it does not run application code

12. If a request cannot be served from a cached copy at a nearby edge location, what does CloudFront do?
    - A) It rejects the request entirely
    - B) It runs the application code itself to generate a response
    - C) It goes back to the origin server to fetch the content
    - D) It permanently disables caching for that content

13. Which of the following is NOT something CloudFront does?
    - A) Checking whether content is cached at a nearby edge location
    - B) Routing requests to the origin server when needed
    - C) Serving cached content faster than going to the origin
    - D) Running an application's backend compute workload

### Region/AZ, Edge Locations, and Local Zones Are Two Separate Systems, Not One Hierarchy

4. Which statement correctly describes the relationship between Region/AZ and Edge Locations?
   - A) Edge Locations are nested inside specific Availability Zones
   - B) Region/AZ and Edge Locations are two separate systems that connect to each other, not one nested inside the other
   - C) A Region is just a large collection of Edge Locations
   - D) Edge Locations replace the need for Availability Zones

14. Are Edge Locations organized as a subset of Availability Zones?
    - A) No, Edge Locations are a separate, much larger network layered on top, unrelated to AZ boundaries
    - B) Yes, every edge location belongs to exactly one AZ
    - C) Yes, but only in certain Regions
    - D) Edge Locations replace the need for AZs entirely

15. In the worked video streaming example, where does the source video and backend logic actually live?
    - A) Spread across edge locations worldwide
    - B) In a region, spread across its Availability Zones, for durability and redundancy
    - C) In a Local Zone closest to the largest customer base
    - D) Nowhere specific - CloudFront generates it on demand

### Fault Tolerance Is the Mechanism, High Availability Is the Outcome

5. Which statement best captures the relationship between fault tolerance and high availability?
   - A) They are the same thing, just different names for it
   - B) High availability requires no redundancy at all
   - C) Fault tolerance is a mechanism (redundancy with zero noticeable impact); high availability is the outcome that mechanism helps produce
   - D) Fault tolerance only applies to databases, high availability only applies to compute

16. If a system has fault tolerance but poor overall high availability, what does that suggest?
    - A) This combination is impossible - they always match exactly
    - B) Fault tolerance and high availability are unrelated concepts
    - C) The redundancy mechanism might not be covering every failure scenario that actually threatens uptime
    - D) The system is more available than a system with both properties

17. Which best describes how fault tolerance and high availability relate as concepts?
    - A) They are competing goals - improving one always worsens the other
    - B) High availability is required before fault tolerance can exist
    - C) They only apply to database services, never to compute
    - D) Fault tolerance is a specific mechanism; high availability is the broader outcome that mechanism helps produce

### Multi-AZ Redundancy Is a Customer Decision, Not Automatic

1. A company deploys their application on a single EC2 instance in one Availability Zone. That Availability Zone experiences an outage. What happens to the application?
   - A) AWS automatically fails it over to another Availability Zone with no interruption
   - B) AWS automatically relaunches the instance in the same Availability Zone within seconds
   - C) The application goes offline, since it was never deployed to more than one Availability Zone
   - D) The application's data is lost permanently

18. Why doesn't having other healthy Availability Zones in a region automatically help an application that was only deployed to one AZ?
    - A) Because nothing was ever deployed to those other AZs, so there's nothing there to fail over to
    - B) Because AWS charges extra to enable failover
    - C) Because different AZs run incompatible versions of EC2
    - D) Because failover only works within a single AZ, never across AZs

19. Which part of the Shared Responsibility Model does "architecting an application to use multi-AZ redundancy" fall under?
    - A) It isn't part of the Shared Responsibility Model at all
    - B) The customer's responsibility - reliability in the cloud, the same bucket as permissions and patching
    - C) AWS's responsibility, since AZs are AWS infrastructure
    - D) A shared 50/50 responsibility between AWS and the customer

### Auto Scaling (What Actually Handles Traffic Spikes)

6. What actually allows a system to handle a sudden 10x traffic spike, like a flash sale?
   - A) Auto Scaling dynamically launches new compute instances in response to demand, rather than relying on pre-provisioned idle capacity
   - B) Availability Zones automatically provide extra idle capacity for this purpose
   - C) CloudFront runs additional compute to absorb the extra load
   - D) Regions automatically merge their capacity during high-traffic events

20. What happens to Auto Scaling-managed instances when traffic demand drops back down?
    - A) They keep running indefinitely regardless of demand
    - B) AWS charges a penalty fee for reduced usage
    - C) Auto Scaling terminates the extra instances that are no longer needed
    - D) The instances are permanently reserved for the next spike

21. What is Auto Scaling commonly paired with to distribute traffic across the instances it creates?
    - A) A Network ACL
    - B) An Internet Gateway
    - C) A Local Zone
    - D) A load balancer

### Elastic Load Balancing (The Missing Piece for Multi-AZ Redundancy)

7. A company deploys instances in three different Availability Zones, but does not use a load balancer - traffic goes directly to one specific instance's address. What happens when that specific instance's AZ goes down?
   - A) Traffic automatically reroutes to an instance in a healthy AZ
   - B) The other AZs automatically take over the exact IP address of the failed instance
   - C) AWS merges the three AZs into one during the outage
   - D) The application becomes unreachable, since nothing was routing traffic across the multiple AZs in the first place

22. What does an Elastic Load Balancer continuously check in order to know where to route traffic?
    - A) The health of each instance behind it
    - B) The current stock price of AWS
    - C) The customer's billing history
    - D) The CIDR block size of the VPC

23. Why is having instances in multiple AZs, by itself, not enough for real redundancy?
    - A) It actually is enough by itself - nothing else is needed
    - B) Without a load balancer to detect failures and redirect traffic, nothing automatically reroutes requests away from a failed instance
    - C) Multiple AZs increase cost without any benefit
    - D) AWS requires at least five AZs before redundancy takes effect

### Multi-AZ Redundancy Does Not Protect Against a Region-Wide Outage

8. A startup deploys its app across three Availability Zones with a load balancer, all within a single Region, and claims they're now protected against "any AWS outage." What's the gap in that claim?
   - A) There is no gap - this setup protects against everything
   - B) The setup only protects against an AZ-level failure; a Region-wide problem would still affect all three AZs, since they're all in the same Region
   - C) Load balancers don't actually work across more than one AZ
   - D) Three AZs is not enough - AWS requires at least five for redundancy

24. What is required to protect against a full Region-wide outage, beyond multi-AZ redundancy?
    - A) Nothing more is needed - multi-AZ already covers this
    - B) Adding more Availability Zones within the same Region
    - C) Deploying into a second Region as well
    - D) Switching from EC2 to Local Zones

25. Why does redundancy built using multiple AZs within one Region fail to protect against a Region-wide problem?
    - A) Because AZs within a Region are not actually connected to each other
    - B) Because multi-AZ redundancy is only a marketing term with no real effect
    - C) Because Regions share physical infrastructure with each other
    - D) Because every one of those AZs is still inside the same Region, and Regions are isolated from each other

### Cache Refresh: TTL Expiration vs. Invalidation

9. A company fixes a broken image on their site, but CloudFront keeps serving the old broken version to some users. Which two things would resolve this?
   - A) Restarting the origin server, or waiting a full day
   - B) Switching to a different Region, or disabling CloudFront entirely
   - C) The cached copy's TTL expiring naturally, or manually triggering an invalidation to force it to refresh immediately
   - D) Nothing can fix this until the next deployment

26. What happens automatically once a cached object's TTL expires?
    - A) The next request for that object causes a fresh fetch from the origin
    - B) The object is permanently deleted with no way to recover it
    - C) The entire edge location shuts down
    - D) Nothing - TTL expiration has no effect on caching behavior

27. When would you want to use an invalidation instead of just waiting for a TTL to expire?
    - A) Never - invalidations are always worse than waiting
    - B) When you can't wait - e.g. a broken image was just fixed and shouldn't keep serving the old cached version
    - C) Invalidations are required before any content can be cached at all
    - D) Only when switching to a different AWS Region

### CDN Security Features: Geoblocking, SSL, and DDoS Protection

28. When CloudFront serves a cached response for a viewer's HTTPS request, how many separate encrypted connections are actually involved?
    - A) Two separate encrypted hops - viewer-to-edge, and (only on a cache miss) edge-to-origin
    - B) Just one continuous encrypted tunnel from viewer all the way to the origin
    - C) None - CloudFront never encrypts anything itself
    - D) Three: viewer-to-edge, edge-to-edge, and edge-to-origin

29. Why does the viewer-to-edge connection specifically need encryption on every single request, regardless of cache hit or miss?
    - A) It doesn't - only the edge-to-origin connection matters
    - B) That connection happens on every request and travels over whatever network the viewer is on, the most exposed stretch of the journey
    - C) The viewer-to-edge connection is only made once per day
    - D) Viewer connections are automatically safe regardless of encryption

30. Why does CloudFront's distributed edge network help absorb a DDoS attack?
    - A) It doesn't - DDoS attacks always succeed regardless of CDN use
    - B) CloudFront blocks all traffic during any attack, including legitimate users
    - C) Malicious traffic gets spread across hundreds of edge locations instead of overwhelming one single origin server
    - D) DDoS protection requires a separate paid product with no free tier

31. What does CloudFront's geoblocking feature actually check to decide whether to allow or block a request?
    - A) The user's actual physical GPS location
    - B) The user's passport information
    - C) The device's operating system
    - D) The apparent source IP address and what country it's registered to

32. Why can a VPN or proxy circumvent geoblocking?
    - A) Geoblocking only checks the apparent source IP, and a VPN makes the request genuinely appear to originate from a different country
    - B) VPNs are specifically whitelisted by AWS
    - C) Geoblocking does not actually exist as a real CloudFront feature
    - D) VPNs disable CloudFront entirely

33. Who is responsible for making sure the edge-to-origin connection is actually encrypted?
    - A) AWS automatically encrypts it with no configuration needed, in all cases
    - B) The customer must configure CloudFront's origin protocol policy and install a valid certificate on their origin - AWS provides the capability, not automatic enforcement
    - C) Encryption is never possible on the edge-to-origin leg
    - D) It is impossible to configure this incorrectly

34. What is AWS Shield?
    - A) A paid-only firewall product with no free tier
    - B) A physical security team stationed at AWS data centers
    - C) A service automatically included at no extra cost with CloudFront, providing DDoS protection
    - D) A tool for encrypting data at rest in S3

### EC2 Overview (Compute Services Preview)

35. What is the relationship between an AMI and an EC2 instance?
    - A) An AMI is the template (OS + software) an instance boots from
    - B) An AMI is a type of EBS volume
    - C) An AMI is a pricing model for EC2
    - D) An AMI only exists after an instance is already running

36. What does the family letter in an instance type name (e.g. the "t" in t3.micro) indicate?
    - A) The AWS Region the instance runs in
    - B) What the instance type is optimized for (general purpose, compute, memory, etc.)
    - C) The pricing model being used
    - D) Whether the instance uses EBS or instance store

37. Which EC2 pricing model would be most appropriate for a workload that must run continuously for 3 years and never be interrupted?
    - A) Spot Instances
    - B) On-Demand only
    - C) Reserved Instances
    - D) None of the pricing models support long-term workloads

38. What is an AMI (Amazon Machine Image)?
    - A) A pricing discount for long-term EC2 usage
    - B) A virtual hard drive attached to an instance
    - C) A type of Availability Zone
    - D) The template an instance boots from - an OS plus pre-installed software

39. What does an EC2 instance type actually define?
    - A) The instance's hardware - CPU, memory, and network performance
    - B) The Region the instance is deployed in
    - C) Whether the instance uses HTTP or HTTPS
    - D) The instance's billing currency

40. What happens to an EBS volume's data when the EC2 instance it's attached to is terminated?
    - A) It is always immediately and permanently deleted with no exceptions
    - B) It can persist independently of the instance, unlike temporary instance store storage
    - C) It automatically transfers to a different customer's account
    - D) EBS volumes cannot be attached to EC2 instances at all

41. What defines the On-Demand EC2 pricing model?
    - A) A mandatory 3-year commitment
    - B) Bidding on unused spare capacity
    - C) Paying per hour or second, with no commitment
    - D) A one-time upfront payment covering the instance forever

42. What is the tradeoff with Reserved Instances?
    - A) They cost more than On-Demand with no benefit
    - B) They can be reclaimed by AWS with little notice
    - C) They only work with Spot pricing
    - D) You commit to 1-3 years of usage in exchange for a steep discount

43. What is the major risk of using Spot Instances?
    - A) AWS can reclaim that capacity with little notice, since you're bidding on unused spare capacity
    - B) They are always more expensive than On-Demand
    - C) They cannot be used for any workload type
    - D) They require a 5-year minimum commitment

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
10. A - Making AZs too close together risks a single local disaster taking out more than one AZ at once, undermining the fault isolation the spacing is meant to provide.
11. B - Making AZs too far apart would make near-instant failover and physical proximity to customers harder to achieve - that's the other half of the tradeoff.
12. C - On a cache miss, CloudFront fetches the content from the origin server, serves it, and caches it for next time.
13. D - CloudFront checks, routes, and serves cached content, but never runs an application's backend compute workload - that's not its job.
14. A - Edge Locations are a separate, much larger network layered on top of the Region/AZ system, not organized by or nested inside any AZ.
15. B - The source video and backend logic live in a region, spread across its Availability Zones, for durability and redundancy.
16. C - Fault tolerance in one area doesn't guarantee high availability overall if the redundancy mechanism doesn't cover every failure scenario that actually threatens uptime.
17. D - Fault tolerance is a specific mechanism; high availability is the broader outcome that mechanism helps produce.
18. A - Nothing was ever deployed to the other AZs, so there's nothing there for traffic to fail over to, no matter how healthy those AZs are.
19. B - Architecting an application to use multi-AZ redundancy is the customer's responsibility - reliability in the cloud, the same bucket as permissions and patching.
20. C - Auto Scaling terminates the extra instances that are no longer needed once demand drops, avoiding paying for idle capacity.
21. D - Auto Scaling is commonly paired with a load balancer, which distributes traffic across whichever instances currently exist.
22. A - An Elastic Load Balancer continuously checks the health of each instance behind it, to know where it's safe to route traffic.
23. B - Without a load balancer to detect failures and redirect traffic, nothing automatically reroutes requests away from a failed instance, even if other AZs have healthy instances.
24. C - Protecting against a full Region-wide outage requires deploying into a second Region as well, not just adding more AZs within the same Region.
25. D - Every AZ used is still inside the same Region, and Regions are isolated from each other, so a Region-wide problem affects all of them equally.
26. A - Once a cached object's TTL expires, the next request for it automatically triggers a fresh fetch from the origin.
27. B - Use an invalidation when you can't wait for the TTL to expire naturally - e.g. a broken image was just fixed and shouldn't keep serving the old cached version.
28. A - There are two separate encrypted hops - viewer-to-edge always, and edge-to-origin only on a cache miss - not one continuous tunnel.
29. B - The viewer-to-edge connection happens on every request and travels over whatever network the viewer is on, making it the most exposed stretch of the journey.
30. C - Malicious traffic gets spread across hundreds of edge locations instead of overwhelming one single origin server.
31. D - Geoblocking checks the apparent source IP address and what country it's registered to.
32. A - Geoblocking only checks the apparent source IP; a VPN makes the request genuinely appear to originate from a different country, which CloudFront cannot see through.
33. B - The customer must configure CloudFront's origin protocol policy and install a valid certificate on their origin - AWS provides the capability, not automatic enforcement.
34. C - AWS Shield is automatically included at no extra cost with CloudFront, providing DDoS protection.
35. A - An AMI is the template - an OS plus pre-installed software - that an instance boots from.
36. B - The family letter indicates what the instance type is optimized for (general purpose, compute, memory, etc.).
37. C - Reserved Instances are the right fit for a long-term, continuous, non-interruptible workload.
38. D - An AMI is the template an instance boots from - an OS plus pre-installed software.
39. A - An EC2 instance type defines the instance's hardware: CPU, memory, and network performance.
40. B - An EBS volume can persist independently of the instance's own lifecycle, unlike temporary instance store storage.
41. C - On-Demand means paying per hour or second, with no commitment.
42. D - Reserved Instances require committing to 1-3 years of usage in exchange for a steep discount.
43. A - AWS can reclaim Spot Instance capacity with little notice, since you're bidding on unused spare capacity.
