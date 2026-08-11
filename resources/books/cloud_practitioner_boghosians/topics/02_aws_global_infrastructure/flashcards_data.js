// Chapter 2: AWS Global Infrastructure - flashcard data.
// This is the single source of truth for this chapter's card content as far
// as the HTML viewers are concerned - flashcards.html (this chapter) and
// all_flashcards.html (whole book) both load this same file via <script
// src="...">, so there is only one place to update, not several.
//
// This file itself is generated from flashcards.md and
// deeper_dive_flashcards.md - if those change, regenerate this file to match.
const chapter02Decks = {
  "core": [
    { "term": "Region", "definition": "A broad geographic area where AWS resources can live. Fully isolated from every other region. Customers choose which region their resources run in." },
    { "term": "Availability Zone (AZ)", "definition": "One or more data centers within a region, isolated enough to survive a local disaster on its own, but close enough to other AZs in the same region to work together effectively. A region is made up of multiple AZs." },
    { "term": "Edge Location", "definition": "A small AWS data center that caches content (video, images, other data) close to end users, so requests don't have to travel all the way to the origin server. Cannot process/compute anything - caching and delivery only." },
    { "term": "Amazon CloudFront", "definition": "AWS's CDN (Content Delivery Network). Delivers content through edge locations, checking whether requested data is already cached nearby before going back to the origin. Also handles dynamic content (e.g. real-time dashboards, personalized recommendations), not just static files." },
    { "term": "AWS Local Zone", "definition": "A physical extension of a region, placed in another city to bring AWS infrastructure closer to a specific population of users. Still fully managed by AWS. Used for latency-sensitive workloads (real-time gaming, live production, virtual desktops) where milliseconds matter. Unlike an edge location, a Local Zone can actually process/compute workloads." },
    { "term": "Shared Responsibility Model (Region/AZ context)", "definition": "AWS secures the physical infrastructure, network hardware, power, and cooling, and keeps core services like EC2 and S3 reliable. The customer is responsible for permissions, firewalls, security in the cloud, and patching whatever they deploy (e.g. an EC2 instance they spin up). Most security incidents come from the customer's side of this line, not AWS's." },
    { "term": "Fault Tolerance", "definition": "Redundancy - a backup is already in place before something breaks, so a failure doesn't take the system down." },
    { "term": "High Availability", "definition": "The property of a system continuing to run even when part of it goes down - enabled by spreading infrastructure across multiple Availability Zones connected by private networks, so traffic can fail over almost instantly." }
  ],
  "deeper": []
};
