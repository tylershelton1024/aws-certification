---
title: "Chapter 1: AWS Cloud Fundamentals - Deeper Dive Questions"
tags: [chapter_01, cloud_fundamentals, deeper_dive, practice_questions]
updated: 2026-08-10
---

# Chapter 1: AWS Cloud Fundamentals - Deeper Dive Questions

Source: written by the assistant based on `deeper_dive_notes.md` and our conversation, in CLF-C02 multiple-choice style - not pulled from an official AWS question bank. Covers topics that went beyond the book's core content - see `practice_questions.md` for questions on the book material itself. Questions are grouped under `###` headings matching deeper_dive_notes.md's sections. Answers are in the Answer Key at the bottom, so you can try answering first.

## Questions

### Choosing a Service Model: Pros, Cons, and Tradeoffs

6. A company has legacy, on-premises software that needs very specific OS-level configuration to run. Which service model is most appropriate for migrating it to AWS?
   - A) SaaS, since it requires the least setup
   - B) PaaS, since AWS manages the OS
   - C) Legacy software cannot run in the cloud
   - D) IaaS, since it provides full control down to the OS level

7. Why is it generally harder to migrate an application away from a PaaS platform compared to an IaaS-hosted application?
   - A) The application becomes structurally dependent on the platform's specific deployment model, environment variables, and platform-managed behaviors
   - B) PaaS applications are always written in a proprietary programming language
   - C) PaaS applications cannot store any data
   - D) IaaS applications cannot be moved between cloud providers either

14. Why might a company choose IaaS specifically, even though it requires more work than PaaS?
    - A) They need a specific OS or full server-level access that PaaS doesn't provide
    - B) IaaS is always the cheapest option available
    - C) IaaS requires no operational knowledge at all
    - D) PaaS is not a real AWS offering

### The Virtualization Layer

1. What is the primary role of a hypervisor in AWS's virtualization layer?
   - A) It divides a single physical server into multiple, isolated virtual machines
   - B) It encrypts data at rest
   - C) It manages billing across AWS accounts
   - D) It replaces the need for an operating system

2. Which statement correctly describes the relationship between a physical host and EC2 instances?
   - A) One EC2 instance always requires its own dedicated physical server
   - B) A single physical host, through virtualization, can run multiple EC2 instances, each behaving as its own isolated virtual machine
   - C) EC2 instances do not use virtualization at all
   - D) Multiple customers' EC2 instances on the same host can access each other's data

15. Why don't AWS customers need their own dedicated physical hardware?
    - A) AWS gives every customer a free physical server
    - B) Shared physical hardware is divided via virtualization, with each customer's slice isolated from others
    - C) Customers are required to bring their own hardware regardless
    - D) Virtualization eliminates the need for any physical hardware anywhere

### Runtime

3. In the OS-upward responsibility breakdown, which layer is responsible for actually executing your application's code (e.g. running a Java or Node.js app)?
   - A) Middleware
   - B) Hypervisor
   - C) Route table
   - D) Runtime

16. What would happen if you tried to run a Java application without the Java Runtime Environment present?
    - A) It would run normally, just slower
    - B) AWS would automatically substitute a different runtime
    - C) The OS wouldn't know how to execute the code, since the runtime is what makes that possible
    - D) Nothing - runtimes are optional for all languages

17. Is the runtime the same thing as the hypervisor?
    - A) Yes, they are two names for the exact same layer
    - B) Yes, but only for Java applications specifically
    - C) No - the runtime and hypervisor are unrelated to any of AWS's virtualization or execution layers
    - D) No - the runtime executes your code, which is a different job from the hypervisor's job of dividing hardware into virtual machines

### Middleware

18. What role does middleware play between the OS and an application?
    - A) It sits between the OS and the application, handling things like request routing and queuing
    - B) It replaces the OS entirely
    - C) It is only used for billing purposes
    - D) It divides physical hardware into virtual machines

19. The book's analogy describes middleware as which role?
    - A) The building supervisor who divides the building into apartments
    - B) The waiter that carries requests back and forth between the kitchen (OS) and the table (app)
    - C) The landlord who owns the physical property
    - D) The security guard checking IDs at the door

