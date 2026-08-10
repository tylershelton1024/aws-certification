---
title: "Chapter 1: AWS Cloud Fundamentals - Deeper Dive Flashcards"
tags: [chapter_01, cloud_fundamentals, deeper_dive, flashcards]
updated: 2026-08-09
---

# Chapter 1: AWS Cloud Fundamentals - Deeper Dive Flashcards

Source: written by the assistant from deeper_dive_notes.md. Source of truth for the cards - `flashcards.html` (this chapter) and `../../all_flashcards.html` (whole book) are generated from files like this one and need to be regenerated if cards here change.

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

## Internet/NAT Gateway

Controls whether and how private resources can reach the internet.
