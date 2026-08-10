---
title: "Chapter 1: AWS Cloud Fundamentals - Practice Questions"
tags: [chapter_01, cloud_fundamentals, practice_questions]
updated: 2026-08-09
---

# Chapter 1: AWS Cloud Fundamentals - Practice Questions

Source: written by the assistant based on your notes and our conversation, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Scoped to the book's core content only - see `deeper_dive_questions.md` for questions on topics that went beyond the book. Answers are in the Answer Key at the bottom, so you can try answering first.

## Core Concepts Questions

1. Which of the following best describes the primary advantage of cloud elasticity?
   - A) You pay a fixed monthly fee no matter how much you use
   - B) Resources automatically scale up or down based on demand, and you pay only for what you use
   - C) You must manually order new hardware anytime you need more capacity
   - D) It removes the need for internet access

2. Under the AWS Shared Responsibility Model, which of the following is the customer always responsible for, regardless of service model?
   - A) Physical security of the data center
   - B) Securing their own data and controlling who has access to it
   - C) Maintaining the underlying network hardware
   - D) Patching the hypervisor

3. Which of the following requires a company to buy, build, and maintain its own physical servers?
   - A) IaaS
   - B) PaaS
   - C) SaaS
   - D) A traditional on-premises data center

4. Which AWS service is the classic example of Infrastructure as a Service (IaaS)?
   - A) AWS Elastic Beanstalk
   - B) Amazon EC2
   - C) Gmail
   - D) AWS Cost Explorer

5. A company wants to deploy their application by handing AWS their code, without managing servers, scaling, or load balancing themselves. Which service model are they using?
   - A) IaaS
   - B) PaaS
   - C) SaaS
   - D) On-premises

6. Netflix and Dropbox are commonly used as real-world examples of which AWS service model?
   - A) IaaS
   - B) PaaS
   - C) SaaS
   - D) None of the above

## Answer Key

1. B - Elasticity means scaling to demand and paying only for what's used.
2. B - Under the Shared Responsibility Model, you always secure your own data and access, no matter the service model.
3. D - Only a traditional on-premises data center requires owning physical hardware; all three AWS models remove that.
4. B - Amazon EC2 is the classic IaaS example - virtual servers you configure yourself.
5. B - Handing off code without managing servers/scaling/load balancing is the definition of PaaS.
6. C - Netflix and Dropbox are end-user products you just use - SaaS.