20. Which of the following is an example of what middleware handles?
    - A) Physical power and cooling for a data center
    - B) Encrypting data at rest in S3
    - C) Queuing and prioritizing work so the app and OS can communicate
    - D) Assigning public IP addresses to EC2 instances

### Configuration-Level Networking and Security

4. Which AWS networking component acts as a firewall applied to an individual EC2 instance, rather than an entire subnet?
   - A) Network ACL
   - B) Security group
   - C) Route table
   - D) Internet gateway

5. Which AWS networking component acts as a firewall at the subnet level, checking traffic before it reaches individual instances?
   - A) Security group
   - B) VPC
   - C) Network ACL
   - D) NAT gateway

9. Which AWS resource gives a private subnet outbound-only internet access, and unlike its similarly-named counterpart, has an hourly charge plus per-GB fees?
   - A) Internet Gateway
   - B) NAT Gateway
   - C) Route Table
   - D) VPC

21. What is a VPC (Virtual Private Cloud)?
    - A) A physical data center owned exclusively by one customer
    - B) A synonym for an Availability Zone
    - C) AWS's public internet backbone shared by all customers
    - D) Your own private, isolated slice of AWS's network

22. What are subnets, in the context of a VPC?
    - A) Smaller pieces that a VPC is divided into
    - B) A separate networking product unrelated to VPCs
    - C) Physical cables connecting AWS data centers
    - D) A type of firewall rule

23. What is the role of a route table?
    - A) It encrypts traffic between subnets
    - B) It controls how data moves between subnets
    - C) It stores a company's billing information
    - D) It replaces the need for a security group

### CIDR Notation

24. Why does a smaller number after the slash in CIDR notation (e.g. /8) mean a bigger address block, not a smaller one?
    - A) It doesn't - smaller numbers always mean smaller blocks
    - B) CIDR notation has no relationship to block size
    - C) Fewer locked bits leaves more bits free to vary, and each combination of free bits is one address in the block
    - D) AWS assigns block size randomly regardless of the CIDR number

25. Using the sizing shortcut, how many addresses are in a /24 block?
    - A) 65,536
    - B) 16,777,216
    - C) 65,000
    - D) 256

26. Why does an 8-bit octet allow exactly 256 possible values?
    - A) Each bit is either 0 or 1, and 8 bits gives 2^8 = 256 possible combinations
    - B) AWS arbitrarily chose 256 as a round number
    - C) An octet actually allows 255 values, not 256
    - D) 256 comes from multiplying 8 by 32

27. Which of the following are reserved as private IP ranges, never used directly on the public internet?
    - A) 8.8.8.0/24 and 1.1.1.0/24
    - B) 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16
    - C) Any range starting with a number above 200
    - D) There are no reserved private IP ranges - all ranges can be public or private

### The Internet Gateway, In Depth

8. Which AWS resource is the door between a VPC and the public internet, and requires a route table rule pointing at it to actually be used?
   - A) NAT Gateway
   - B) Security Group
   - C) Internet Gateway
   - D) Network ACL

28. How many VPCs can a single internet gateway attach to?
    - A) Up to five VPCs at once
    - B) An unlimited number of VPCs
    - C) Exactly one - it's a 1-to-1 relationship
    - D) It depends on the Region

29. What two jobs does an internet gateway actually do?
    - A) Encrypts data and manages billing
    - B) Runs application compute and stores logs
    - C) Creates security groups and manages IAM permissions
    - D) Gives the route table something to point at for internet-bound traffic, and translates between private and public IPs

### Security Groups Are Stateful (and the Full Request/Response Path)

10. Why doesn't a security group need a separate outbound rule to let a response back out, after the matching inbound request was allowed in?
    - A) Outbound traffic is never checked by security groups
    - B) The internet gateway handles all outbound rules instead
    - C) Network ACLs override security group behavior
    - D) Security groups are stateful - the response is automatically allowed back out

