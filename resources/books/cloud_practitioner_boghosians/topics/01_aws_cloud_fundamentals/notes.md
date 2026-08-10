---
title: "Chapter 1: AWS Cloud Fundamentals - Notes"
tags: [chapter_01, cloud_fundamentals, notes]
updated: 2026-08-09
---

# Chapter 1: AWS Cloud Fundamentals - Notes

## What Is Cloud Computing? (the apartment analogy)

AWS is like renting an apartment instead of owning a house - it can grow with you as needed. Companies no longer need to own physical servers and hardware; they outsource that to AWS.

AWS can grow or shrink based on usage - you pay for what you need, when you need it. This also means companies don't need a huge in-house admin/IT team to manage infrastructure.

## Key Benefits

- **Flexibility** - AWS scales to demand, and servers stay available no matter the load.
- **Speed** - instant access to compute and data. Developers can focus on their actual jobs instead of waiting on infrastructure to be provisioned.
- **Security** - built into the foundation, including:
  - Encryption
  - Identity management
  - Compliance tools
  - Note: AWS still follows a Shared Responsibility Model - AWS secures the underlying cloud infrastructure, but you're still responsible for securing what you put in it and who has access.
- **Reliability** - improved speed and reliability across regions.
- **Business impact** - growth, better user satisfaction, and faster innovation, since teams don't have to build everything themselves.

## Cloud vs. Traditional Data Centers

Traditional data centers require the company to handle everything themselves:

- Power
- Maintenance
- Full control, but costly - maintenance costs never really end.

AWS's model is different:

- Designed to be simple - no onsite staff required.
- Like renting a ready-to-use office instead of building one from scratch - the infrastructure already exists.
- You still control access to your own data and applications, even though AWS owns and secures the underlying infrastructure.

## Service Models (the pizza analogy)

Three main cloud service models, from most to least hands-on:

### Infrastructure as a Service (IaaS) - "making a pizza from scratch"

- You buy the dough, sauce, and cheese, set up the kitchen, and manage the timing yourself.
- Full control, but you take on all the work.
- Example: Amazon EC2 (Elastic Compute Cloud) - virtual servers you configure from the ground up.
- Best for maximum flexibility.

### Platform as a Service (PaaS) - "pizza delivered, you just bake it"

- Ingredients are already measured and assembled - you skip the messy setup.
- Example: AWS Elastic Beanstalk.
- Developers write code and hand it to AWS; AWS handles scaling and load balancing.
- Best for focusing on the application instead of the infrastructure underneath it.

### Software as a Service (SaaS) - "pizza arrives hot and ready to eat"

- Everything is managed for you - log in and use the service immediately.
- Examples: Netflix, Dropbox, Gmail - you use the product without knowing how it was built.
- AWS's own account-management tools (like the Billing Dashboard and Cost Explorer) work this way too.

### Summary

- IaaS - total control
- PaaS - focus on the application
- SaaS - everything handled for you

Businesses mix and match these models depending on the project and how much control the team wants.

See `deeper_dive_notes.md` for topics that came from questions asked beyond what this chapter covers directly.

See `../../../../../hands_on/00_account_setup/` and `../../../../../hands_on/01_CCP_app/` for real, deployed AWS work tied to this chapter.
