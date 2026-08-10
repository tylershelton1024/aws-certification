---
title: "Hands-On 00: Account Setup"
tags: [hands_on, account_setup]
updated: 2026-08-09
---

# Hands-On 00: Account Setup

What was done to get a real AWS account ready for hands-on work, and why. Written generically - no account IDs, keys, or other identifying/credential details.

## What was set up

- Created a new AWS account (root user).
- Enabled MFA on the root account immediately, before doing anything else. Root is not used for day-to-day work from here on.
- Created an IAM user for daily use, with its own MFA.
- Set up a Zero Spend Budget (alerts on any spend above $0) plus AWS Free Tier usage alerts, so unexpected charges get caught quickly.

## Why this came first

This account, created after AWS's July 2025 Free Tier changes, gets credit-based Free Tier (not the older separate "750 EC2 hours/month" allowance) - so cost awareness and a billing alarm had to exist before creating any billable resources, not after.

## Note

This covers almost exactly what Chapter 3 (AWS Accounts and Billing) is about - it happened first out of necessity (had to exist before any other hands-on work), not because Chapter 3 was studied first.
