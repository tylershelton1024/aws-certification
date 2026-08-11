// Chapter 1: AWS Cloud Fundamentals - flashcard data.
// This is the single source of truth for this chapter's card content as far
// as the HTML viewers are concerned - flashcards.html (this chapter) and
// all_flashcards.html (whole book) both load this same file via <script
// src="...">, so there is only one place to update, not several.
//
// This file itself is generated from flashcards.md and
// deeper_dive_flashcards.md - if those change, regenerate this file to match.
const chapter01Decks = {
  "core": [
    { "term": "Elasticity", "definition": "The ability of cloud resources to automatically scale up or down based on demand - you pay only for what you use, when you use it." },
    { "term": "Shared Responsibility Model", "definition": "AWS secures the underlying cloud infrastructure; you're responsible for securing what you put in it and who has access to it." },
    { "term": "IaaS (Infrastructure as a Service)", "definition": "You get virtualized hardware (like EC2) and manage everything from the OS up yourself - maximum control, maximum responsibility." },
    { "term": "PaaS (Platform as a Service)", "definition": "AWS manages the OS, runtime, and middleware; you just provide your application code (e.g. AWS Elastic Beanstalk)." },
    { "term": "SaaS (Software as a Service)", "definition": "The vendor manages everything, including the application itself; you just use it (e.g. Netflix, Gmail, Dropbox)." },
    { "term": "Service Models Comparison (IaaS vs. PaaS vs. SaaS)", "definition": "The pizza analogy, side by side: IaaS is making a pizza from scratch (you control everything, do all the work). PaaS is pizza delivered for you to bake (AWS handles the infrastructure, you just handle your code/application). SaaS is pizza arriving hot and ready (everything, including the application itself, is already handled - you just consume it). Same underlying spectrum of \"how much do you manage yourself,\" three different points on it." },
    { "term": "Amazon EC2", "definition": "Elastic Compute Cloud - virtual servers (\"instances\") you configure from the ground up. The classic IaaS example." },
    { "term": "AWS Elastic Beanstalk", "definition": "AWS's PaaS offering. You hand over your code; AWS handles provisioning, scaling, and load balancing underneath it." },
    { "term": "Flexibility (Key Benefit)", "definition": "AWS scales to demand, and servers stay available no matter the load." },
    { "term": "Speed (Key Benefit)", "definition": "Instant access to compute and data - developers can focus on their actual jobs instead of waiting on infrastructure to be provisioned." },
    { "term": "Security (Key Benefit)", "definition": "Built into AWS's foundation, including encryption, identity management, and compliance tools - though the Shared Responsibility Model still applies: AWS secures the underlying infrastructure, you secure what you put in it." },
    { "term": "Reliability (Key Benefit)", "definition": "Improved speed and reliability across AWS's regions." },
    { "term": "Business Impact (Key Benefit)", "definition": "Growth, better user satisfaction, and faster innovation, since teams don't have to build everything themselves." }
  ],
  "deeper": [
    { "term": "Hypervisor", "definition": "The software layer that divides a single physical server into multiple, isolated virtual machines." },
    { "term": "Virtualization", "definition": "The technology that lets one physical host run multiple isolated virtual machines (like EC2 instances), enabling shared hardware without customers being able to access each other's data." },
    { "term": "Nitro System", "definition": "AWS's current approach to EC2 virtualization, combining dedicated hardware with a lightweight hypervisor. (Confidence flag: exam-testability depth not verified.)" },
    { "term": "Runtime", "definition": "The environment needed to actually execute your code - for example, the Java Runtime Environment or the Node.js runtime." },
    { "term": "Middleware", "definition": "Software that sits between the OS and your application, handling things like request routing and queuing - the \"waiter\" connecting the kitchen (OS) and the table (app)." },
    { "term": "VPC (Virtual Private Cloud)", "definition": "Your own private, isolated slice of AWS's network." },
    { "term": "Subnet", "definition": "A smaller network segment that a VPC is divided into - public (internet-facing) or private (isolated)." },
    { "term": "Route Table", "definition": "Rules controlling how traffic flows between subnets and to/from the internet." },
    { "term": "Security Group", "definition": "A firewall applied to an individual EC2 instance." },
    { "term": "Network ACL", "definition": "A firewall applied at the subnet level, checking traffic before it reaches individual instances." },
    { "term": "Internet Gateway", "definition": "The door between a VPC and the public internet. One per VPC. Needs a route table rule pointing at it to actually be used. No hourly charge." },
    { "term": "NAT Gateway", "definition": "A separate resource from an internet gateway, used by private subnets that need outbound-only internet access without being directly reachable. Has an hourly charge plus per-GB fees." },
    { "term": "CIDR", "definition": "Classless Inter-Domain Routing - a compact way to write a range of IP addresses (e.g. 10.0.0.0/16) instead of listing each one. Used for VPC/subnet sizing." },
    { "term": "Octet", "definition": "One group of 8 bits in an IP address (e.g. the \"10\" in 10.0.0.0). Each octet holds 256 possible values (0-255), since 2^8 = 256." },
    { "term": "CIDR Prefix Length", "definition": "The number after the slash in a CIDR block (e.g. the \"16\" in /16). It's how many of the 32 bits are locked as the network prefix - fewer locked bits means more addresses, so a smaller number means a bigger block." },
    { "term": "Private IP Ranges", "definition": "10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 - reserved address ranges for internal/private networks, never used directly on the public internet." },
    { "term": "Stateful (Security Groups)", "definition": "If a request is allowed in by a security group, the matching response is automatically allowed back out - no separate outbound rule needed. Different from Network ACLs, which are stateless." },
    { "term": "Stateless (Network ACLs)", "definition": "A stateless firewall does not remember past traffic, so it cannot tell that a piece of outbound traffic is the response to an inbound request it already allowed. It needs a separate, explicit rule for each direction. Different from Security Groups, which are stateful." },
    { "term": "Stateful vs. Stateless (Security Groups vs. Network ACLs)", "definition": "The core difference: a stateful firewall (security group) remembers a request it already allowed in, so it automatically permits the matching response back out - one rule covers both directions. A stateless firewall (Network ACL) has no memory of past traffic, so inbound and outbound each need their own explicit rule, even for what's really the same exchange." },
    { "term": "Public vs. Private IP", "definition": "The private IP is what a device uses inside its own network (e.g. 192.168.1.5 at home, or an EC2 instance's internal IP). The public IP is the address visible to the outside internet - a router or internet gateway translates between the two." },
    { "term": "HTTP", "definition": "HyperText Transfer Protocol - the standard protocol web browsers and servers use to exchange requests and responses. Defaults to port 80. Not encrypted on its own - see HTTPS." },
    { "term": "HTTPS", "definition": "HTTP wrapped in encryption (TLS/SSL) - same messages, unreadable in transit. Uses a different default port (443) than HTTP (80), which matters operationally: opening one port does not open the other." },
    { "term": "HTTP vs. HTTPS (Port Difference)", "definition": "Not two layered protocols in a stack - the same messages, either plain (HTTP, port 80) or encrypted (HTTPS, port 443). The operational trap: they use different default ports, so a security group or firewall rule opening one does not open the other. This caused a real bug in this project - a browser auto-upgraded a bare IP request to HTTPS, hitting port 443 with no rule allowing it through, even though port 80 was correctly open." },
    { "term": "SSH", "definition": "Secure Shell - a protocol for securely logging into a remote server's command line over a network. What actually lets you type commands directly on an EC2 instance from your own computer." },
    { "term": "SSH Key Pair", "definition": "A public/private key pair used to log into a server via SSH instead of a password. AWS keeps the public half; you download and keep the private half (a .pem file). Whoever holds that file can log in - never commit it to a repo." },
    { "term": "\"Permission Denied\" (SSH)", "definition": "Means the network connection itself worked (security groups/routing are fine) - the key specifically was rejected. Narrows the problem to the key file, its permissions, or the username." }
  ]
};
