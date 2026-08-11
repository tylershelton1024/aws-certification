---
title: "Chapter 1: AWS Cloud Fundamentals - Practice Questions"
tags: [chapter_01, cloud_fundamentals, practice_questions]
updated: 2026-08-10
---

# Chapter 1: AWS Cloud Fundamentals - Practice Questions

Source: written by the assistant based on your notes and our conversation, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Scoped to the book's core content only - see `deeper_dive_questions.md` for questions on topics that went beyond the book. Questions are grouped under `###` headings matching notes.md's sections. Answers are in the Answer Key at the bottom, so you can try answering first.

## Core Concepts Questions

### What Is Cloud Computing? (the apartment analogy)

7. What does the apartment-versus-house analogy illustrate about AWS?
   - A) Using AWS is like renting an apartment - it can grow with you as needed, without owning the underlying property
   - B) AWS requires you to own physical infrastructure, like owning a house
   - C) AWS is more expensive than owning your own data center in every case
   - D) The analogy has no connection to how AWS actually works

8. Why don't companies using AWS need a huge in-house admin/IT team to manage infrastructure?
   - A) AWS requires companies to hire even more IT staff than on-premises
   - B) AWS handles the underlying infrastructure, so companies can focus their staff elsewhere
   - C) AWS does not allow companies to have any IT staff at all
   - D) IT teams are unrelated to infrastructure management

9. How does AWS's usage-based model affect company costs?
   - A) Companies pay a fixed cost no matter how much they use
   - B) Costs only decrease if a company uses less compute, never more
   - C) Companies pay for what they need, when they need it, letting usage grow or shrink with demand
   - D) AWS requires large upfront hardware purchases before any usage begins

### Key Benefits

1. Which of the following best describes the primary advantage of cloud elasticity?
   - A) You pay a fixed monthly fee no matter how much you use
   - B) You must manually order new hardware anytime you need more capacity
   - C) Resources automatically scale up or down based on demand, and you pay only for what you use
   - D) It removes the need for internet access

2. Under the AWS Shared Responsibility Model, which of the following is the customer always responsible for, regardless of service model?
   - A) Securing their own data and controlling who has access to it
   - B) Physical security of the data center
   - C) Maintaining the underlying network hardware
   - D) Patching the hypervisor

10. Which of the following best summarizes AWS's key benefits as a group?
    - A) They only benefit large enterprises, not small companies
    - B) AWS's benefits are entirely unrelated to each other
    - C) Security is the only meaningful benefit; the others are marketing
    - D) Flexibility, speed, built-in security, reliability, and business impact all reinforce each other

11. What does "Speed" refer to as one of AWS's key benefits?
    - A) Instant access to compute and data, so developers aren't stuck waiting on infrastructure to be provisioned
    - B) The physical speed of AWS's network cables
    - C) A discount tier for companies that pay faster
    - D) Speed only applies to data transfer, never to provisioning

12. What does "Reliability" refer to as one of AWS's key benefits?
    - A) A guarantee that AWS never has any outages
    - B) Improved speed and reliability across regions
    - C) A benefit that only applies to the free tier
    - D) Reliability is unrelated to AWS's regional infrastructure

13. What does "Business impact" refer to as one of AWS's key benefits?
    - A) AWS charging businesses extra fees for growth
    - B) A benefit exclusive to Fortune 500 companies
    - C) Growth, better user satisfaction, and faster innovation, since teams don't have to build everything themselves
    - D) Business impact only refers to marketing spend

### Cloud vs. Traditional Data Centers

14. What does managing a traditional, on-premises data center require that AWS's model avoids?
    - A) Nothing - traditional data centers and AWS require the exact same things
    - B) A traditional data center is always cheaper than AWS
    - C) On-premises data centers require no maintenance at all
    - D) The company handling power, maintenance, and full control themselves, with costs that never really end

15. AWS's model is compared to which everyday analogy in contrast to traditional data centers?
    - A) Renting a ready-to-use office instead of building one from scratch
    - B) Building a custom house from scratch
    - C) Buying a car outright instead of leasing one
    - D) Growing your own food instead of buying groceries

16. Even though AWS owns and secures the underlying infrastructure, who still controls access to a company's own data and applications?
    - A) AWS controls all access, with no customer input
    - B) The company itself still controls access to its own data and applications
    - C) A third-party auditor controls access on behalf of both parties
    - D) Access control is randomly assigned by AWS

### Service Models (the pizza analogy)

3. Which of the following requires a company to buy, build, and maintain its own physical servers?
   - A) IaaS
   - B) PaaS
   - C) SaaS
   - D) A traditional on-premises data center

4. Which AWS service is the classic example of Infrastructure as a Service (IaaS)?
   - A) Amazon EC2
   - B) AWS Elastic Beanstalk
   - C) Gmail
   - D) AWS Cost Explorer

5. A company wants to deploy their application by handing AWS their code, without managing servers, scaling, or load balancing themselves. Which service model are they using?
   - A) IaaS
   - B) SaaS
   - C) On-premises
   - D) PaaS

6. Netflix and Dropbox are commonly used as real-world examples of which AWS service model?
   - A) IaaS
   - B) SaaS
   - C) PaaS
   - D) None of the above

## Answer Key

1. C - Elasticity means scaling to demand and paying only for what's used.
2. A - Under the Shared Responsibility Model, you always secure your own data and access, no matter the service model.
3. D - Only a traditional on-premises data center requires owning physical hardware; all three AWS models remove that.
4. A - Amazon EC2 is the classic IaaS example - virtual servers you configure yourself.
5. D - Handing off code without managing servers/scaling/load balancing is the definition of PaaS.
6. B - Netflix and Dropbox are end-user products you just use - SaaS.
7. A - The apartment analogy illustrates that using AWS is like renting - it can grow with you without owning the underlying property.
8. B - AWS handles the underlying infrastructure, freeing up company staff to focus elsewhere.
9. C - AWS's usage-based model means companies pay for what they need, when they need it.
10. D - AWS's key benefits reinforce each other rather than operating independently.
11. A - Speed refers to instant access to compute and data, without waiting on infrastructure provisioning.
12. B - Reliability refers to improved speed and reliability across AWS's regions.
13. C - Business impact refers to growth, better user satisfaction, and faster innovation from not having to build everything in-house.
14. D - Traditional data centers require the company to handle power, maintenance, and full control themselves, with ongoing costs.
15. A - AWS's model is compared to renting a ready-to-use office instead of building one from scratch.
16. B - The company itself still controls access to its own data and applications, even though AWS secures the underlying infrastructure.
