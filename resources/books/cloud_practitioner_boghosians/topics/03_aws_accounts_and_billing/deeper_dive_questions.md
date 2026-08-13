---
title: "Chapter 3: AWS Accounts and Billing - Deeper Dive Questions"
tags: [chapter_03, accounts_and_billing, deeper_dive, practice_questions]
updated: 2026-08-12
---

# Chapter 3: AWS Accounts and Billing - Deeper Dive Questions

Source: written by the assistant based on `deeper_dive_notes.md` and our conversation - not pulled from an official AWS question bank. Covers topics that went beyond the book's core content - see `practice_questions.md` for questions on the book material itself. Questions are grouped under `###` headings matching deeper_dive_notes.md's sections. Answers are in the Answer Key at the bottom, so you can try answering first.

## Questions

### CLI vs. SDK: Who's Doing the Talking

1. What is the core distinguishing factor between the CLI and the SDK?
   - A) Who is doing the talking to AWS - a human (or their script) for CLI, versus the application's own code for SDK
   - B) The CLI is free while the SDK requires a paid subscription
   - C) The SDK can only be used with Amazon S3
   - D) The CLI only works within the AWS Console

2. In the photo-upload example, why does the app use the SDK rather than the CLI to store each upload in S3?
   - A) Because the CLI cannot interact with S3 at all
   - B) Because the app's own code needs to make that call automatically, live, with no human running a command per upload
   - C) Because SDK calls are always cheaper than CLI calls
   - D) Because the CLI requires a Reserved pricing commitment

3. If a tool's own code reaches into a database to connect two applications together, without any human running commands, which interaction method is that an example of?
   - A) Console
   - B) CLI
   - C) SDK
   - D) AWS Organizations

4. What do the CLI and SDK have in common that makes them easy to blur together?
   - A) Both require a Reserved pricing commitment
   - B) Both are only usable by AWS support staff
   - C) Both are limited to read-only operations
   - D) Both let you automate interactions with AWS

### Exceeding a Free Tier Limit: No Grace Period

5. What happens the moment your AWS usage crosses a Free Tier limit?
   - A) AWS starts billing the overage at standard rates automatically, with no grace period
   - B) Your account is immediately suspended until you upgrade
   - C) AWS deletes the resources that caused the overage
   - D) Nothing happens until you manually acknowledge the overage

6. How would you find out you were about to exceed a Free Tier limit before it actually happens?
   - A) AWS automatically emails you a warning the day before
   - B) By proactively setting up a budget alert via AWS Budgets
   - C) By checking the Service Quotas console
   - D) There is no way to find out in advance

7. Does AWS wait until the end of the month to bill you for exceeding a Free Tier limit?
   - A) Yes, overages are only billed once a year
   - B) Yes, but only for EC2 and RDS specifically
   - C) No - it bills automatically and silently the moment you cross the limit, showing up on the normal monthly invoice
   - D) No, it bills you instantly and separately from your normal invoice

### Spot Instance Reclaiming: The 2-Minute Warning

8. How much warning does AWS give before reclaiming a Spot instance?
   - A) 24 hours
   - B) No warning at all
   - C) 30 minutes
   - D) 2 minutes

9. What should a workload be capable of doing to be safely run on Spot instances?
   - A) Saving state or shutting down gracefully within a very short window, or otherwise tolerating sudden interruption
   - B) Running continuously with zero tolerance for interruption
   - C) Serving live customer traffic directly
   - D) Committing to 1-3 years of guaranteed usage

10. Why is a live, customer-facing database a poor fit for Spot instances?
    - A) Databases cannot technically run on EC2 at all
    - B) Losing the instance mid-request drops service out from under real users, and the warning window isn't enough time to prevent that
    - C) Databases are not compatible with any EC2 pricing model except On-Demand
    - D) Spot instances cannot store data of any kind

### Requesting a Service Quota Increase

11. Where do you go to check your current AWS quotas and request an increase?
    - A) AWS Budgets
    - B) Cost Explorer
    - C) The Service Quotas console (or the aws service-quotas CLI)
    - D) The AWS Organizations console

12. Why are some quota increase requests approved automatically while others require manual review?
    - A) It's random and has no consistent pattern
    - B) Manual review is required for every single request, with no auto-approvals
    - C) Approval speed depends only on how long you've had your AWS account
    - D) It comes down to risk - small increases are low-risk and auto-approved, large or unusual jumps get manual review

