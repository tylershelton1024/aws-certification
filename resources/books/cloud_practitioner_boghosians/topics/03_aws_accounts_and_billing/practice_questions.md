---
title: "Chapter 3: AWS Accounts and Billing - Practice Questions"
tags: [chapter_03, accounts_and_billing, practice_questions]
updated: 2026-08-12
---

# Chapter 3: AWS Accounts and Billing - Practice Questions

Source: written by the assistant based on your notes, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Scoped to the book's core content only - see `deeper_dive_questions.md` for questions on topics that went beyond the book. Questions are grouped under `###` headings matching notes.md's sections, so they can eventually be filtered by section. Answers are in the Answer Key at the bottom, so you can try answering first.

## Core Concepts Questions

### Creating an AWS Account

1. Creating an AWS account is most similar to which everyday action, according to the household analogy?
   - A) Opening a bank account for your household
   - B) Renting a car
   - C) Signing up for a gym membership
   - D) Subscribing to a streaming service

2. What piece of information does AWS require in order to create an account?
   - A) A government-issued ID
   - B) An email address
   - C) A credit score
   - D) A physical mailing address

3. Why does it matter to stay aware of what's going on with your AWS account from the very start?
   - A) AWS requires you to memorize your account settings
   - B) It only matters after you exceed the Free Tier
   - C) So you can avoid getting caught off guard by unexpected costs
   - D) It has no real importance - it's just a formality

### Ways to Interact with AWS

4. Which way of interacting with AWS is best described as a simple, no-coding-required graphical interface, like a touchscreen panel on your wall?
   - A) SDK
   - B) API Gateway
   - C) CLI
   - D) Console

5. Why do power users and admins favor the CLI?
   - A) It saves time and allows for automation - the most flexible option
   - B) It requires no technical knowledge at all
   - C) It's the only way to create an AWS account
   - D) It's exclusively used for billing tasks

6. Which way of interacting with AWS is defined by the application's own code talking to AWS directly, with no human running commands at all?
   - A) Console
   - B) SDK
   - C) CLI
   - D) Service Quotas

7. In the smart home analogy, what do CLI, Console, and SDK all represent?
   - A) Three unrelated AWS billing categories
   - B) Three tiers of AWS Free Tier eligibility
   - C) Three ways to control AWS, differing by how hands-on you want to be
   - D) Three physical locations where AWS infrastructure lives

8. A team wants to script the daily teardown and rebuild of test environments, with no one manually clicking through menus. Which interaction method fits best?
   - A) CLI
   - B) Console
   - C) AWS Budgets
   - D) Cost Explorer

### AWS Free Tier

9. What is the overall purpose of the AWS Free Tier, according to the grocery store sample analogy?
   - A) To let startups, learners, developers, and businesses sample services before committing to pay for them
   - B) To permanently replace paid AWS pricing for small businesses
   - C) To restrict new accounts from using more than one AWS service
   - D) To only benefit AWS's largest enterprise customers

10. How much does AWS Lambda include as part of the "always free" tier?
    - A) 25 GB of storage
    - B) 1,000,000 requests per month
    - C) 40 hours of processing per month
    - D) 750 hours per month

11. How much storage does DynamoDB include as part of the "always free" tier?
    - A) 5 GB
    - B) 1,000,000 publishes per month
    - C) 25 GB of storage
    - D) Unlimited storage

12. How many publishes does Amazon SNS include as part of the "always free" tier?
    - A) 40 hours per month
    - B) 750 hours per month
    - C) 25 GB
    - D) 1,000,000 publishes per month

13. How many hours of processing does AWS Glue DataBrew include as part of the "always free" tier?
    - A) 40 hours per month
    - B) 750 hours per month
    - C) 1,000,000 requests per month
    - D) 5 GB

14. As part of the 12-month free tier, how much EC2 usage is included per month?
    - A) 5 GB of storage
    - B) 25 GB of storage
    - C) 1,000,000 requests
    - D) 750 hours of t2.micro or t3.micro usage - enough to run one instance continuously all month

15. As part of the 12-month free tier, how much free storage does Amazon S3 include?
    - A) 25 GB
    - B) 750 hours per month
    - C) 5 GB
    - D) Unlimited storage for the first year

