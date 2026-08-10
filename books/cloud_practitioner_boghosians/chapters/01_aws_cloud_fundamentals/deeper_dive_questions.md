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

8. Which AWS resource is the door between a VPC and the public internet, and requires a route table rule pointing at it to actually be used?
   - A) NAT Gateway
   - B) Internet Gateway
   - C) Security Group
   - D) Network ACL

9. Which AWS resource gives a private subnet outbound-only internet access, and unlike its similarly-named counterpart, has an hourly charge plus per-GB fees?
   - A) Internet Gateway
   - B) NAT Gateway
   - C) Route Table
   - D) VPC

10. Why doesn't a security group need a separate outbound rule to let a response back out, after the matching inbound request was allowed in?
    - A) Outbound traffic is never checked by security groups
    - B) Security groups are stateful - the response is automatically allowed back out
    - C) The internet gateway handles all outbound rules instead
    - D) Network ACLs override security group behavior

11. What does a "Permission denied" error when connecting via SSH actually indicate?
    - A) The network connection failed entirely
    - B) The instance isn't running
    - C) The network connection succeeded, but the key was rejected
    - D) The security group is blocking all traffic

12. A web app became unreachable even after the correct HTTP security group rule was added and confirmed. What was the actual remaining cause?
    - A) HTTP was disabled at the OS level
    - B) The browser auto-upgraded to HTTPS, which uses a different port (443) that wasn't open
    - C) The route table needed to be recreated
    - D) The VPC's CIDR block was too small

## Answer Key

1. B - The hypervisor divides physical hardware into isolated virtual machines.
2. B - One physical host can run many EC2 instances; each instance is its own isolated virtual machine.
3. B - The runtime (e.g. Java Runtime Environment, Node runtime) is what executes your code.
4. C - Security groups are firewalls scoped to an individual instance.
5. B - Network ACLs are firewalls scoped to an entire subnet.
6. C - IaaS gives the OS-level control legacy software typically needs.
7. B - Migration difficulty comes from structural dependency on the platform's deployment model and managed behaviors, not just a feature limitation.
8. B - The internet gateway is the door in/out of a VPC; the route table is what makes it actually usable.
9. B - NAT gateways are for private-subnet outbound access and are billed hourly plus per-GB, unlike internet gateways.
10. B - Security groups are stateful, so allowed inbound traffic gets its response allowed back out automatically.
11. C - "Permission denied" means the connection worked; the key itself was rejected.
12. B - HTTP and HTTPS use different default ports (80 vs. 443) - opening one doesn't open the other.
