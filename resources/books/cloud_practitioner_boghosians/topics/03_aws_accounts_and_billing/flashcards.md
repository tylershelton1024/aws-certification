---
title: "Chapter 3: AWS Accounts and Billing - Flashcards"
tags: [chapter_03, accounts_and_billing, flashcards]
updated: 2026-08-12
---

# Chapter 3: AWS Accounts and Billing - Flashcards

Source: written by the assistant from notes.md. This is the source of truth for the cards - `flashcards.html` (this chapter) and `../../../../../all_flashcards.html` (whole book) are generated from files like this one and need to be regenerated if cards here change.

## CLI (Command Line Interface)

A text-based way to interact with AWS by typing individual commands. Favored by power users and admins because it saves time and allows automation - the most flexible way to interact with AWS.

## Console

AWS's web-based graphical interface. Simple, doesn't require coding knowledge - the commands are already there for you, just click through.

## SDK (Software Development Kit)

A set of tools for writing code so an application can talk to AWS directly and automatically, without a human running commands. Used to build apps and automated systems that rely on AWS.

## CLI vs. Console vs. SDK

All three are ways to interact with AWS, differing by who's doing the interacting and how much automation is involved. Console: a human clicking through a simple graphical interface, no coding required - best for getting started. CLI: a human (or a script they wrote) typing individual commands - flexible, good for automation a person kicks off. SDK: the application's own code talks to AWS directly while running - no human involved at all, used to build software that manages itself.

## AWS Free Tier

AWS's way of letting you sample services before committing to paying for them - like a grocery store offering free samples. Aimed at startups, learners, developers, and businesses during the experimentation phase.

## AWS Lambda

A serverless compute service that runs code without managing servers. Part of AWS's "always free" tier: 1,000,000 requests per month, no matter how long you've had your account.

## DynamoDB

A NoSQL database service. Part of AWS's "always free" tier: 25 GB of storage included, no matter how long you've had your account.

## Amazon SNS (Simple Notification Service)

A messaging/notification service. Part of AWS's "always free" tier: 1,000,000 publishes per month.

## AWS Glue DataBrew

A visual data preparation tool. Part of AWS's "always free" tier: 40 hours of processing per month.

## EC2 (Elastic Compute Cloud)

AWS's virtual server service. Included in the 12-month free tier: 750 hours/month of t2.micro or t3.micro usage - enough to keep one instance running continuously all month.

## Amazon S3 (Simple Storage Service)

AWS's object storage service. Included in the 12-month free tier: 5 GB of free storage.

## Amazon RDS (Relational Database Service)

AWS's managed relational database service. Included in the 12-month free tier: 750 hours/month of usage.

## Amazon Redshift

AWS's data warehouse service. Offered as a 30-day free trial - not part of the always-free or 12-month free tiers.

## On-Demand Pricing

Pay-as-you-go pricing, billed by the minute, second, or hour - like paying for electricity or water. Best for unpredictable workloads, new projects, and short-term experiments.

## Reserved Pricing

Committing to specific services for 1 or 3 years in exchange for a significant discount, up to 72% - like a gym membership. Good fit for production systems and databases.

## Spot Pricing

Up to 90% off, but AWS can reclaim the resources at any time. Good for flexible, fault-tolerant workloads like image rendering, big data analysis, and testing environments where occasional interruptions are acceptable.

## On-Demand vs. Reserved vs. Spot Pricing

The three pricing models trade commitment for discount. On-Demand: zero commitment, full price, best for unpredictable/new/short-term work. Reserved: commits to 1-3 years for up to 72% off, best for steady long-term workloads like production systems and databases. Spot: bids on unused capacity for up to 90% off, but AWS can reclaim it, so it only fits fault-tolerant, interruptible work.

## Quota

A safe default boundary AWS sets on a new account - e.g. how many EC2 instances or static IPs you can create at first. Protects both the customer (from accidentally overspending) and AWS's infrastructure. Limits are flexible - you can request an increase.

## AWS Organizations

Lets multiple teams run under a single set of connected AWS accounts, with one main account connecting and managing the others.

## Consolidated Billing

A feature of AWS Organizations that combines all linked accounts' charges into a single invoice, like a family's shared budget. Also pools usage across accounts to help reach volume discounts faster.

## AWS Budgets

A tool for setting a cost or usage threshold and getting alerted when you're approaching or exceeding it.

## Cost Explorer

A tool for visualizing historical AWS spending - by service, account, tag, or time period - to see trends and forecast future costs.