16. As part of the 12-month free tier, how much usage does Amazon RDS include per month?
    - A) 40 hours
    - B) 750 hours
    - C) 5 GB
    - D) 1,000,000 publishes

17. What kind of Free Tier offer does Amazon Redshift provide?
    - A) 750 hours per month, always free
    - B) 25 GB of storage, always free
    - C) Full access for the account's entire first year
    - D) A 30-day free trial

18. What happens if you exceed your AWS Free Tier limits?
    - A) Your account is automatically suspended
    - B) You are billed at standard rates for the amount you exceeded
    - C) AWS deletes the exceeding resources automatically
    - D) Nothing - Free Tier limits are only suggestions

19. What's the key difference between an "always free" service and a "12-month free tier" service?
    - A) 12-month free tier services never expire; always-free services expire after 30 days
    - B) There is no real difference between the two categories
    - C) Always-free services apply no matter how long you've had your account; 12-month free tier services start counting down from account creation
    - D) Always-free services require a paid subscription first

### Pricing Models

20. Which pricing model is described using the analogy of paying for electricity or water, monitored by the minute, second, or hour?
    - A) Reserved pricing
    - B) Spot pricing
    - C) Consolidated billing
    - D) On-Demand pricing

21. Which pricing model uses the analogy of committing to a gym membership, in exchange for a discount of up to 72%?
    - A) Reserved pricing
    - B) On-Demand pricing
    - C) Spot pricing
    - D) AWS Organizations

22. Which pricing model offers up to 90% off, but the resources can be taken back by AWS at any time?
    - A) On-Demand pricing
    - B) Spot pricing
    - C) Reserved pricing
    - D) Consolidated billing

23. Can you use more than one AWS pricing model within the same account?
    - A) No, an account must pick exactly one pricing model
    - B) Only if you contact AWS support for special approval
    - C) Yes, you can mix and match different pricing models within the same account
    - D) Only Reserved and On-Demand can be combined; Spot is always separate

24. Which pricing model best fits a production database that needs to run continuously for the next 3 years?
    - A) On-Demand pricing
    - B) Spot pricing
    - C) AWS Free Tier
    - D) Reserved pricing

25. Which pricing model best fits a short-term experiment with unpredictable, new workload patterns?
    - A) On-Demand pricing
    - B) Reserved pricing
    - C) Spot pricing
    - D) Consolidated billing

### AWS Service Limits and Quotas

26. What is a quota, in the context of a new AWS account?
    - A) A one-time signup fee
    - B) A safe default boundary set on the account, like a limit on how many EC2 instances you can run at first
    - C) A discount applied automatically after 12 months
    - D) A mandatory training course for new users

27. Who do AWS service quotas protect?
    - A) Only AWS's own infrastructure
    - B) Neither AWS nor the customer - they exist purely for legal reasons
    - C) Only the customer
    - D) Both the customer (from accidentally overspending) and AWS's own infrastructure

28. Are AWS service quotas fixed permanently once an account is created?
    - A) No, they're flexible - you can request an increase, and AWS can raise your limits
    - B) Yes, quotas can never change for the life of an account
    - C) Only Enterprise Support customers can ever request a quota increase
    - D) Quotas double automatically every year

29. Understanding AWS service limits is best described as being about which of these?
    - A) Restriction for its own sake
    - B) A punishment for new accounts
    - C) Readiness, not restriction
    - D) A billing category, not a technical one

### AWS Organizations and Consolidated Billing

30. What does AWS Organizations let a company do?
    - A) Automatically encrypt all data across every account
    - B) Run multiple teams under a single set of connected AWS accounts, with one main account managing the others
    - C) Bypass AWS service quotas entirely
    - D) Merge two separate Regions into one

31. What does Consolidated Billing do, according to the shared family budget analogy?
    - A) Gives every linked account its own completely separate invoice
    - B) Removes the need for any AWS account to pay for usage
    - C) Combines all linked accounts' charges into a single invoice
    - D) Only applies to AWS's largest enterprise customers

32. Besides producing a single invoice, what's another advantage Consolidated Billing offers?
    - A) It disables AWS service quotas for all linked accounts
    - B) It removes the Free Tier limits for every linked account
    - C) It guarantees every linked account pays the exact same amount
    - D) Discounts are calculated from combined usage across the organization, so even small departments can benefit