13. Why does a Network ACL need a separate, explicit rule for both inbound and outbound traffic, when a security group does not?
    - A) Network ACLs only support inbound rules, so outbound must be handled elsewhere
    - B) Network ACLs are stateless - they don't remember that outbound traffic is the response to an already-allowed inbound request
    - C) Security groups are actually slower, so they need the shortcut of statefulness
    - D) Network ACLs only apply to private subnets

30. In the full request/response path to a deployed app, what is the FIRST thing a browser's request hits after leaving the internet?
    - A) The internet gateway - the only door into the VPC
    - B) The security group
    - C) The EC2 instance directly
    - D) The route table, bypassing the internet gateway entirely

### Public vs. Private IP Addresses (and How "My IP" Is Found)

31. What does an AWS console feature like "My IP" actually do when creating a security group rule?
    - A) It generates a brand new IP address for your device
    - B) It reports whatever source IP the request arrived from
    - C) It contacts AWS support to verify your identity
    - D) It has no real function - it's just a placeholder

32. Why does every network request need to include a return address (source IP)?
    - A) It doesn't - responses find their way back automatically without one
    - B) Return addresses are only needed for HTTPS traffic
    - C) Otherwise a response could never find its way back to the requester
    - D) Source IPs are only used for billing purposes

33. What does a home router do that is conceptually similar to what an internet gateway does for a VPC?
    - A) It assigns CIDR blocks to every device on the network
    - B) It runs a hypervisor to virtualize home devices
    - C) It blocks all outbound internet traffic by default
    - D) It performs its own NAT translation, from private addresses to one shared public address

34. What is a device's public IP address?
    - A) The address a router presents to the internet, not the private IP of the actual device on the home/internal network
    - B) The same thing as a private IP, just a different name
    - C) An IP address only EC2 instances have, never home devices
    - D) An address that changes every time a request is sent

### HTTP vs. HTTPS: Different Default Ports

12. A web app became unreachable even after the correct HTTP security group rule was added and confirmed. What was the actual remaining cause?
    - A) HTTP was disabled at the OS level
    - B) The route table needed to be recreated
    - C) The browser auto-upgraded to HTTPS, which uses a different port (443) that wasn't open
    - D) The VPC's CIDR block was too small

35. Is HTTPS a completely separate protocol layered on top of HTTP?
    - A) Yes, HTTPS and HTTP share no relationship at all
    - B) No - HTTPS is the same HTTP messages, wrapped in encryption so they can't be read in transit
    - C) Yes, HTTPS replaces HTTP entirely as of recent AWS updates
    - D) No - HTTPS and HTTP are unrelated protocols that happen to sound similar

36. A browser auto-upgrades a bare IP address request to https://. What port does that request now try, and what happens if that port has no security group rule?
    - A) Port 22; the connection succeeds anyway since SSH is always open
    - B) Port 80; the request succeeds since that's the default
    - C) Port 443; the connection silently times out, since nothing allows traffic through that port
    - D) Port 3306; the request is redirected to a database

### SSH Key Pairs

11. What does a "Permission denied" error when connecting via SSH actually indicate?
    - A) The network connection succeeded, but the key was rejected
    - B) The network connection failed entirely
    - C) The instance isn't running
    - D) The security group is blocking all traffic

37. When is an EC2 key pair actually created?
    - A) After the instance is already running, via a separate console screen
    - B) Automatically by AWS, with no user involvement
    - C) Only if the customer requests it via a support ticket
    - D) During EC2 launch, in the "Key pair (login)" step, before the instance ever launches

38. What is AWS's default SSH username for Amazon Linux AMIs?
    - A) ec2-user
    - B) root
    - C) admin
    - D) aws-default

### Debugging Methodology

39. What should you check before assuming something is actually broken?
    - A) Immediately escalate to AWS support
    - B) Rule out the simplest explanation first - e.g. whether enough time has actually passed for setup to finish
    - C) Restart every resource in the account
    - D) Assume the most complex possible cause first

40. Why is checking indirect evidence (like a system/boot log) not always sufficient on its own?
    - A) Logs are never useful for debugging
    - B) Logs always contain the exact answer needed
    - C) Logs can be noisy and don't always show the specific thing you're looking for
    - D) Logs are only available to AWS support, not customers

