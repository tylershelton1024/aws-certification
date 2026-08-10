---
title: "Chapter 1: AWS Cloud Fundamentals - Deeper Dive Questions"
tags: [chapter_01, cloud_fundamentals, deeper_dive, practice_questions]
updated: 2026-08-09
---

# Chapter 1: AWS Cloud Fundamentals - Deeper Dive Questions

Source: written by the assistant based on `deeper_dive_notes.md` and our conversation, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Covers topics that went beyond the book's core content - see `practice_questions.md` for questions on the book material itself. Answers are in the Answer Key at the bottom, so you can try answering first.

## Questions

1. What is the primary role of a hypervisor in AWS's virtualization layer?
   - A) It encrypts data at rest
   - B) It divides a single physical server into multiple, isolated virtual machines
   - C) It manages billing across AWS accounts
   - D) It replaces the need for an operating system

2. Which statement correctly describes the relationship between a physical host and EC2 instances?
   - A) One EC2 instance always requires its own dedicated physical server
   - B) A single physical host, through virtualization, can run multiple EC2 instances, each behaving as its own isolated virtual machine
   - C) EC2 instances do not use virtualization at all
   - D) Multiple customers' EC2 instances on the same host can access each other's data

3. In the OS-upward responsibility breakdown, which layer is responsible for actually executing your application's code (e.g. running a Java or Node.js app)?
   - A) Middleware
   - B) Runtime
   - C) Hypervisor
   - D) Route table

4. Which AWS networking component acts as a firewall applied to an individual EC2 instance, rather than an entire subnet?
   - A) Network ACL
   - B) Route table
   - C) Security group
   - D) Internet gateway

5. Which AWS networking component acts as a firewall at the subnet level, checking traffic before it reaches individual instances?
   - A) Security group
   - B) Network ACL
   - C) VPC
   - D) NAT gateway

6. A company has legacy, on-premises software that needs very specific OS-level configuration to run. Which service model is most appropriate for migrating it to AWS?
   - A) SaaS, since it requires the least setup
   - B) PaaS, since AWS manages the OS
   - C) IaaS, since it provides full control down to the OS level
   - D) Legacy software cannot run in the cloud

7. Why is it generally harder to migrate an application away from a PaaS platform compared to an IaaS-hosted application?
   - A) PaaS applications are always written in a proprietary programming language
   - B) The application becomes structurally dependent on the platform's specific deployment model, environment variables, and platform-managed behaviors
   - C) PaaS applications cannot store any data
   - D) IaaS applications cannot be moved between cloud providers either

## Answer Key

1. B - The hypervisor divides physical hardware into isolated virtual machines.
2. B - One physical host can run many EC2 instances; each instance is its own isolated virtual machine.
3. B - The runtime (e.g. Java Runtime Environment, Node runtime) is what executes your code.
4. C - Security groups are firewalls scoped to an individual instance.
5. B - Network ACLs are firewalls scoped to an entire subnet.
6. C - IaaS gives the OS-level control legacy software typically needs.
7. B - Migration difficulty comes from structural dependency on the platform's deployment model and managed behaviors, not just a feature limitation.
