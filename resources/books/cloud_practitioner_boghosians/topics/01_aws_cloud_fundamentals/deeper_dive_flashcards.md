---
title: "Chapter 1: AWS Cloud Fundamentals - Deeper Dive Flashcards"
tags: [chapter_01, cloud_fundamentals, deeper_dive, flashcards]
updated: 2026-08-09
---

# Chapter 1: AWS Cloud Fundamentals - Deeper Dive Flashcards

Source: written by the assistant from deeper_dive_notes.md. Source of truth for the cards - `flashcards.html` (this chapter) and `../../../../../all_flashcards.html` (whole book) are generated from files like this one and need to be regenerated if cards here change.

## Hypervisor

The software layer that divides a single physical server into multiple, isolated virtual machines.

## Virtualization

The technology that lets one physical host run multiple isolated virtual machines (like EC2 instances), enabling shared hardware without customers being able to access each other's data.

## Nitro System

AWS's current approach to EC2 virtualization, combining dedicated hardware with a lightweight hypervisor. Confidence flag: exam-testability depth not verified.

## Runtime

The environment needed to actually execute your code - for example, the Java Runtime Environment or the Node.js runtime.

## Middleware

Software that sits between the OS and your application, handling things like request routing and queuing - the "waiter" connecting the kitchen (OS) and the table (app).

## VPC (Virtual Private Cloud)

Your own private, isolated slice of AWS's network.

## Subnet

A smaller network segment that a VPC is divided into - public (internet-facing) or private (isolated).

## Route Table

Rules controlling how traffic flows between subnets and to/from the internet.

## Security Group

A firewall applied to an individual EC2 instance.

## Network ACL

A firewall applied at the subnet level, checking traffic before it reaches individual instances.

## Internet Gateway

The door between a VPC and the public internet. One per VPC. Needs a route table rule pointing at it to actually be used. No hourly charge.

## NAT Gateway

A separate resource from an internet gateway, used by private subnets that need outbound-only internet access without being directly reachable. Has an hourly charge plus per-GB fees.

## CIDR

Classless Inter-Domain Routing - a compact way to write a range of IP addresses (e.g. `10.0.0.0/16`) instead of listing each one. Used for VPC/subnet sizing.

## Octet

One group of 8 bits in an IP address (e.g. the "10" in `10.0.0.0`). Each octet holds 256 possible values (0-255), since 2^8 = 256.

## CIDR Prefix Length

The number after the slash in a CIDR block (e.g. the "16" in `/16`). It's how many of the 32 bits are locked as the network prefix - fewer locked bits means more addresses, so a smaller number means a bigger block.

## Private IP Ranges

`10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` - reserved address ranges for internal/private networks, never used directly on the public internet.

## Stateful (Security Groups)

If a request is allowed in by a security group, the matching response is automatically allowed back out - no separate outbound rule needed. Different from Network ACLs, which are stateless.

## Public vs. Private IP

The private IP is what a device uses inside its own network (e.g. `192.168.1.5` at home, or an EC2 instance's internal IP). The public IP is the address visible to the outside internet - a router or internet gateway translates between the two.

## HTTPS

HTTP wrapped in encryption (TLS/SSL) - same messages, unreadable in transit. Uses a different default port (443) than HTTP (80), which matters operationally: opening one port does not open the other.

## SSH Key Pair

A public/private key pair used to log into a server instead of a password. AWS keeps the public half; you download and keep the private half (a `.pem` file). Whoever holds that file can log in - never commit it to a repo.

## "Permission Denied" (SSH)

Means the network connection itself worked (security groups/routing are fine) - the key specifically was rejected. Narrows the problem to the key file, its permissions, or the username.
