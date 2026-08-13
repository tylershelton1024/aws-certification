---
title: "Chapter 3: AWS Accounts and Billing - Deeper Dive Flashcards"
tags: [chapter_03, accounts_and_billing, deeper_dive, flashcards]
updated: 2026-08-12
---

# Chapter 3: AWS Accounts and Billing - Deeper Dive Flashcards

Source: written by the assistant from deeper_dive_notes.md. Source of truth for the cards - `flashcards.html` (this chapter) and `../../../../../all_flashcards.html` (whole book) are generated from files like this one and need to be regenerated if cards here change.

## CLI vs. SDK: Who's Doing the Talking

Both let you automate things, but the real difference is who's doing the talking to AWS. CLI: a person (or a script they wrote) runs individual commands - there's always a human behind it somewhere. SDK: the application's own code talks to AWS directly while running - no human typing commands at all. Example: an app that stores every user's photo upload in S3 the moment they upload it uses the SDK, not the CLI - nobody runs a command per upload.

## Exceeding a Free Tier Limit

There is no grace period. The moment usage crosses a Free Tier limit, AWS bills the overage at standard On-Demand rates automatically and silently - it just shows up on the normal monthly invoice. The only way to get warned beforehand is to proactively set up a budget alert via AWS Budgets; AWS does not do this automatically.

## Spot Instance Reclaiming (the 2-Minute Warning)

When AWS needs Spot capacity back, it gives a 2-minute warning before terminating the instance - the entire window to save state or shut down gracefully, not negotiable and not guaranteed to be any longer. This is why Spot only fits workloads that tolerate sudden interruption (e.g. an overnight batch job), not anything serving live traffic continuously (e.g. a database customers query directly).

## Requesting a Service Quota Increase

Current quotas and increase requests are both handled through the Service Quotas console (or the `aws service-quotas` CLI). Some requests are approved automatically and near-instantly; others go through manual AWS review. The difference comes down to risk: small increases within normal bounds are low-risk and auto-approved, while large or unusual-looking jumps get manual review to guard against runaway costs or abuse.

## Consolidated Billing's Discount Mechanics

AWS pools usage across every linked account in an Organization before applying volume-based discounts, rather than evaluating each account in isolation. Some pricing gets cheaper as usage climbs (e.g. S3's tiered pricing) - pooling usage lets the combined total cross into cheaper tiers faster than any single small account could alone. Reserved capacity works the same way: unused reserved capacity in one account can automatically apply to another linked account's matching usage instead of going to waste. Net effect: smaller departments get pulled into discounts they'd never reach running as a standalone account.

## AWS Budgets vs. Cost Explorer

These two tools split the job by time direction. AWS Budgets is forward-looking - set a cost/usage threshold, get alerted when approaching or exceeding it. Cost Explorer is backward-looking - visualizes historical spending by service, account, tag, or time period, and can forecast future costs from that history. Rule of thumb: to find out what already happened, open Cost Explorer; to make sure something doesn't sneak up again, set up AWS Budgets.
