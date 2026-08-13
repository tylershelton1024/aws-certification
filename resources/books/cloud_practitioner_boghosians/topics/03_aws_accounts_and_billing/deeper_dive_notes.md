---
title: "Chapter 3: AWS Accounts and Billing - Deeper Dive Notes"
tags: [chapter_03, accounts_and_billing, deeper_dive]
updated: 2026-08-12
---

# Chapter 3: AWS Accounts and Billing - Deeper Dive Notes

Source: written by the assistant based on a reinforcement conversation - not pulled directly from the book. Covers topics that go beyond what Chapter 3's core content explains.

## CLI vs. SDK: Who's Doing the Talking

Both CLI and SDK let you automate things, which makes them easy to blur together. The real distinction is *who is doing the talking to AWS*:

- **CLI** - a person (or a script that person wrote) runs individual AWS commands. There's always a human behind it somewhere, even if the commands are automated.
- **SDK** - the application's own code talks to AWS directly, as part of what the app does while it's running. No human is typing commands - the software manages itself.

Worked example: an app that stores every user's photo upload in S3 automatically, the moment they upload it. Nobody runs a CLI command per upload - the app's own code, using the SDK, makes that call live, as part of running. Same idea applies to a tool that reaches into a database to connect two applications together - if the tool's own code is what's doing the connecting, that's SDK territory, not CLI.

## Exceeding a Free Tier Limit: No Grace Period

There is no grace period. The moment usage crosses a Free Tier limit, AWS starts billing the overage at standard On-Demand rates automatically and silently - it just shows up on the normal monthly invoice, with no built-in warning beforehand.

The only way to get warned *before* it happens is to proactively set up a **budget alert** via AWS Budgets - AWS does not do this automatically. For anyone new to AWS, setting up a billing alert on day one is the single concrete safeguard against a surprise bill.

## Spot Instance Reclaiming: The 2-Minute Warning

When AWS needs Spot capacity back (for On-Demand/Reserved customers, or shifting demand elsewhere), it gives a **2-minute warning** before terminating the instance. That's the entire window to save state or shut down gracefully - not negotiable, and not guaranteed to be any longer.

This makes Spot suitable only for workloads that tolerate sudden interruption with a reduced/degraded workload rather than an outright failure - e.g. an overnight batch job processing a pile of images, where losing an instance just means finishing later. It's unsuitable for anything serving live traffic continuously (e.g. a database customers query directly), since losing that instance mid-request drops service out from under real users.

## Requesting a Service Quota Increase

Current quotas and increase requests are both handled through the **Service Quotas** console (or the `aws service-quotas` CLI). Some increase requests are approved automatically and near-instantly; others go through manual AWS review before approval.

The difference comes down to risk/blast-radius: small increases within normal bounds are low-risk and get auto-approved, while large jumps or unusual-looking requests get manual review specifically to guard against runaway costs or abuse (e.g. an accidental denial-of-service-like usage spike) - protecting both AWS's shared infrastructure and the requesting customer's own bill.

## Consolidated Billing's Discount Mechanics

AWS combines usage across every linked account in an Organization *before* applying volume-based discounts, rather than evaluating each account's usage in isolation:

- Some AWS pricing gets cheaper as usage climbs (e.g. S3's tiered pricing). Pooling usage across every linked account lets the combined total cross into cheaper tiers faster than any single small account could reach alone.
- Reserved Instances and Savings Plans work the same way - unused reserved capacity in one account can automatically apply to another linked account's matching usage instead of going to waste.
- Net effect: smaller departments within a larger company get pulled into pricing tiers and discounts they'd never reach running as a fully separate, standalone AWS account. Billing benefits are earned by the organization as a pooled group, not by each account individually.

## AWS Budgets vs. Cost Explorer

These two tools split the job by time direction rather than overlapping:

- **AWS Budgets** - forward-looking. Set a cost or usage threshold, get alerted when approaching or exceeding it. This is the concrete tool behind "set up a billing alert."
- **Cost Explorer** - backward-looking. Visualizes historical spending - by service, account, tag, time period - to show trends and identify what actually drove past spending, and can forecast future costs from that history.

Rule of thumb: to find out what already happened, open Cost Explorer. To make sure something doesn't sneak up again going forward, set up AWS Budgets.