33. What is AWS Budgets used for?
    - A) Visualizing historical spending trends only
    - B) Filing tax documents related to AWS usage
    - C) Setting a cost or usage threshold and getting alerted when approaching or exceeding it
    - D) Automatically canceling services that go over budget

34. What is Cost Explorer used for?
    - A) Automatically lowering your AWS bill
    - B) Visualizing historical AWS spending - by service, account, tag, or time period - to see trends and forecast future costs
    - C) Setting forward-looking cost alerts
    - D) Requesting AWS service quota increases

35. What overall goal does AWS Organizations help a company balance?
    - A) Independence for individual teams with central control over billing and oversight
    - B) Maximum spend with minimum oversight
    - C) Eliminating the need for any account-level permissions
    - D) Replacing the AWS Free Tier for every linked account

36. What advantage does AWS Organizations provide by maintaining a central view of services across linked accounts?
    - A) It automatically writes application code for every account
    - B) It removes the need for individual AWS accounts entirely
    - C) It guarantees zero security incidents
    - D) It helps maintain security and compliance across the organization

## Answer Key

1. A - Creating an AWS account is like opening a bank account for your household - the foundational setup step.
2. B - AWS needs an email address to create the account.
3. C - Staying aware of what's going on helps you avoid getting caught off guard by unexpected costs.
4. D - The Console is the simple, no-coding-required graphical interface, like a touchscreen panel.
5. A - The CLI saves time and allows for automation, making it the most flexible option for power users and admins.
6. B - The SDK is what lets an application's own code talk to AWS directly, with no human running commands.
7. C - CLI, Console, and SDK are three ways to control AWS, differing by how hands-on you want to be.
8. A - Scripting repeatable, hands-off automation is exactly what the CLI is for.
9. A - The AWS Free Tier lets startups, learners, developers, and businesses sample services before committing to pay.
10. B - AWS Lambda's always-free tier includes 1,000,000 requests per month.
11. C - DynamoDB's always-free tier includes 25 GB of storage.
12. D - Amazon SNS's always-free tier includes 1,000,000 publishes per month.
13. A - AWS Glue DataBrew's always-free tier includes 40 hours of processing per month.
14. D - EC2's 12-month free tier includes 750 hours/month of t2.micro or t3.micro usage - enough for one instance to run continuously all month.
15. C - Amazon S3's 12-month free tier includes 5 GB of free storage.
16. B - Amazon RDS's 12-month free tier includes 750 hours/month of usage.
17. D - Amazon Redshift is offered as a 30-day free trial.
18. B - Exceeding Free Tier limits means you're billed at standard rates for the overage.
19. C - Always-free services apply no matter how long you've had your account; 12-month free tier services start counting down from account creation.
20. D - On-Demand pricing is monitored by the minute, second, or hour, like paying for electricity or water.
21. A - Reserved pricing uses the gym membership analogy - commit for a discount of up to 72%.
22. B - Spot pricing offers up to 90% off, but the resources can be reclaimed by AWS at any time.
23. C - You can mix and match different pricing models within the same account.
24. D - A long-term, continuous, non-interruptible workload like a production database fits Reserved pricing.
25. A - On-Demand pricing fits unpredictable workloads, new projects, and short-term experiments.
26. B - A quota is a safe default boundary set on a new account, like a limit on EC2 instances.
27. D - Quotas protect both the customer from accidentally overspending and AWS's own infrastructure.
28. A - Quotas are flexible - you can request an increase, and AWS can raise your limits.
29. C - Understanding service limits is about readiness, not restriction.
30. B - AWS Organizations lets multiple teams run under a single set of connected accounts, with one main account managing the others.
31. C - Consolidated Billing combines all linked accounts' charges into a single invoice, like a family's shared budget.
32. D - Discounts are calculated from combined usage across the organization, so even small departments can benefit.
33. C - AWS Budgets lets you set a cost or usage threshold and get alerted when approaching or exceeding it.
34. B - Cost Explorer visualizes historical spending by service, account, tag, or time period, to see trends and forecast costs.
35. A - AWS Organizations helps balance independence for individual teams with central control over billing and oversight.
36. D - A central view of services across linked accounts helps maintain security and compliance across the organization.
