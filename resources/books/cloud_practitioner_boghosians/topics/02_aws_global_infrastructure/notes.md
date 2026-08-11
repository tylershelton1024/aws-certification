---
title: "Chapter 2: AWS Global Infrastructure - Notes"
tags: [chapter_02, global_infrastructure, notes]
updated: 2026-08-10
---

# Chapter 2: AWS Global Infrastructure - Notes

## Regions and Availability Zones (the fast-food chain analogy)

Think of AWS as a large fast-food chain. Its global infrastructure works the same way a chain manages locations across the world.

- **Region** - a broad geographic area, like a market the chain operates in. Customers (you, when building on AWS) pick which region their resources live in. Each region is fully isolated from every other region.
- **Availability Zone (AZ)** - like one franchise location within that region, complete with its own backup kitchens. Each AZ acts as its own independent "restaurant" - it can go down without stopping the others.
- Hierarchy: **Region -> Availability Zone**. A region is made up of multiple AZs.
- An AZ itself is a group of data centers, close enough together to work as a team, but far enough apart to avoid being taken out by the same local disaster.

Why this design matters:
- **Data compliance** - some data has to stay within specific geographic areas. Picking the right region helps meet that requirement.
- **Fast failover** - if one AZ has a problem, workloads can shift to another AZ almost immediately, without losing data.
- **Speed** - putting data physically closer to customers makes it literally faster to reach them. This is also part of what keeps services fast and resilient.

## Edge Locations and CloudFront (CDN)

AWS caches content instead of sending every request across the internet. **Edge locations** are small data centers that hold cached videos, content, and images, closer to end users.

- **Amazon CloudFront** is AWS's CDN (Content Delivery Network) - it manages delivery through these edge locations.
- CloudFront checks whether requested data is already cached at a nearby edge location. If so, it serves it from there instead of the origin server, so videos and webpages load faster.
- This is why globally-distributed businesses can offer fast speeds worldwide - their content is cached close to users everywhere, not served from one central location.
- CloudFront also handles **dynamic content** (e.g. real-time dashboards, personalized recommendations), not just static cached files.
- Edge locations themselves cannot process/compute anything - they only cache and deliver content. (Contrast with Local Zones, below, which can.)

## AWS Local Zones

A **Local Zone** is a physical extension of a region, placed in another city closer to a specific population of users - AWS infrastructure without needing a full second region.

- Still fully managed by AWS - same services, same experience, just physically closer to a particular set of users.
- You choose what runs in the Local Zone vs. the main region, to optimize for your customers' experience.
- Useful for latency-sensitive use cases where milliseconds matter: real-time gaming, live video production, virtual desktops, media production.
- Not literally "a data center" in the traditional sense, but functions similarly - it brings the cloud physically closer to users.

## AWS Shared Responsibility Model (the rental car analogy)

- **AWS is the rental car company.** They maintain the car (the infrastructure) and make sure it's in good working order before you drive off.
- **You are the driver.** Once you're behind the wheel, you decide the speed, the destination, how you drive - that's on you.

**AWS's responsibilities:**
- Physical infrastructure security
- Network hardware
- Power
- Cooling
- Making sure core services (e.g. EC2, S3) are secure and reliable at the infrastructure level

**Your (the customer's) responsibilities:**
- Setting up permissions
- Establishing firewalls
- Security *in* the cloud (as opposed to security *of* the cloud, which is AWS's job)
- Deciding who gets access to what
- Updating and patching the applications you set up
- If you spin up an EC2 instance, it's your job to lock it down and keep it up to date

Most security issues happen when AWS customers don't hold up their end of this model - not because AWS's side failed.

## High Availability and Fault Tolerance

- **Fault tolerance** - redundancy. AWS's systems are designed so a backup is already in place before something breaks.
- **High availability** - the system keeps running even when something does go down.
- AWS spreads infrastructure across multiple Availability Zones, connected through private networks that stay up. If one AZ goes down, another is already up and ready - traffic and data hand off instantly.
- Problem detection is built into AWS's systems, not bolted on as an add-on.
- Net effect: services stay available even when something goes wrong, and bringing the cloud physically closer to users (edge locations, Local Zones) reinforces that speed and resilience.

## Topics Flagged for a Deeper Dive Later

Concepts from this chapter worth coming back to, either because they need more depth or weren't fully explained by the book:

- Edge locations, in more depth
- Why data must be kept in certain regions (data residency/compliance specifics)
- CDN details: geoblocking, SSL encryption, DDoS protection (mentioned as things a CDN helps secure, not yet explained individually)
- What exactly counts as "dynamic content"
- How a Local Zone actually differs from an edge location, mechanically
- EC2 - flagged for a real deeper dive
- S3

See `deeper_dive_notes.md` for topics that came from questions asked beyond what this chapter covers directly.

See `../../../../../hands_on/00_account_setup/` and `../../../../../hands_on/01_CCP_app/` for real, deployed AWS work tied to this chapter.
