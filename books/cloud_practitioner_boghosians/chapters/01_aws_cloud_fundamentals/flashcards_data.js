// Chapter 1: AWS Cloud Fundamentals - flashcard data.
// This is the single source of truth for this chapter's card content as far
// as the HTML viewers are concerned - flashcards.html (this chapter) and
// all_flashcards.html (whole book) both load this same file via <script
// src="...">, so there is only one place to update, not several.
//
// This file itself is generated from flashcards.md and
// deeper_dive_flashcards.md - if those change, regenerate this file to match.
const chapter01Decks = {
  core: [
    { term: "Elasticity", definition: "The ability of cloud resources to automatically scale up or down based on demand - you pay only for what you use, when you use it." },
    { term: "Shared Responsibility Model", definition: "AWS secures the underlying cloud infrastructure; you're responsible for securing what you put in it and who has access to it." },
    { term: "IaaS (Infrastructure as a Service)", definition: "You get virtualized hardware (like EC2) and manage everything from the OS up yourself - maximum control, maximum responsibility." },
    { term: "PaaS (Platform as a Service)", definition: "AWS manages the OS, runtime, and middleware; you just provide your application code (e.g. AWS Elastic Beanstalk)." },
    { term: "SaaS (Software as a Service)", definition: "The vendor manages everything, including the application itself; you just use it (e.g. Netflix, Gmail, Dropbox)." },
    { term: "Amazon EC2", definition: "Elastic Compute Cloud - virtual servers (\"instances\") you configure from the ground up. The classic IaaS example." },
    { term: "AWS Elastic Beanstalk", definition: "AWS's PaaS offering. You hand over your code; AWS handles provisioning, scaling, and load balancing underneath it." }
  ],
  deeper: [
    { term: "Hypervisor", definition: "The software layer that divides a single physical server into multiple, isolated virtual machines." },
    { term: "Virtualization", definition: "The technology that lets one physical host run multiple isolated virtual machines (like EC2 instances), enabling shared hardware without customers being able to access each other's data." },
    { term: "Nitro System", definition: "AWS's current approach to EC2 virtualization, combining dedicated hardware with a lightweight hypervisor. (Confidence flag: exam-testability depth not verified.)" },
    { term: "Runtime", definition: "The environment needed to actually execute your code - for example, the Java Runtime Environment or the Node.js runtime." },
    { term: "Middleware", definition: "Software that sits between the OS and your application, handling things like request routing and queuing - the \"waiter\" connecting the kitchen (OS) and the table (app)." },
    { term: "VPC (Virtual Private Cloud)", definition: "Your own private, isolated slice of AWS's network." },
    { term: "Subnet", definition: "A smaller network segment that a VPC is divided into - public (internet-facing) or private (isolated)." },
    { term: "Route Table", definition: "Rules controlling how traffic flows between subnets and to/from the internet." },
    { term: "Security Group", definition: "A firewall applied to an individual EC2 instance." },
    { term: "Network ACL", definition: "A firewall applied at the subnet level, checking traffic before it reaches individual instances." },
    { term: "Internet/NAT Gateway", definition: "Controls whether and how private resources can reach the internet." },
    { term: "CIDR", definition: "Classless Inter-Domain Routing - a compact way to write a range of IP addresses (e.g. 10.0.0.0/16) instead of listing each one. Used for VPC/subnet sizing." },
    { term: "Octet", definition: "One group of 8 bits in an IP address (e.g. the \"10\" in 10.0.0.0). Each octet holds 256 possible values (0-255), since 2^8 = 256." },
    { term: "CIDR Prefix Length", definition: "The number after the slash in a CIDR block (e.g. the \"16\" in /16). It's how many of the 32 bits are locked as the network prefix - fewer locked bits means more addresses, so a smaller number means a bigger block." },
    { term: "Private IP Ranges", definition: "10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 - reserved address ranges for internal/private networks, never used directly on the public internet." }
  ]
};
