# A Framework for Integrating Application Security into Software Engineering (FIASSE) and The Securable Software Engineering Model (SSEM)

> Request for Comments:
> 
> Obsoletes: None
> 
> Category: Informational
>
> Alton Crossley
> May 2025

## Abstract

> This document describes the Framework for Integrating Application Security into Software Engineering (FIASSE&trade;), a vendor independent framework designed to integrate application security principles and practices directly into the software engineering discipline. FIASSE addresses the common challenges of friction between Application Security (AppSec) and Development teams, the perceived slow progress in enhancing software security, the need to scale AppSec, and the need to empower developers to build securable code without requiring them to become penetration testing experts. Within this framework, the Securable Software Engineering Model (SSEM&trade;) provides a specific design language based on established software engineering terms, focusing on inherent security attributes of code and software architecture that contribute to security. This document outlines the core principles of the FIASSE framework, the key attributes defined by its SSEM model, methods for their integration into the development processes, practical guidance for developers, and considerations for adoption and evolution. It also defines a durable model as the foundation for FIASSE. The goal is to reduce the probability of material impact from cyber events by fostering a collaborative, developer-centric approach to application security, particularly for software that implements or relies on Internet protocols and services.

## Copyright Notice

> Copyright (c) 2025 Alton Crossley All rights reserved.
>
> see licence.txt for details.

## Table of Contents