13. What is manual review of a large quota increase request meant to guard against?
    - A) Runaway costs or abuse, like an accidental denial-of-service-style usage spike
    - B) Competing AWS customers stealing capacity
    - C) Violations of AWS's terms of service around trademarks
    - D) Fraudulent AWS Free Tier signups only

### Consolidated Billing's Discount Mechanics

14. Why does pooling usage across every linked account under an AWS Organization help reach cheaper pricing tiers faster?
    - A) It doesn't - each linked account is still billed at its own individual tier
    - B) Some AWS pricing gets cheaper as usage climbs, and the combined total crosses into cheaper tiers faster than one small account could alone
    - C) AWS grants organizations a flat 50% discount regardless of usage
    - D) Pricing tiers only apply to Reserved pricing, not to pooled usage

15. What happens to unused reserved capacity in one linked account under Consolidated Billing?
    - A) It expires unused at the end of each billing cycle
    - B) It is refunded in cash to that account
    - C) It can automatically apply to another linked account's matching usage instead of going to waste
    - D) It is converted into Spot pricing credits

16. Why would a small department within a large company benefit from Consolidated Billing?
    - A) It doesn't - Consolidated Billing only benefits the largest account in the organization
    - B) It removes that department's need for an AWS account entirely
    - C) It exempts that department from AWS service quotas
    - D) It gets pulled into pricing tiers and discounts it would never reach running as a standalone account

### AWS Budgets vs. Cost Explorer

17. Which tool would you open to find out which specific service drove last month's AWS bill up?
    - A) Cost Explorer
    - B) AWS Budgets
    - C) Service Quotas console
    - D) AWS Organizations

18. Which tool would you set up to make sure a cost spike doesn't sneak up on you again going forward?
    - A) Cost Explorer
    - B) AWS Budgets
    - C) AWS Glue DataBrew
    - D) Consolidated Billing

19. What's the core difference in how AWS Budgets and Cost Explorer relate to time?
    - A) They both only look backward at historical data
    - B) They both only look forward and predict future costs
    - C) AWS Budgets is forward-looking (alerts on thresholds); Cost Explorer is backward-looking (historical analysis)
    - D) There is no meaningful difference - they're interchangeable

## Answer Key

1. A - The core distinction is who's doing the talking to AWS: a human (or their script) for CLI, the application's own code for SDK.
2. B - The app's own code needs to make that call automatically, live, with no human running a command per upload.
3. C - Code doing the connecting itself, with no human involved, is SDK territory.
4. D - Both the CLI and SDK let you automate interactions with AWS, which is exactly what makes them easy to blur together.
5. A - The moment usage crosses a Free Tier limit, AWS bills the overage automatically at standard rates, with no grace period.
6. B - Proactively setting up a budget alert via AWS Budgets is the only way to get warned before it happens.
7. C - AWS bills automatically and silently the moment you cross the limit - it just shows up on the normal monthly invoice.
8. D - AWS gives a 2-minute warning before reclaiming a Spot instance.
9. A - A Spot-safe workload can save state or shut down gracefully in a short window, or otherwise tolerate sudden interruption.
10. B - Losing the instance mid-request drops service out from under real users, and the warning window isn't enough time to prevent that.
11. C - Quotas and increase requests are handled through the Service Quotas console (or the aws service-quotas CLI).
12. D - It comes down to risk: small increases are low-risk and auto-approved, large or unusual jumps get manual review.
13. A - Manual review guards against runaway costs or abuse, like an accidental denial-of-service-style usage spike.
14. B - Some AWS pricing gets cheaper as usage climbs, so pooling usage crosses into cheaper tiers faster than one small account could alone.
15. C - Unused reserved capacity in one linked account can automatically apply to another linked account's matching usage instead of going to waste.
16. D - A small department gets pulled into pricing tiers and discounts it would never reach running as a standalone account.
17. A - Cost Explorer is the backward-looking tool for seeing what already drove past spending.
18. B - AWS Budgets is the forward-looking tool that alerts you before a cost spike sneaks up on you again.
19. C - AWS Budgets is forward-looking (alerts on thresholds); Cost Explorer is backward-looking (historical analysis).
