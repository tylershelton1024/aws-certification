---
title: "Chapter 3: AWS Accounts and Billing - Notes"
tags: [chapter_03, accounts_and_billing, notes]
updated: 2026-08-09
---

# Chapter 3: AWS Accounts and Billing - Notes

Managing your AWS account is like running a household - you have to pay attention and use the right tools to stay alert. When you know what's going on, you can avoid getting caught off guard by unexpected costs.

## Creating an AWS Account (the bank account analogy)

Creating an AWS account is like opening a bank account for your household - the foundational setup step before anything else. AWS needs an email address to create the account.

## Ways to Interact with AWS (the smart home analogy)

AWS is like having a smart home - there are multiple ways to control it depending on how hands-on you want to be. The customer gets to choose how they interact with the cloud.

- **CLI** (Command Line Interface) - power users and admins love this because it saves time and allows for automation. This is the most flexible option.
- **Console** - like a touchscreen panel on your wall. Simple, doesn't require coding knowledge - like using the CLI, but the commands are already there for you.
- **SDK** (Software Development Kit) - like programming a smart home to run on its own. Writing code so things happen automatically. This can be used for building smart, responsive systems - and apps - that rely on AWS for functionality.

## AWS Free Tier (the grocery store sample analogy)

The **AWS Free Tier** gives you the opportunity to explore - sample before you buy. Like a grocery store where staff offer free samples, the AWS Free Tier is meant to help startups, learners, developers, and businesses during the experimentation phase.

**Always free** - some services are always free, no matter how long you've had your account:
- **AWS Lambda** - 1,000,000 requests/month
- **DynamoDB** - 25 GB of storage
- **Amazon SNS** - 1,000,000 publishes
- **AWS Glue DataBrew** - 40 hours of processing/month

**12-month free tier** - starts when you create your AWS account:
- **EC2** - 750 hours/month of t2.micro or t3.micro instance usage, enough to keep one instance running all month long
- **Amazon S3** - 5 GB of free storage
- **Amazon RDS** - 750 hours/month of usage
- Full access to premium features during the first year, so you can try things out while you build

**Free trials:**
- **Amazon Redshift** - 30-day free trial
- Special coupons available for some full products

If you exceed free tier limits, you'll be billed at standard rates.

## Pricing Models

AWS lets you work with no financial risk up front. As your projects grow, it's important to understand the different pricing models available - you can mix and match different models within the same account. Broadly, there are two categories: prepaid and pay-as-you-go.

### On-Demand Pricing (the utility bill analogy)

**On-Demand pricing** (pay-as-you-go) is like paying for electricity or water - AWS monitors usage by the minute, second, or hour. Ideal for:
- Unpredictable workloads
- New projects
- Short-term experiments

### Reserved Pricing (the gym membership analogy)

**Reserved pricing** is like committing to a gym membership - you commit to specific services for 1 or 3 years in exchange for a significant discount, up to 72%. Good fit for:
- Production systems
- Databases

### Spot Pricing

**Spot pricing** offers up to 90% off, but the resources can be taken back (reclaimed) by AWS at any time. Good for fault-tolerant workloads where interruption is acceptable:
- Flexible, fault-tolerant workloads
- Image rendering
- Big data analysis
- Testing environments where occasional interruptions are acceptable
- Work with flexible deadlines

## AWS Service Limits and Quotas

A **quota** is a safe default boundary set on a new account - for example, a limit on how many EC2 instances you can run at first, or how many static IPs you can create.

- Protects you from doing something costly by accident.
- Protects AWS's own infrastructure as well.
- Helps new users avoid spending a lot of money unintentionally.
- Limits are flexible - you can request more, and AWS can raise your limits.
- You can look up your quotas ahead of time, before you need them.
- Understanding service limits is about readiness, not restriction.

## AWS Organizations and Consolidated Billing (the shared family budget analogy)

**AWS Organizations** lets multiple teams run under a single set of accounts - one main account that connects and manages other accounts.

- **Consolidated billing** acts like a family's shared budget - AWS combines all charges across the organization into a single invoice.
- Discounts are calculated from combined usage across the whole organization, so even small departments can benefit.
- Visibility and control is another advantage - it maintains a central view of services, helping maintain security and compliance across the organization.
- **AWS Budgets** and **Cost Explorer** are tools for managing and tracking this.
- The overall goal: balance independence (teams operate their own accounts) with central control (billing and oversight stay unified).

## Topics Flagged for a Deeper Dive Later

Concepts from this chapter worth coming back to, either because they need more depth or weren't fully explained by the book:

- CLI vs. Console vs. SDK - concrete examples of when you'd actually reach for each one
- What actually happens when you exceed a Free Tier limit (grace period, or billed immediately?)
- How Spot pricing "reclaiming" actually works mechanically, and how an interruption is handled
- How to actually check your current quotas and request a quota increase
- How Consolidated Billing's discount calculation actually works mechanically
- What AWS Budgets and Cost Explorer actually do, day to day - not yet covered

See `deeper_dive_notes.md` for topics that came from questions asked beyond what this chapter covers directly.