- [A Framework for Integrating Application Security into Software Engineering (FIASSE) and The Securable Software Engineering Model (SSEM)](#a-framework-for-integrating-application-security-into-software-engineering-fiasse-and-the-securable-software-engineering-model-ssem)
  - [Abstract](#abstract)
  - [Copyright Notice](#copyright-notice)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1. The Application Security Challenge](#11-the-application-security-challenge)
    - [1.2. A Developer-Centric Security Paradigm](#12-a-developer-centric-security-paradigm)
    - [1.3. Document Purpose and Scope](#13-document-purpose-and-scope)
  - [2. Foundational Principles](#2-foundational-principles)
    - [2.1. The Securable Paradigm: No Static Secure State](#21-the-securable-paradigm-no-static-secure-state)
    - [2.2. Resiliently Add Computing Value](#22-resiliently-add-computing-value)
    - [2.3. Security Mission: Reducing Material Impact](#23-security-mission-reducing-material-impact)
    - [2.4. Mindset Convergence: Hacker vs. Engineer](#24-mindset-convergence-hacker-vs-engineer)
    - [2.5. Aligning Security with Development](#25-aligning-security-with-development)
  - [3. The Securable Software Engineering Model (SSEM)](#3-the-securable-software-engineering-model-ssem)
    - [3.1. Overview and Objectives](#31-overview-and-objectives)
    - [3.2. Core Securable Attributes](#32-core-securable-attributes)
      - [3.2.1. Maintainability](#321-maintainability)
        - [3.2.1.1. Analyzability](#3211-analyzability)
        - [3.2.1.2. Modifiability](#3212-modifiability)
        - [3.2.1.3. Testability](#3213-testability)
      - [3.2.2. Trustworthiness](#322-trustworthiness)
        - [3.2.2.1. Confidentiality](#3221-confidentiality)
        - [3.2.2.2. Accountability](#3222-accountability)
          - [3.2.2.2.1 Non-repudiation](#32221-non-repudiation)
        - [3.2.2.3. Authenticity](#3223-authenticity)
      - [3.2.3. Reliability](#323-reliability)
        - [3.2.3.1. Availability](#3231-availability)
        - [3.2.3.2. Integrity](#3232-integrity)
        - [3.2.3.3. Fault Tolerance](#3233-fault-tolerance)
        - [3.2.3.4. Resilience](#3234-resilience)
    - [3.3 SSEM as a Design Language](#33-ssem-as-a-design-language)
    - [3.4 Measuring SSEM Attributes](#34-measuring-ssem-attributes)
      - [3.4.1. Measuring Maintainability](#341-measuring-maintainability)
        - [3.4.1.1. Analyzability](#3411-analyzability)
        - [3.4.1.2. Modifiability](#3412-modifiability)
        - [3.4.1.3. Testability](#3413-testability)
      - [3.4.2. Measuring Trustworthiness](#342-measuring-trustworthiness)
        - [3.4.2.1. Confidentiality](#3421-confidentiality)
        - [3.4.2.2. Accountability](#3422-accountability)
        - [3.4.2.3. Authenticity](#3423-authenticity)
      - [3.4.3. Measuring Reliability](#343-measuring-reliability)
        - [3.4.3.1. Availability](#3431-availability)
        - [3.4.3.2. Integrity](#3432-integrity)
        - [3.4.3.3. Fault Tolerance](#3433-fault-tolerance)
        - [3.4.3.4. Resilience](#3434-resilience)
  - [4. Integrating SSEM into Development Strategy](#4-integrating-ssem-into-development-strategy)
    - [4.1. Applying SSEM to Dependency Management](#41-applying-ssem-to-dependency-management)
    - [4.2. Natively Extending Development Processes](#42-natively-extending-development-processes)
    - [4.3. The Role of Merge/Pull Request Reviews](#43-the-role-of-mergepull-request-reviews)
    - [4.4. Early Integration: Planning and Requirements](#44-early-integration-planning-and-requirements)
  - [5. Addressing Common AppSec Anti-Patterns](#5-addressing-common-appsec-anti-patterns)
    - [5.1. The "Shoveling Left" Phenomenon](#51-the-shoveling-left-phenomenon)
      - [5.1.1. Ineffective Vulnerability Reporting](#511-ineffective-vulnerability-reporting)
      - [5.1.2. Pitfalls of Exploit-First Training](#512-pitfalls-of-exploit-first-training)
    - [5.2. Strategic Use of Security Output](#52-strategic-use-of-security-output)
  - [6. Practical Guidance for Secure Software Development](#6-practical-guidance-for-secure-software-development)
    - [6.1. Establishing Clear Expectations](#61-establishing-clear-expectations)
      - [6.1.1. Proactive Communication](#611-proactive-communication)
      - [6.1.2. Integrating Security into Requirements](#612-integrating-security-into-requirements)
    - [6.2. Threat Modeling as a Collaborative Practice](#62-threat-modeling-as-a-collaborative-practice)
    - [6.3. Managing Flexibility and Control](#63-managing-flexibility-and-control)
    - [6.4. Resilient Coding and System Resilience](#64-resilient-coding-and-system-resilience)
    - [6.5. Dependency Management](#65-dependency-management)
  - [7. Roles and Responsibilities in SSEM Adoption](#7-roles-and-responsibilities-in-ssem-adoption)
    - [7.0. Application Security's Role](#70-application-securitys-role)
    - [7.1. Empowering Senior Software Engineers](#71-empowering-senior-software-engineers)
    - [7.2. Guiding Developing Software Engineers](#72-guiding-developing-software-engineers)
    - [7.3. The Role of Product Owners and Managers](#73-the-role-of-product-owners-and-managers)
  - [8. Evolution and Adoption of FIASSE](#8-evolution-and-adoption-of-fiasse)
    - [8.1. Adapting to Emerging Software Engineering Trends](#81-adapting-to-emerging-software-engineering-trends)
      - [8.1.1. AI-Driven Software Development](#811-ai-driven-software-development)
      - [8.1.2. Low-Code and No-Code Platforms](#812-low-code-and-no-code-platforms)
      - [8.1.3. Cloud-Native and Serverless Architectures](#813-cloud-native-and-serverless-architectures)
      - [8.1.4. Continuous Security Engineering](#814-continuous-security-engineering)
      - [8.1.5. Quantum-Resistant Cryptography](#815-quantum-resistant-cryptography)
      - [8.1.6. Ethical AI and Security Governance](#816-ethical-ai-and-security-governance)
    - [8.2. Organizational Adoption Strategies](#82-organizational-adoption-strategies)
  - [9. Security Considerations](#9-security-considerations)
  - [10. Conclusion](#10-conclusion)
  - [11. References](#11-references)
  - [12. Author's Address](#12-authors-address)

## 1. Introduction

### 1.1. The Application Security Challenge

Organizations invest significantly in secure coding initiatives and security testing tools, yet often do not observe commensurate outcomes in application security (AppSec). Tangible progress can feel slow, and friction between AppSec and Development teams is a common impediment.  The advent of Generative AI tools for code generation, while powerful, also presents a risk of amplifying past security mistakes or introducing new, subtle vulnerabilities if not guided by sound engineering principles. Ensuring that AI-generated code is inherently securable is a new facet of this challenge. A fundamental question arises: how can development teams consistently create securable code if they are not deeply versed in security expertise?
Furthermore, many well-intentioned strategies, including the prevalent "shift left" movement, have often yielded disappointing results in practice, failing to impact the software produced.

### 1.2. A Developer-Centric Security Paradigm

This document advocates for a developer-centric security paradigm. Rather than expecting software engineers to adopt a penetration tester's mindset (a distinction further explored in Section 2.4), this approach emphasizes empowering developers. While leveraging sound software engineering principles is foundational, it is complemented by clear security requirements and robust assurance activities. With these elements effectively integrated, engineers can build securable systems as a natural part of their discipline. The common misconception is that the gap between security and development is an issue. This document makes the case that the gap is not a problem; rather, it is the lack of understanding of how software is produced and alignment with those processes.

### 1.3. Document Purpose and Scope

The purpose of this document is to introduce the Framework for Integrating Application Security into Software Engineering (FIASSE) and its core component, the Securable Software Engineering Model (SSEM). FIASSE provides the overarching strategic approach and processes for integrating security into software engineering. SSEM, as a model within FIASSE, offers a common design language and a set of principles to guide the creation of secure software, aligning AppSec objectives with business goals.

You will notice the proliferent use of the word 'securable' throughout this document to emphasize the dynamic nature of software security. see Section 2.1 for a detailed explanation of this term. Application Security must align with the business objectives for software development because of this dynamic nature.

This document will cover:

- Foundational principles underpinning FIASSE and SSEM.
- The core attributes of securable software as defined by SSEM.
- Strategies for integrating FIASSE (and SSEM) into existing development processes.
- Common pitfalls in AppSec and how FIASSE helps to avoid them.
- Practical guidance for developers to build securable code.
- The roles of different engineering personnel in adopting FIASSE.
- The potential evolution of FIASSE in response to emerging software engineering trends and strategies for organizational adoption.

This document is intended for AppSec professionals, software engineers, engineering managers, and anyone involved in the Software Development Lifecycle (SDLC) who seeks to improve application security outcomes.

## 2. Foundational Principles

### 2.1. The Securable Paradigm: No Static Secure State

The deliberate and consistent use of the term "securable" throughout this document reflects a fundamental principle: there is no static state of "secure" for software systems. Unlike traditional security approaches that may imply a binary secure/insecure classification, the concept of "securable" acknowledges that security is an ongoing, dynamic process rather than a fixed destination.

Software exists in a constantly evolving threat landscape where new vulnerabilities emerge, attack vectors evolve, business requirements change, and dependencies change. What may be considered secure today could become vulnerable tomorrow due to newly discovered exploits, changes in the threat environment, or modifications to the system itself. This reality necessitates a shift from pursuing an illusory state of perfect security to building software with inherent qualities that enable it to adapt to and withstand evolving threats.

Consider the difference between a house that is currently locked (a static 'secure' state) and a house built with strong foundations, high-quality locks, a well-maintained alarm system, and clear lines of sight ('securable'). The 'securable' house is designed with inherent qualities that allow it to be made and remain secure against evolving threats over time, even if a window is momentarily left open or a new lock-picking technique emerges. FIASSE focuses on embedding these inherent 'securable' qualities into software architecture and code.

The "securable" paradigm emphasizes:

- **Adaptive Resilience**: Software should be designed with the capability to respond to and recover from security events.
- **Evolutionary Security**: Security measures must evolve alongside the software and its operating environment.
- **Continuous Improvement**: Security is an iterative process that requires ongoing attention and refinement.
- **Business Alignment**: Security efforts must align with business objectives and risk tolerance, not pursue security for its own sake.

This approach aligns security practices with the reality of software development, where systems are continuously modified, extended, and deployed in changing environments. By focusing on building securable software, development teams can create systems that maintain their protective qualities even as they evolve, rather than systems that become brittle and insecure when changed.

### 2.2. Resiliently Add Computing Value

The primary directive of software engineering in a business context is to create valuable code in a way that is robust enough to withstand change, stress, and attack. Expressed concisely: "Resiliently add computing value". This means creating software that not only meets functional requirements but also possesses securable qualities — such as those defined by SSEM like high Analyzability, Modifiability, and Testability — that allow it to adapt, persist, and maintain its integrity over time and under various conditions. These qualities enable it to withstand operational failures, accommodate evolving business needs, and resist security threats more effectively. Software Engineering refers to the broader discipline of designing, developing, and maintaining software in a systematic and organized way [Wikipedia-SE].

This principle underscores the idea that security is not an add-on but an intrinsic component of well-engineered software, contributing directly to its ability to deliver value reliably and sustainably.

### 2.3. Security Mission: Reducing Material Impact

The core mission of cybersecurity, as articulated by Rick Howard in "Cyber Security First Principles," is to "Reduce the probability of material impact of a cyber event". Complete elimination of breaches, while an ideal, is often not a functional business goal. Security strategies MUST, therefore, align with overarching business objectives. This requires a balanced approach. While formal buy-in and metrics are necessary, AppSec's role extends to enabling Development teams to meet security expectations and pass security assessments. Effectively reducing the chance of a successful attack and minimizing potential damage.

### 2.4. Mindset Convergence: Hacker vs. Engineer

The perspective that all programmers should put security first, think like attackers, or also be pentesters, to eliminate security problems overlooks a critical distinction. While understanding how systems can be compromised is valuable, it does not inherently translate into the knowledge of how to build them securely. It is unreasonable to expect business value to be a secondary concern. There is a significant difference between identifying a vulnerability and implementing a robust, scalable software engineering solution. This also complements the reality that line-level fixing does not scale effectively.

Additionally, the two mindsets do not represent a gap. Instead, they are complementary disciplines used to conduct business. Just as we don't talk about the complementary roles of Accounting and Operations as a gap, we should not view the roles of Security and Development in this way.

### 2.5. Aligning Security with Development

True alignment between security and development requires a return to first principles. Instead of imposing security-centric jargon and processes that may seem alien to developers, SSEM advocates for using well-established Software Engineering terms to describe securable code attributes (the SSEM properties like Analyzability, Modifiability, Testability, Confidentiality, etc.). This fosters understanding and empowers developers to address security confidently without years of dedicated security experience. The goal is to instill confidence in developers, enabling them to recognize these securable attributes in existing code — for example, identifying highly Analyzable code by its clarity and ease of understanding or low Cyclomatic complexity. Or by recognizing Testable code by the simplicity of writing unit tests for it. Security cultivates confidence by understand what building securable software entails from an engineering perspective. As will be discussed, this also requires specific participation from AppSec professionals in the early stages of the Software Development Lifecycle (SDLC), particularly during requirements gathering and feature planning.

## 3. The Securable Software Engineering Model (SSEM)

### 3.1. Overview and Objectives

The Securable Software Engineering Model (SSEM) is centered on providing a design language that uses established software engineering terms to define the core attributes that make software "securable" as conceptualized in this document (see Section 2.1). These attributes, detailed in Section 3.2, allow SSEM to abstract security away from specialized jargon or exploit-centric views, enabling software engineers to confidently integrate security considerations as a natural part of their development work.

A key objective of SSEM, facilitated by this design language, is to shift the conversation regarding software security. Instead of a binary "Is it secure?" assessment, the focus moves to a more nuanced and actionable question: "Do we meet our defined goals for this particular securable attribute?" (The broader impact and application of SSEM as a design language is detailed in Section 3.3).

SSEM is further designed to:

- Account for the iterative nature of software development and agile methodologies.
- Serve as a mental model, a checklist, or a means to set clear expectations for securable design.

Here are the core attributes of SSEM are grouped into three primary categories, each representing a fundamental aspect of securable software:

| **Maintainability** | **Trustworthiness** | **Reliability** |
|:-----------------|:-----------------:|--------------:|
| Analyzability    | Confidentiality   | Availability  |
| Modifiability    | Accountability    | Integrity     |
| Testability      | Authenticity      | Resilience    |

SSEM is not a rigid framework but a flexible model that can adapt to various software engineering practices. It emphasizes the inherent qualities of well-engineered software that contribute directly to security, rather than prescribing specific security controls or processes. This allows it to scale effectively without requiring security to adopt toilsome or overly complex processes that may not align with the development team's workflow.

### 3.2. Core Securable Attributes

SSEM identifies several fundamental and universal attributes that are the building blocks of securable software—software designed with the inherent qualities needed to adapt and maintain its security posture in an evolving landscape (as discussed in Section 2.1). These attributes are not merely abstract concepts but represent tangible characteristics of well-engineered software that directly contribute to its overall security and resilience. They are grouped into three primary categories: Maintainability, Trustworthiness, and Reliability, each encompassing specific sub-attributes detailed below. By focusing on these, developers can proactively build systems that are easier to secure and keep secure over time.

#### 3.2.1. Maintainability

Definition: Maintainability is the "degree of effectiveness and efficiency with which a product or system can be modified by the intended maintainers" (ISO/IEC 25010:2011). In the context of SSEM, this means software can be evolved, corrected, and adapted to new threats or requirements without undue effort or introducing new vulnerabilities. This focus on ease of modification and adaptation is central to building securable software, as it directly supports the ability to respond to the dynamic threat landscape and evolving security needs outlined in Section 2.1. It encompasses the following sub-attributes:

##### 3.2.1.1. Analyzability

Definition: “The degree of effectiveness and efficiency with which it is possible to assess the impact on a product or system of an intended change to one or more of its parts, or to diagnose a product for deficiencies or causes of failures, or to identify parts to be modified” (ISO 25010, §4.2.7.3). This means the ability to find the cause of a behavior within the code. From a security standpoint, code must be understandable to find and fix vulnerabilities. Analyzability directly correlates to the speed and efficiency of vulnerability remediation.

Contributing Factors:

- Volume (Lines of Code - LoC): Overall size of the codebase.
- Duplication: Percentage of duplicated code.
- Unit Size (e.g., mLoC/cLoC): Lines of code per class, method, or block.
- Unit Complexity (e.g., Cyclomatic Complexity): Degree of complexity within a code unit.
- Component Balance: The distribution and size uniformity of top-level components.

##### 3.2.1.2. Modifiability

Definition: “The degree to which a product or system can be effectively and efficiently modified without introducing defects or degrading existing product quality” (ISO 25010, §4.2.7.4). This means the ability to modify code without breaking existing functionality or introducing new vulnerabilities.

Contributing Factors:

- Duplication: As above, duplicated code increases the risk of inconsistent changes.
- Unit Complexity: Complex units are harder to modify safely.
- Module Coupling: The number of incoming dependencies for modules; high coupling can lead to cascading changes and unintended consequences.

Modifiability is particularly important for security because it allows for rapid response to newly discovered vulnerabilities or changing security requirements. It enables teams to adapt their codebase without extensive rework, which is crucial in a fast-paced development environment.

##### 3.2.1.3. Testability

Definition: “The degree of effectiveness and efficiency with which test criteria can be established for a system, product or component and tests can be performed to determine whether those criteria have been met” (ISO 25010, §4.2.7.5). This is the ability to write a test for a piece of code without needing to change the code under test. Effective testing is crucial for verifying security controls and detecting regressions.

Contributing Factors:

- Volume: Larger codebases can be more challenging to test comprehensively.
- Unit Complexity: Complex units are more difficult to test thoroughly.
- Component Independence: The percentage of code in modules with no incoming dependencies from modules in other top-level components; higher independence facilitates isolated testing.
- Unit Coupling: The number of incoming dependencies for units; high coupling can complicate testing by introducing dependencies that must also be tested.

Testability is essential for security because it allows teams to verify that security controls are functioning as intended and that changes do not introduce new vulnerabilities. It also supports the development of automated tests, which can be run continuously. Because of this, it correlates to the scaling of Security Assurance.

#### 3.2.2. Trustworthiness

Definition: Trustworthiness is "the degree to which a system (including all its components and procedures) can be expected to achieve a set of requirements, such as security requirements" (RFC 4949). A trustworthy system operates within defined levels of trust and meets specified security properties. The FIASSE approach differs from a security-controls-centric view by focusing on the inherent qualities of the code that enable trustworthiness. 

Trustworthiness is foundational to securable software. It requires a coordinated effort to ensure that the software consistently achieves its security goals. To achieve this, strong architectural design and style are essential. This includes defining clear trust boundaries, and establishing areas of the codebase that are expected to be more flexible.

Key attributes contributing to trustworthiness include:

##### 3.2.2.1. Confidentiality

Definition: "The property that data is not disclosed to system entities unless they have been authorized to know the data" (RFC 4949). This ensures that sensitive information is protected from unauthorized access.

FIASSE emphasizes confidentiality as a fundamental attribute achieved by designing software with inherent qualities that protect sensitive information, rather than relying solely on overlaid security controls.

##### 3.2.2.2. Accountability

Definition: "The property of a system or system resource that ensures that the actions of a system entity may be traced uniquely to that entity" (RFC 4949). This involves managing principals and their access, enabling the attribution of actions to specific users or processes, which is crucial for auditing and incident response.

Achieving accountability relies on robust methods for managing principals and their access rights. While it leverages strategies common to non-repudiation, such as comprehensive logging and secure authentication, its core focus is the unique and verifiable attribution of every system action to a specific entity. This is essential for effective auditing and incident response.

###### 3.2.2.2.1 Non-repudiation

Definition: The "ability to prove the occurrence of a claimed event or action and its originating entities" (ISO/IEC 27000:2018). This prevents entities from falsely denying having performed an action or sent a message.

Focusing on non-repudiation means ensuring that actions taken by users or systems can be traced back to their origin. This involves implementing logging, auditing, and secure authentication. These strategies provide transparency to support the maintenance and troubleshooting of the system, and they also enable accountability and authenticity.

##### 3.2.2.3. Authenticity

Definition: "The property that an entity is what it claims to be" (ISO/IEC 27000:2018). This ensures that users, systems, or information are genuine and can be verified.

Focusing on authenticity means ensuring that the entities involved in a transaction or communication are who they claim to be. This involves implementing strategies such as digital signatures, certificates, and secure authentication methods. These strategies provide assurance that the entities involved in a transaction or communication are who they claim to be, which is essential for maintaining trust in the system.

#### 3.2.3. Reliability

Definition: Reliability is the "degree to which a system, product or component performs specified functions under specified conditions for a specified period of time" (ISO/IEC 25010:2011). In SSEM, this means the software operates consistently and predictably, even under adverse conditions or when facing unexpected inputs or attacks. It includes the following attributes:

##### 3.2.3.1. Availability

Definition: "The property of a system or a system resource being accessible and usable upon demand by an authorized system entity, according to performance specifications for the system" (RFC 4949). This ensures that the system is operational and accessible when needed.

For security this means that the system is designed to be resilient against attacks like Distributed Denial of Service (DDoS) attacks. It also means that the system can recover quickly from failures or disruptions, ensuring that it remains accessible to authorized users.

##### 3.2.3.2. Integrity

Definition: Encompasses both data integrity, "the property that data has not been changed, destroyed, or lost in an unauthorized or accidental manner," and system integrity, where a system "performs its intended function in an unimpaired manner free from unauthorized manipulation" (RFC 4949). This ensures the accuracy, completeness, and soundness of data and system operations.

For security this means implementing measures such as cryptographic hashing, checksums, and access controls to prevent unauthorized modification or corruption of data. Emphasizing this attribute in a fundamental way ensures that the system can be trusted holisticly, not just in isolated components.

This approach recognizes that integrity is not just about preventing unauthorized changes but also about ensuring that the system operates correctly and consistently, even in the face of potential threats or failures.

##### 3.2.3.3. Fault Tolerance

Definition: "The ability of a system to continue to operate correctly even though a component has failed" (RFC 4949). This allows the system to withstand partial failures without complete breakdown.

Focusing on this as a fundamental attribute means it is not just for specific features but for the system as a whole. It involves designing the system to handle errors gracefully, recover from failures, and maintain functionality even when parts of the system are compromised or unavailable.

##### 3.2.3.4. Resilience

Definition: "The ability of a system to: (a) continue to operate during and after a failure of some part of the system (i.e., provide a degree of fault tolerance); and (b) recover from the failure and restore full operations" (RFC 4949). This also aligns with the concept of an application's ability to continue running predictably, even under unfavorable circumstances or load (as noted in Section 6.4).

Strategies for resilience include:

- Coding Defensively: Writing code that anticipates input outside the expected bounds and ignores those inputs rather than failing.
- Predictable code execution: Ensuring that the code behaves consistently under various conditions.
- Strong trust boundaries: Clearly defining areas of the codebase that exert strictly controlled execution.

### 3.3 SSEM as a Design Language

By defining these attributes using established software engineering terminology, SSEM provides a common design language. This enables developers to discuss, reason about, and implement security considerations using concepts already familiar to them. It shifts the focus from myopic treatment of vulnerabilities to cohesive creation of software with inherent securable qualities.

This design language plays a crucial role in creating a cohesive product. It complements architecture to help Development understand how principles and key qualities are to be understood and applied across the codebase. This guides the Software Engineer to make the countless smaller decisions that make while writing code.

A design language fosters a shared understanding around specific technical values. This can bring together a culture of quality made up of diversely inclined professionals to focus on these common goals and ideals. This is achieved by the shift in conversations around security as mentioned in Section 3.1, where the focus is on meeting goals for specific attributes rather than binary security assessments. This cultural alignment can strongly influence the product's internal structure to support these technical values. This is contrast with the traditional approach of find-and-fix monotony.

### 3.4 Measuring SSEM Attributes

Measuring the attributes defined by SSEM is essential to quantify and evaluate the securable qualities of software. This section outlines approaches for measuring each of the core attributes: Maintainability, Trustworthiness, and Reliability. These measurements provide actionable insights to guide developers in enhancing the securability of their software.

#### 3.4.1. Measuring Maintainability

##### 3.4.1.1. Analyzability

- **Quantitative:**
  - **Volume (Lines of Code - LoC):** Tracked per module/system. Lower LoC for a given functionality can indicate better analyzability.
  - **Duplication Percentage:** Measured by static analysis tools (e.g., SonarQube, PMD). Lower is better.
  - **Unit Size (e.g., mLoC/cLoC):** Average lines of code per method or class. Excessively large units are harder to analyze.
  - **Unit Complexity (e.g., Cyclomatic Complexity):** Measured by static analysis tools. Lower complexity per unit is generally better.
  - **Comment Density/Quality:** Ratio of comment lines to code lines, or qualitative review of comment usefulness.
- **Qualitative/Process-based:**
  - **Time to Understand (TTU):** Average time it takes a developer unfamiliar with a code section to understand its purpose and flow for a specific task (e.g., bug fix).
  - **Developer Surveys:** Periodically ask developers to rate the analyzability of modules they work with.

##### 3.4.1.2. Modifiability

- **Quantitative:**
  - **Module Coupling (Afferent/Efferent):** Number of incoming (afferent) and outgoing (efferent) dependencies for modules. Lower afferent coupling for a module often means it's easier to change without impacting many other parts.
  - **Change Impact Size:** Number of files/modules typically affected by a common type of change. Smaller is better.
  - **Regression Rate:** Percentage of changes that introduce new defects. Lower is better.
- **Qualitative/Process-based:**
  - **Ease of Change Assessment:** During code reviews, assess how easy it would be to make a hypothetical related change.
  - **Time to Implement Change:** Average time to implement standard types of modifications or feature enhancements.

##### 3.4.1.3. Testability

- **Quantitative:**
  - **Code Coverage:** Percentage of code covered by automated tests (unit, integration). Higher is generally better.
  - **Unit Test Density:** Number of unit tests per KLoC or per class/module.
  - **Mocking/Stubbing Complexity:** Difficulty or amount of setup required to isolate units for testing.
- **Qualitative/Process-based:**
  - **Ease of Writing Tests:** Developer feedback on how easy it is to write meaningful tests for new or existing code.
  - **Test Execution Time:** While not a direct measure of testability, excessively long test suite runs can disincentivize testing.

#### 3.4.2. Measuring Trustworthiness

##### 3.4.2.1. Confidentiality

- **Quantitative:**
  - **Number of Identified Data Leaks:** From penetration tests, code reviews, or incidents.
  - **Access Control Violations:** Number of logged unauthorized access attempts (prevented or successful).
- **Qualitative/Process-based:**
  - **Data Classification Adherence:** Review of how well data is classified and if protections align with classification.
  - **Principle of Least Privilege Review:** Assessment of whether components and users only have necessary permissions.
  - **Effectiveness of Encryption:** Review of encryption algorithms used, key management practices.

##### 3.4.2.2. Accountability

- **Quantitative:**
  - **Audit Log Coverage:** Percentage of critical system actions that are logged with sufficient detail.
  - **Traceability Success Rate:** Percentage of audited actions that can be uniquely traced to an entity.
- **Qualitative/Process-based:**
  - **Audit Log Review Findings:** Results from periodic reviews of audit logs for completeness and usefulness.
  - **Non-repudiation Strength:** Assessment of the strength of evidence linking actions to entities (e.g., use of digital signatures).

##### 3.4.2.3. Authenticity

- **Quantitative:**
  - **Authentication Failures:** Number of failed login attempts (can indicate brute-forcing or issues).
  - **Use of Strong Authentication:** Percentage of authentication points using multi-factor authentication or strong credential types.
- **Qualitative/Process-based:**
  - **Verification of Identities:** Review of processes for verifying user and system identities.
  - **Integrity of Authentication Mechanisms:** Assessment of the security of authentication protocols and implementations.

#### 3.4.3. Measuring Reliability

##### 3.4.3.1. Availability

- **Quantitative:**
  - **Uptime Percentage:** (e.g., 99.99%).
  - **Mean Time Between Failures (MTBF).**
  - **Mean Time To Recovery (MTTR).**
- **Qualitative/Process-based:**
  - **Redundancy Review:** Assessment of system redundancy for critical components.
  - **Disaster Recovery Test Results.**

##### 3.4.3.2. Integrity

- **Quantitative:**
  - **Number of Data Corruption Incidents.**
  - **Checksum/Hash Validation Success Rate:** For data at rest and in transit.
- **Qualitative/Process-based:**
  - **Input Validation Effectiveness:** Review of input validation mechanisms at trust boundaries.
  - **System File Integrity Monitoring Alerts.**

##### 3.4.3.3. Fault Tolerance

- **Quantitative:**
  - **Service Degradation under Failure:** Measure of performance or functionality loss when components fail.
- **Qualitative/Process-based:**
  - **Chaos Engineering Results:** System behavior during controlled failure experiments.
  - **Single Point of Failure (SPOF) Analysis:** Number of identified SPOFs.
  - **Effectiveness of Error Handling:** Review of how gracefully the system handles unexpected errors.

##### 3.4.3.4. Resilience

- **Quantitative:**
  - **Recovery Time Objective (RTO) Adherence:** How often RTOs are met after an incident.
  - **Performance Under Stress:** System performance metrics during load testing or simulated attacks (e.g., DDoS).
- **Qualitative/Process-based:**
  - **Defensive Coding Practices Review:** Assessment of code for practices like proper input validation, output encoding, and robust error handling.
  - **Incident Response Plan Effectiveness:** Review of how well the system and team recover from security incidents or operational failures.

## 4. Integrating SSEM into Development Strategy

### 4.1. Applying SSEM to Dependency Management

SSEM principles are not limited to first-party code; they are equally critical when managing software dependencies. Proactively applying SSEM attributes to the selection, integration, and maintenance of third-party libraries is essential for building securable systems. Detailed practical guidance on dependency management through the lens of SSEM is provided in Section 6.5.

### 4.2. Natively Extending Development Processes

A key principle for reducing friction and effectively preparing development teams is to integrate security into existing development workflows rather than imposing separate, external security gates. This involves understanding and extending current practices.

Examples include:

- Architecture review: Consider business concerns to emphasize security implications. (e.g., DDOS protection to preserve business integrity).
- Predefined checklists: Develop flexible checklists that incorporate SSEM attributes and security considerations that can be used in various contexts.
- Usability: Framing usability not just as aesthetics but as building trust from a security standpoint (e.g., clear error messages, intuitive permissions management).

### 4.3. The Role of Merge/Pull Request Reviews

While software engineering may lack formal licensing like other engineering disciplines, the merge review (or pull request review) process serves as a crucial point for mentoring, guidance, and validation. For security, this is where securable code review can scale effectively. It acts as an agile training ground where developers learn from peers and receive feedback in a constructive environment. SSEM attributes can provide a concrete basis for these reviews.

The teams should be careful to avoid introducing unnecessary complexity or friction into the review process. This means that the merge review is used as guard rails and not as a gate. The goal is to grow the FIASSE mindset within the team, not to create a negative experience for the developers.

In the future guidance for merge reviews, we will explore how to effectively integrate SSEM attributes into the review process in detail.

### 4.4. Early Integration: Planning and Requirements

FIASSE advocates for setting expectations at the earliest stages of the development, particularly during planning and requirements definition. This ensures security is a foundational design aspect rather than an afterthought. Detailed methods for integrating security into requirements, such as defining Threat Scenarios and Security Acceptance Criteria, are discussed in Section 6.1.2.

## 5. Addressing Common AppSec Anti-Patterns

### 5.1. The "Shoveling Left" Phenomenon

"Shoveling Left" is defined as the practice of supplying impractical information to developers and leaving the responsibility on them to make sense of it. This anti-pattern often manifests in how vulnerabilities are reported, training is conducted, and testing results are delivered. It can undermine AppSec's credibility and lead to developer disengagement.

#### 5.1.1. Ineffective Vulnerability Reporting

A prime example of "Shoveling Left" is dumping raw findings from security scanning tools directly into the development team's backlog. This approach often lacks context, prioritization, and actionable guidance. While initial progress might be observed, momentum is typically lost, and issues may reappear (the "whack-a-mole" effect). Raw tool output, on its own, is rarely impactful enough to drive sustained improvement.

To avoid this, AppSec SHOULD:

1. Focus on True Positives: Validate findings to ensure accuracy.
2. Identify Root Causes: Address systemic issues rather than just symptoms.
3. Prioritize by Impact: Focus on issues that are plentiful or affect sensitive resources.
4. Collaborate on Solutions: Work with development to formulate wide impact solutions instead of just line-level fixes.
5. Verify Fixes: Ensure remediation is effective and consider automated regression tests.

#### 5.1.2. Pitfalls of Exploit-First Training

Security training for developers that primarily emphasizes exploitation techniques ("learn the hack to stop the attack") is another manifestation of "Shoveling Left." As discussed in Section 2.4, understanding how to compromise a system (the 'hacker' mindset) is distinct from knowing how to engineer a robust and securable one (the 'engineer' mindset).

This type of training often fails because it does not equip developers with the engineering principles needed for their daily tasks, nor does it teach them how to identify or build code with inherently securable qualities (as defined by SSEM). Consequently, developers might gain a superficial understanding of risks without the practical knowledge to implement effective, systemic preventative measures. This can lead to a false sense of security and does little to foster the proactive, engineering-focused question of "What can go wrong?" in a way that leads to better design and implementation.

### 5.2. Strategic Use of Security Output

While scanning and testing tools are valuable for AppSec to understand the current security posture, their output MUST be used strategically. It should not be assumed that security requirements are implicit or that developers should be blamed for missing controls if clear expectations were not set. Productive software engineers have a structured workflow designed to deliver value. Any disruption of this workflow can lead to degraded software quality and the flaws that Application Security is trying to prevent.

This is also why fix requests should never circumvent the processes that software engineers rely on. Misunderstandings and mistakes result from bypassing established workflows. Therefore AppSec should not expect developers to act on security findings without clear, actionable information and the opportunity to properly execute their workflow.

## 6. Practical Guidance for Secure Software Development

### 6.1. Establishing Clear Expectations

Clear expectations are foundational to building securable products. AppSec can maximize its impact by setting these expectations effectively. This requires AppSec's alignment with the business processes involved in software development.

#### 6.1.1. Proactive Communication

Basic communication is essential. Development teams should be informed about new testing initiatives or security programs pertaining to the product they maintain. Demonstrating tools to interested senior developers can foster collaboration and identify key contacts for strategic collaboration efforts. Regular synchronization points can help offer support and maintain momentum. Soft skills are important for Application Security professionals to be effective in their role.

#### 6.1.2. Integrating Security into Requirements

Active AppSec participation in formal requirements gathering is crucial. This shifts security from a post-development review or audit to an integral component of the product, aligning it with productivity rather than being perceived as a gate.

Key methods include:

- Threat Scenarios: Describing potential misuse cases or attack paths relevant to the feature being developed. This helps identify necessary controls.
- Security Acceptance Criteria: Defining specific, testable conditions that a feature must meet to be considered secure. These criteria allow QA to perform security testing by verifying requirements.

By embedding security into foundational design decisions via requirements, attributes like Trustworthiness, Integrity, and Fault Tolerance are more effectively realized. This approach allows Development teams to address security concerns as part of their standard workflow, making requirements an often underutilized yet powerful tool for security.

### 6.2. Threat Modeling as a Collaborative Practice

Threat modeling is a valuable team activity, ideally performed early in the development process, similar to requirements gathering. Even a simple framework, such as the "Four Question Framework" (What are we building? What can go wrong? What are we going to do about it? Did we do a good job?), can highlight areas needing more detailed design or specific security requirements. Threat modeling can be organically integrated with the FIASSE mindset by simply asking "What can go wrong?" at any point in the process.

A key concept taken from threat modeling is the identification of **trust boundaries**. These are points in the system where data passes between entities with different levels of trust (e.g., user to application, application to database, service to service). Trust boundaries require heightened control over data and process execution.

### 6.3. Managing Flexibility and Control

Software engineers often value flexibility in code, as it can facilitate feature implementation and bug fixing. Attackers, however, seek uncontrolled flexibility as a means to force the application to deviate from intended behavior.

The issue is not flexibility itself, but the lack of appropriate control, especially at trust boundaries. An example of uncontrolled flexibility might be a function capable of executing arbitrary query statements with arbitrary parameters without restriction. Control is essential to ensure trustworthy execution, maintain system Integrity, and support Fault Tolerance. While flexibility is necessary for Maintainability.

Think of trust boundaries like the hard candy shell of a jellybean: the soft, flexible interior represents the bulk of the application's logic, while the hard shell represents the critical points where external data or untrusted operations are carefully controlled. Just as the candy shell protects the jellybean's interior, well defined trust boundaries protect the core application from potentially harmful external influences. Defining and communicating these boundaries during the design phase makes it clear which areas of code are responsible for tight control, allowing developers to focus their efforts on maintaining the integrity and trustworthiness of these critical interfaces.

### 6.4. Resilient Coding and System Resilience

Resilience refers to an application's ability to continue running predictably, even under unfavorable circumstances or load. Tactical resilience is achieved through **defensive coding** practices that promote predictable execution.

This drives the need for concrete developer actions such as:

- Strong typing to ensure data is usable in the intended way.
- Filtering and validating all input at trust boundaries. Input validation ensures that data conforms to expected formats, types, lengths, and ranges before processing.
- Properly escaping and encoding all output destined for other systems or interpreters (exiting trust boundaries). This prevents injection attacks by ensuring that data is treated as data, not executable code.

These are verifiable actions that AppSec can assess.

### 6.5. Dependency Management

Dependency management starts when a library is introduced to the system, or even earlier if possible. The library should be evaluated for being fit to support your system and its values. This is a key aspect of the FIASSE mindset, which emphasizes the importance of understanding the implications of dependencies on the overall system architecture and security posture.

Applying SSEM principles proactively to dependency selection and management, beyond merely scanning for known vulnerabilities, is crucial. This involves considering:

- **Analyzability**: Thoroughly understand each dependency's full scope, including its transitive dependencies, its specific purpose within the application, and its potential attack surface. Maintain a clear inventory and a documented rationale for every included dependency.
- **Modifiability**: Design systems with loosely coupled dependencies to facilitate easier updates, patching, or replacement if a vulnerability is discovered, a dependency becomes obsolete, or a more secure alternative is identified. This aligns with architectural modifiability.
- **Testability**: Ensure that dependencies can be effectively managed during testing (e.g., through mocking, stubbing, or version pinning) and that their integration points are themselves robustly testable.
- **Trustworthiness (Authenticity and Integrity)**: Implement processes to verify the source and integrity of dependencies (e.g., using signed packages, checksums, and trusted repositories) before their integration into the codebase.
- **Reliability**: Assess how a dependency's failure modes (e.g., unavailability, performance degradation, security compromise) could impact the overall system's reliability and resilience, and subsequently plan appropriate mitigations.

Not all code that is shared is intended for reuse in systems that need to be resilient. Once FIASSE has been adopted, potential dependencies can be evaluated against the values of the culture it aims to create, ensuring alignment with these SSEM attributes.

Regularly updating software dependencies is a fundamental tactic for maintaining system resilience. Updates often include fixes for known bugs, including security vulnerabilities. This should be a routine process, integrated into sprints or regular maintenance cycles.

Further key considerations for dependency management include:

- Avoid unnecessary dependencies. Each dependency introduces the need for additional maintenance.
- If no direct update fixes a known flaw in a dependency, further analysis is required to identify mitigation strategies (e.g., compensating controls, forking and patching, or reimplementation).
- Organizations should have a clear policy regarding the use and maintenance of open-source dependencies, including processes for addressing vulnerabilities found within them.
- Reliance solely on CVE (Common Vulnerabilities and Exposures) reporting may not be sufficient. A thorough analysis of dependencies and their transitive "baggage" is recommended.

## 7. Roles and Responsibilities in SSEM Adoption

Understanding different development roles is useful for tailoring guidance and effectively integrating SSEM.

### 7.0. Application Security's Role

It should be understood in early stages of FIASSE adoption that Application Security's role in development is that of assurance. The only shared responsibility between AppSec and Development teams is the timely delivery of the end result. This ensures the focus of Software Engineers remains on building securable code through a self-governed process. AppSec is to provide guidance through participation in development activities like design and requirements. This establishes the guardrails for development to operate in as intended. Admittedly, AppSec is not responsible for development's level of adherence to the architecure of the system or feature requirements.

Therefore security metrics (those derived from Application Security Testing tools and pentests) are a measure of the effective participation of AppSec in the development process, not a measure of Software Engineering's adherence to security. The overall security posture of an application reflects how well expectations are set. This is a key distinction that allows AppSec to focus on providing value through requirements, design, and assurance rather than policing or micromanaging development teams.

If the posture stays stagnant over time, adjustments to development culture and/or leadership are necessary. AppSec can encourage culture change by promoting FIASSE and sponsoring activities including continued education. It can be difficult to accept the limits of AppSec's influence, but it is essential to recognize that the responsibility for balancing business value creation with security needs ultimately lies with the development team as a whole.

By spending valuable time in design activities, AppSec can guide larger numbers of developers that are adhering to the principals of FIASSE. It will also foster a culture of shared responsibility for security, where developers are empowered to take ownership of their code while having the support and guidance of AppSec professionals following established software engineering practices.

### 7.1. Empowering Senior Software Engineers

Experienced, top-tier software engineers are critical to the success of any AppSec program. AppSec professionals should work collaboratively *with* these engineers in design activities.

Senior engineers should be empowered to:

- Ask 'What can go wrong?' and consider those issues at every stage of development.
- Drive the creation of Security Requirements, Acceptance Criteria, and Threat Scenarios.
- Lead merge reviews, emphasizing SSEM attributes, software engineering principles.
- Champion and schedule regular dependency maintenance.
- Mentor peers as well as less experienced developers.
- Liaise with AppSec teams to ensure smooth security alignment with software engineering practices.

### 7.2. Guiding Developing Software Engineers

Software engineers who are still gaining experience (aka. Jr Programmers, Artisan or Ancillary Coders) benefit greatly from mental checklists like SSEM and the methodologies FIASSE describes. They may not always intuitively know "What can go wrong?" but can learn through structured guidance, merge reviews, and pair programming.

These engineers should be encouraged to:

- Focus on becoming strong software engineers.
- Ask for clear Security Requirements, Acceptance Criteria, and Threat Scenarios.
- Be cautious about introducing new external dependencies without due diligence.
- Actively seek code reviews from senior team members.
- Write unit tests that cover exceptional conditions and out-of-bounds values.
- Learn and apply defensive coding techniques, particularly input validation and output encoding.
- Be mindful of trust boundaries in the code they write.
- Seek understanding of FIASSE and SSEM to learn how fundamental principles effect outcomes.

### 7.3. The Role of Product Owners and Managers

Product Owners and Managers play a crucial role in ensuring that FIASSE activities are given enough space in the product development lifecycle. They should:

- Advocate for FIASSE considerations during the planning and prioritization of features.
- Collaborate with AppSec and Development teams to define clear expectations through user stories, threat scenarios, and acceptance criteria.
- Allocate time and resources for regular software engineering training and awareness programs around FIASSE.

## 8. Evolution and Adoption of FIASSE

### 8.1. Adapting to Emerging Software Engineering Trends

FIASSE is positioned to evolve alongside emerging trends in software engineering, ensuring that security remains an integral component.

#### 8.1.1. AI-Driven Software Development

The increasing use of AI-powered tools, particularly Generative AI, for code generation, bug detection, code fixes and automated testing presents both significant opportunities and challenges for software security. While these tools can accelerate development, they also risk propagating insecure coding patterns or generating code that is difficult to analyze, modify, and test securely if not properly guided.

FIASSE is well-suited to address this by providing a framework for **Prompt Engineering for Securable Code**. This involves crafting prompts for Generative AI tools that explicitly or implicitly request code exhibiting FIASSE's core securable attributes:

- Analyzability in Prompts: Prompts can direct AI to generate code that is well-commented, uses clear and consistent naming conventions, adheres to established coding standards, and possesses a logical, understandable structure. For example, a prompt might specify, "Generate a Python function to parse CSV data, ensuring comprehensive comments for each logical step and adherence to PEP 8 style guidelines."
- Modifiability in Prompts: Prompts can guide AI to produce modular code with low coupling and high cohesion, clear interfaces, and an avoidance of duplicated logic. An example could be, "Develop a Java class for user authentication that is easily extensible for new authentication methods and avoids hardcoding configuration parameters."
- Testability in Prompts: Prompts can request the generation of code that is inherently testable, for instance, by asking for functions with clear inputs and outputs, minimal side effects, and even the co-generation of unit tests. For example, "Write a Go function to calculate X, and include unit tests covering valid inputs, invalid inputs, and edge cases."

Beyond these core attributes, prompts can also incorporate broader security considerations derived from FIASSE's principles:

- Requesting code that implements specific security controls (e.g., "Generate code to sanitize user input for predictable code execution.").
- Include security requirements and FIASSE attributes as part of the Product Requirements Document (prd.md).
- Include FIASSE attributes as part of the Acceptance Criteria Document (acd.md).
- Include FIASSE attributes as part of the code standards for generation (eg copilot-instructions.md).

Integrating FIASSE into prompt engineering aims to shift the output of AI code generators towards producing code that is not only functional but also inherently more securable from its inception. This proactive approach complements other AI-enhanced security practices.

#### 8.1.2. Low-Code and No-Code Platforms

As low-code and no-code development platforms become more prevalent, FIASSE principles can be adapted by:

- Establishing security guidelines based on FIASSE and tailored for citizen developers.
- Embedding automated security checks within these platforms.
- Ensuring that pre-built components and templates adhere to secure coding principles.

#### 8.1.3. Cloud-Native and Serverless Architectures

The shift towards microservices, containers, and serverless computing necessitates an emphasis within FIASSE on:

- Secure API design and robust authentication/authorization.
- Comprehensive Identity and Access Management (IAM) for distributed systems.
- Resilient architecture principles to mitigate cloud-specific threats.

#### 8.1.4. Continuous Security Engineering

FIASSE naturally aligns with Continuous Security Engineering philosophies by embedding security into CI/CD pipelines. Future adaptations will likely further strengthen this alignment through:

- Enhanced automation of security testing at various stages of the build and deployment process.
- Improved security observability for real-time monitoring and incident response.
- Continued development of developer-friendly security tooling that integrates seamlessly into their workflows.

#### 8.1.5. Quantum-Resistant Cryptography

As quantum computing capabilities advance, posing a threat to current cryptographic standards, FIASSE will incorporate guidance on:

- Transitioning to quantum-safe cryptographic algorithms.
- Secure key management strategies suitable for a post-quantum era.
- Resilient data protection that anticipate future cryptographic challenges.

#### 8.1.6. Ethical AI and Security Governance

With AI playing a larger role in software development, ethical considerations and robust governance become critical. FIASSE may evolve to include:

- Guidelines to ensure AI-generated code adheres to FIASSE principles and SSEM attributes.
- Guidance for governing AI-driven development processes using SSEM.

### 8.2. Organizational Adoption Strategies

Adopting FIASSE does not require a structured approach. However, organizations can benefit from a strategic implementation plan to ensure successful integration of FIASSE principles into their software development practices. Here are some recommended steps:

1. **Assess Current Practices:** Evaluate if the organization is open to adopting FIASSE principles and practices. This may involve discussions with key stakeholders and a review of existing workflows.
   - Identify existing security practices and how they align with SSEM attributes.
   - Determine the current level of understanding and acceptance of Software Engineering principles among development teams.
   - Assess the misalignments FIASSE can address.
2. **Integrate SSEM Terminology:** Deliberately incorporate SSEM attributes (Maintainability, Trustworthiness, Reliability) and their sub-attributes into existing developer documentation, coding standards, style guides, and training materials. This helps socialize the concepts and provides a common language for discussing and evaluating securability.
3. **Identify Key Influencers:** Identify senior software engineers and other key stakeholders who are able to internalize the framework and the principals. These individuals can champion FIASSE adoption. These individuals should have a strong understanding of software engineering.
4. **Educate and Train Teams:** Provide comprehensive training on FIASSE activities and SSEM attributes to Key Influencers. Introductory training should be role-specific and integrated into onboarding and continuous learning programs.
   - Development and AppSec should understand that FIASSE is meant to be discussed in the context of software engineering, not as a separate security initiative.
   - After the initial training, primary delivery of on-going training should be delivered in the context of merge reviews, architecture discussions, and requirements gathering. Leaders should be encouraged to bring FIASSE discussions into these activities.
5. **Foster Collaboration:** Promote regular collaboration between AppSec and Development teams. Discourage AppSec from simply reviewing items in isolation; instead, encourage AppSec to engage in Development activities such as requiremnts gathering.
6. **Continuously Monitor and Improve:** FIASSE is an ongoing process. Implement real-time security observability and use the gathered insights to continuously refine security strategies and FIASSE implementation.

The applicability of FIASSE spans various organizational types, including large technology companies integrating it into Continuous Security Engineering, financial institutions enhancing data protection, AI and cloud-based companies designing secure architectures, and open-source projects adopting secure development guidelines.

## 9. Security Considerations

This entire document is focused on improving application security. The FIASSE itself is a framework designed to systematically address security in development. By promoting attributes like Analyzability, Modifiability, and Testability, and by advocating for practices such as early integration of security requirements, threat modeling, defensive coding, and robust dependency management, FIASSE aims to reduce the likelihood of vulnerabilities and mitigate the potential impact of security incidents.

The successful implementation of FIASSE relies on organizational commitment to security aligning with development activities. Failure to address the cultural aspects of collaboration between AppSec and Development, or neglecting the strategic application of security tooling, can undermine the effectiveness of the framework.

## 10. Conclusion

Building securable software is not solely the responsibility of individual programmers; it MUST be a natural and integral part of the Software Engineering discipline. FIASSE offers a framework to achieve this by fostering a common understanding between Application Security and Development teams.

AppSec can allow development teams to build securable code confidently and autonomously. This collaborative, developer-centric approach, as outlined by FIASSE, aims to reduce friction, avoid common pitfalls like "Shoveling Left," and ultimately lead to more secure software outcomes that align with business objectives.

## 11. References

[Howard] Howard, R., "Cyber Security First Principles: A Reboot of Strategy and Tactics", Cybersecurity First Principles, LLC, 2019.

[ISO-25010] ISO/IEC 25010:2011, "Systems and software engineering -- Systems and software Quality Requirements and Evaluation (SQuaRE) -- System and software quality models". International Organization for Standardization.

[OWASP-SAMM] OWASP Software Assurance Maturity Model (SAMM). (Referenced for role-specific guidance concepts).

[RFC3552] Rescorla, E. and B. Korver, "Guidelines for Writing RFC Text on Security Considerations", BCP 72, RFC 3552, DOI 10.17487/RFC3552, July 2003, <https://www.rfc-editor.org/info/rfc3552>. (Illustrates IETF emphasis on security documentation, which SSEM helps fulfill in spirit for software).

[OpenSSF] Open Source Security Foundation (OpenSSF). (Referenced for data on developer security learning curves).

[Wikipedia-SE] Wikipedia, "Software engineering". <https://en.wikipedia.org/wiki/Software_engineering>.

## 12. Author's Address

Editor
[Details TBD]