41. How did SSH working over a public IP help narrow down a security group problem in the debugging example?
    - A) It didn't help at all - SSH and HTTP are completely unrelated
    - B) It proved the EC2 instance's OS had crashed
    - C) It proved the application code itself was broken
    - D) It proved the network path (gateway, route table, public IP) was fine, narrowing the problem down to the security group specifically

## Answer Key

1. A - The hypervisor divides physical hardware into isolated virtual machines.
2. B - One physical host can run many EC2 instances; each instance is its own isolated virtual machine.
3. D - The runtime (e.g. Java Runtime Environment, Node runtime) is what executes your code.
4. B - Security groups are firewalls scoped to an individual instance.
5. C - Network ACLs are firewalls scoped to an entire subnet.
6. D - IaaS gives the OS-level control legacy software typically needs.
7. A - Migration difficulty comes from structural dependency on the platform's deployment model and managed behaviors, not just a feature limitation.
8. C - The internet gateway is the door in/out of a VPC; the route table is what makes it actually usable.
9. B - NAT gateways are for private-subnet outbound access and are billed hourly plus per-GB, unlike internet gateways.
10. D - Security groups are stateful, so allowed inbound traffic gets its response allowed back out automatically.
11. A - "Permission denied" means the connection worked; the key itself was rejected.
12. C - HTTP and HTTPS use different default ports (80 vs. 443) - opening one doesn't open the other.
13. B - Network ACLs are stateless, so they can't infer that outbound traffic is a response to an already-allowed inbound request - each direction needs its own explicit rule.
14. A - IaaS is chosen when you need a specific OS or full server-level access that PaaS doesn't provide.
15. B - Shared physical hardware is divided via virtualization, with each customer's slice isolated from everyone else's.
16. C - Without the runtime, the OS wouldn't know how to execute the code - that's the runtime's job.
17. D - The runtime executes your code; the hypervisor divides hardware into virtual machines - two distinct jobs.
18. A - Middleware sits between the OS and the application, handling things like request routing and queuing.
19. B - The book's analogy describes middleware as the waiter carrying requests between the kitchen (OS) and the table (app).
20. C - Middleware handles queuing and prioritizing work so the app and OS can communicate.
21. D - A VPC is your own private, isolated slice of AWS's network.
22. A - Subnets are smaller pieces that a VPC is divided into.
23. B - A route table controls how data moves between subnets.
24. C - Fewer locked bits leaves more bits free to vary, and each combination of free bits is one address in the block.
25. D - A /24 block has 256 addresses (3 locked octets, 1 free octet: 256^1).
26. A - Each bit is either 0 or 1, and 8 bits gives 2^8 = 256 possible combinations.
27. B - 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 are the reserved private IP ranges.
28. C - One internet gateway attaches to exactly one VPC - a 1-to-1 relationship.
29. D - An internet gateway gives the route table something to point at for internet-bound traffic, and translates between private and public IPs.
30. A - The internet gateway is the only door into the VPC, so it's the first thing a request hits after leaving the internet.
31. B - "My IP" just reports whatever source IP the request arrived from.
32. C - A return address (source IP) is needed so a response can find its way back to the requester.
33. D - A home router performs its own NAT translation, from private addresses to one shared public address - the same underlying concept as an internet gateway.
34. A - A public IP is the address a router presents to the internet, not the private IP of the actual device on the internal network.
35. B - HTTPS is the same HTTP messages, wrapped in encryption so they can't be read in transit - not a separate protocol.
36. C - The browser tries port 443, which silently times out if nothing allows traffic through that port.
37. D - An EC2 key pair is created during launch, in the "Key pair (login)" step, before the instance ever launches.
38. A - The default SSH username for Amazon Linux AMIs is ec2-user.
39. B - Rule out the simplest explanation first - e.g. whether enough time has actually passed for setup to finish.
40. C - Logs can be noisy and don't always show the specific thing you're looking for.
41. D - SSH working proved the network path (gateway, route table, public IP) was fine, narrowing the problem down to the security group specifically.
