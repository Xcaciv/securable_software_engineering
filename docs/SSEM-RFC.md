# A Framework for Integrating Application Security into Software Engineering: The Securable Software Engineering Model (SSEM)

> Request for Comments:
> 
> Obsoletes: None
> 
> Category: Informational
>
> Alton Crossley
> May 2025

## Abstract

> This document describes the Securable Software Engineering Model (SSEM), a framework designed to integrate application security principles and practices directly into the software engineering discipline. It addresses the common challenges of friction between Application Security (AppSec) and Development teams, the perceived slow progress in enhancing software security, and the need to empower developers to build securable code without requiring them to become penetration testing experts. The SSEM provides a design language based on established software engineering terms, focusing on inherent security attributes of code and software architecture that contribute to security. This document outlines the core principles of SSEM, its key attributes, methods for its integration into the development processes, practical guidance for developers, and considerations for its adoption and evolution. The goal is to reduce the probability of material impact from cyber events by fostering a collaborative, developer-centric approach to application security, particularly for software that implements or relies on Internet protocols and services.

## Copyright Notice

> Copyright (c) 2025 Alton Crossley All rights reserved.
>
> see licence.txt for details.

## Table of Contents

- [A Framework for Integrating Application Security into Software Engineering: The Securable Software Engineering Model (SSEM)](#a-framework-for-integrating-application-security-into-software-engineering-the-securable-software-engineering-model-ssem)
  - [Abstract](#abstract)
  - [Copyright Notice](#copyright-notice)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1. The Application Security Challenge](#11-the-application-security-challenge)
    - [1.2. A Developer-Centric Security Paradigm](#12-a-developer-centric-security-paradigm)
    - [1.3. Document Purpose and Scope](#13-document-purpose-and-scope)
  - [2. Foundational Principles](#2-foundational-principles)
    - [2.1. Security Mission: Reducing Material Impact](#21-security-mission-reducing-material-impact)
    - [2.2. Mindset Divergence: Hacker vs. Engineer](#22-mindset-divergence-hacker-vs-engineer)
    - [2.3. Aligning Security with Development](#23-aligning-security-with-development)
  - [3. The Securable Software Engineering Model (SSEM)](#3-the-securable-software-engineering-model-ssem)
    - [3.1. Overview and Objectives](#31-overview-and-objectives)
    - [3.2. Core Securable Attributes](#32-core-securable-attributes)
      - [3.2.1. Maintainability](#321-maintainability)
        - [3.2.1.1. Analyzability](#3211-analyzability)
        - [3.2.1.2. Modifiability](#3212-modifiability)
        - [3.2.1.3. Testability](#3213-testability)
      - [3.2.2. Trustworthiness](#322-trustworthiness)
        - [3.2.2.1. Confidentiality](#3221-confidentiality)
        - [3.2.2.2. Non-repudiation](#3222-non-repudiation)
        - [3.2.2.3. Accountability](#3223-accountability)
        - [3.2.2.4. Authenticity](#3224-authenticity)
      - [3.2.3. Reliability](#323-reliability)
        - [3.2.3.1. Availability](#3231-availability)
        - [3.2.3.2. Integrity](#3232-integrity)
        - [3.2.3.3. Fault Tolerance](#3233-fault-tolerance)
        - [3.2.3.4. Resilience](#3234-resilience)
    - [3.3. SSEM as a Design Language](#33-ssem-as-a-design-language)
  - [4. Integrating SSEM into Development Lifecycles](#4-integrating-ssem-into-development-lifecycles)
    - [4.1. Applying SSEM to Dependency Management](#41-applying-ssem-to-dependency-management)
    - [4.2. Natively Extending Development Processes](#42-natively-extending-development-processes)
    - [4.3. The Role of Merge/Pull Request Reviews](#43-the-role-of-mergepull-request-reviews)
    - [4.4. Early Integration: Planning and Requirements](#44-early-integration-planning-and-requirements)
  - [5. Addressing Common AppSec Anti-Patterns](#5-addressing-common-appsec-anti-patterns)
    - [5.1. The "Shoveling Left" Phenomenon](#51-the-shoveling-left-phenomenon)
      - [5.1.1. Ineffective Vulnerability Reporting](#511-ineffective-vulnerability-reporting)
      - [5.1.2. Pitfalls of Exploit-First Training](#512-pitfalls-of-exploit-first-training)
    - [5.2. Strategic Use of Security Tooling Output](#52-strategic-use-of-security-tooling-output)
  - [6. Practical Guidance for Secure Software Development](#6-practical-guidance-for-secure-software-development)
    - [6.1. Establishing Clear Expectations](#61-establishing-clear-expectations)
      - [6.1.1. Proactive Communication](#611-proactive-communication)
      - [6.1.2. Integrating Security into Requirements](#612-integrating-security-into-requirements)
    - [6.2. Threat Modeling as a Collaborative Practice](#62-threat-modeling-as-a-collaborative-practice)
    - [6.3. Managing Flexibility and Control](#63-managing-flexibility-and-control)
    - [6.4. Defensive Coding and System Resilience](#64-defensive-coding-and-system-resilience)
    - [6.5. Dependency Management](#65-dependency-management)
  - [7. Roles and Responsibilities in SSEM Adoption](#7-roles-and-responsibilities-in-ssem-adoption)
    - [7.1. Empowering Senior Software Engineers](#71-empowering-senior-software-engineers)
    - [7.2. Guiding Developing Software Engineers](#72-guiding-developing-software-engineers)
  - [8. Evolution and Adoption of SSEM](#8-evolution-and-adoption-of-ssem)
    - [8.1. Adapting to Emerging Software Engineering Trends](#81-adapting-to-emerging-software-engineering-trends)
      - [8.1.1. AI-Driven Software Development](#811-ai-driven-software-development)
      - [8.1.2. Low-Code and No-Code Platforms](#812-low-code-and-no-code-platforms)
      - [8.1.3. Cloud-Native and Serverless Architectures](#813-cloud-native-and-serverless-architectures)
      - [8.1.4. DevSecOps and Continuous Security](#814-devsecops-and-continuous-security)
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

This document posits that expecting every software engineer to adopt the mindset and skillset of a penetration tester ("hacker") is neither scalable nor the most effective path to secure software. Instead, if AppSec practices are effective and well-integrated, software engineers can build secure systems by leveraging sound software engineering principles. This approach focuses on empowering developers with the knowledge and tools to build securable software as a natural part of their discipline.

### 1.3. Document Purpose and Scope

The purpose of this document is to introduce the Securable Software Engineering Model (SSEM). SSEM is a framework designed to align AppSec objectives with business goals. It provides a common language and a set of principles to guide the creation of secure software.

This document will cover:

- Foundational principles underpinning SSEM.
- The core attributes of securable software as defined by SSEM.
- Strategies for integrating SSEM into existing development processes.
- Common pitfalls in AppSec and how SSEM helps to avoid them.
- Practical guidance for developers to build securable code.
- The roles of different engineering personnel in adopting SSEM.
- The potential evolution of SSEM in response to emerging software engineering trends and strategies for organizational adoption.

This document is intended for AppSec professionals, software engineers, engineering managers, and anyone involved in the Software Development Lifecycle (SDLC) who seeks to improve application security outcomes.

## 2. Foundational Principles

### 2.1. Security Mission: Reducing Material Impact

The core mission of cybersecurity, as articulated by Rick Howard in "Cyber Security First Principles," is to 'Reduce the Probability of Material Impact of a cyber event, aligned with the business's risk appetite'. Complete elimination of breaches, while an ideal, is often not a functional business goal. Security strategies MUST, therefore, align with overarching business objectives. This requires a balanced approach, particularly from experienced professionals. While formal buy-in and metrics are necessary, AppSec's role extends to enabling Development teams to meet security expectations and pass security assessments. Effectivly prepairing applications for our connected world.

### 2.2. Mindset Divergence: Hacker vs. Engineer

The perspective that all programmers should be penetration testers, or think like attackers, to eliminate security problems overlooks a critical distinction. While understanding how systems can be compromised is valuable, it does not inherently translate into the knowledge of how to build them securely. There is a significant difference between identifying a vulnerability and implementing a robust, scalable software engineering solution.

Expecting developers to become expert penetration testers is akin to requiring them to master formal software testing or Quality Assurance (QA) disciplines merely to write unit tests. Programmers MUST test their own code, but they do not need to become QA experts. A similar principle applies to security assurance.

### 2.3. Aligning Security with Development

True alignment between security and development requires a return to first principles. Instead of imposing security-centric jargon and processes that may seem alien to developers, SSEM advocates for using well-established Software Engineering terms to describe securable code attributes. This fosters understanding and empowers developers to address security confidently without years of dedicated security experience. The goal is to instill confidence in developers, enabling them to recognize securable attributes in existing code and understand what building securely entails from an engineering perspective. As will be discussed, this also requires specific participation from AppSec professionals in the early stages of the Software Development Lifecycle (SDLC), particularly during requirements gathering and feature planning.

## 3. The Securable Software Engineering Model (SSEM)

### 3.1. Overview and Objectives

The Securable Software Engineering Model (SSEM) provides a design language focused on code and software architecture. It defines securable attributes using terms familiar to developers, abstracting away from specific security processes or exploit-centric language. This allows software engineers to confidently address security as an integral part of their work.

SSEM is designed to:

- Account for the iterative nature of software development and agile methodologies.
- Serve as a mental model, a checklist, or a means to set clear expectations.
- Shift the conversation from a binary "Is it secure?" to a more nuanced "Do we meet our goals for this particular attribute?"

| **Maintainability** | **Trustworthiness** | **Reliability** |
|-----------------|-----------------|--------------|
| Analyzability    | Confidentiality | Availability  |
| Modifiability    | Non-repudiation | Integrity     |
| Testability      | Accountability  | Fault Tolerance|
|                  | Authenticity    | Resilience     |

SSEM is not a rigid framework but a flexible model that can adapt to various software engineering practices. It emphasizes the inherent qualities of well-engineered software that contribute directly to security, rather than prescribing specific security controls or processes. This allows it to scale effectively without requiring security to adopt toilsome or overly complex processes that may not align with the development team's workflow.

### 3.2. Core Securable Attributes

SSEM identifies several fundamental and universal attributes of securable code. These attributes are inherent qualities of well-engineered software that also contribute directly to its security. They are grouped into three primary categories: Maintainability, Trustworthiness, and Reliability, each encompassing specific sub-attributes detailed below.

#### 3.2.1. Maintainability

Definition: Maintainability is the "degree of effectiveness and efficiency with which a product or system can be modified by the intended maintainers" (ISO/IEC 25010:2011). In the context of SSEM, this means software can be evolved, corrected, and adapted to new threats or requirements without undue effort or introducing new vulnerabilities. It encompasses the following sub-attributes:

##### 3.2.1.1. Analyzability

Definition: “The degree of effectiveness and efficiency with which it is possible to assess the impact on a product or system of an intended change to one or more of its parts, or to diagnose a product for deficiencies or causes of failures, or to identify parts to be modified” (ISO 25010, §4.2.7.3). This means the ability to find the cause of a behavior within the code. From a security standpoint, code must be understandable to find and fix vulnerabilities.

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

##### 3.2.1.3. Testability

Definition: “The degree of effectiveness and efficiency with which test criteria can be established for a system, product or component and tests can be performed to determine whether those criteria have been met” (ISO 25010, §4.2.7.5). This is the ability to write a test for a piece of code without needing to change the code under test. Effective testing is crucial for verifying security controls and detecting regressions.

Contributing Factors:

- Volume: Larger codebases can be more challenging to test comprehensively.
- Unit Complexity: Complex units are more difficult to test thoroughly.
- Component Independence: The percentage of code in modules with no incoming dependencies from modules in other top-level components; higher independence facilitates isolated testing.

#### 3.2.2. Trustworthiness

Definition: Trustworthiness is "the degree to which a system (including all its components and procedures) can be expected to achieve a set of requirements, such as security requirements" (RFC 4949). A trustworthy system operates within defined levels of trust and meets specified security properties. Key attributes contributing to trustworthiness include:

##### 3.2.2.1. Confidentiality

Definition: "The property that data is not disclosed to system entities unless they have been authorized to know the data" (RFC 4949). This ensures that sensitive information is protected from unauthorized access.

##### 3.2.2.2. Non-repudiation

Definition: The "ability to prove the occurrence of a claimed event or action and its originating entities" (ISO/IEC 27000:2018). This prevents entities from falsely denying having performed an action or sent a message.

##### 3.2.2.3. Accountability

Definition: "The property of a system or system resource that ensures that the actions of a system entity may be traced uniquely to that entity" (RFC 4949). This involves managing principals and their access, enabling the attribution of actions to specific users or processes, which is crucial for auditing and incident response.

##### 3.2.2.4. Authenticity

Definition: "The property that an entity is what it claims to be" (ISO/IEC 27000:2018). This ensures that users, systems, or information are genuine and can be verified.

#### 3.2.3. Reliability

Definition: Reliability is the "degree to which a system, product or component performs specified functions under specified conditions for a specified period of time" (ISO/IEC 25010:2011). In SSEM, this means the software operates consistently and predictably, even under adverse conditions or when facing unexpected inputs or attacks. It includes the following attributes:

##### 3.2.3.1. Availability

Definition: "The property of a system or a system resource being accessible and usable upon demand by an authorized system entity, according to performance specifications for the system" (RFC 4949). This ensures that the system is operational and accessible when needed.

##### 3.2.3.2. Integrity

Definition: Encompasses both data integrity, "the property that data has not been changed, destroyed, or lost in an unauthorized or accidental manner," and system integrity, where a system "performs its intended function in an unimpaired manner free from unauthorized manipulation" (RFC 4949). This ensures the accuracy, completeness, and soundness of data and system operations.

##### 3.2.3.3. Fault Tolerance

Definition: "The ability of a system to continue to operate correctly even though a component has failed" (RFC 4949). This allows the system to withstand partial failures without complete breakdown.

##### 3.2.3.4. Resilience

Definition: "The ability of a system to: (a) continue to operate during and after a failure of some part of the system (i.e., provide a degree of fault tolerance); and (b) recover from the failure and restore full operations" (RFC 4949). This also aligns with the concept of an application's ability to continue running predictably, even under unfavorable circumstances or load (as noted in Section 6.4).

### 3.3. SSEM as a Design Language

By defining these attributes using established software engineering terminology, SSEM provides a common design language. This enables developers to discuss, reason about, and implement security considerations using concepts already familiar to them. It shifts the focus from reacting to vulnerabilities to proactively building software with inherent securable qualities.

## 4. Integrating SSEM into Development Lifecycles

### 4.1. Applying SSEM to Dependency Management

SSEM principles can be effectively applied to the entire lifecycle of software dependencies. This application extends beyond merely scanning for vulnerabilities (a reactive tactic detailed further in Section 6.5) to proactively considering the following SSEM attributes in the context of dependency management:

- Analyzability: Requires a thorough understanding of each dependency's full scope, including its transitive dependencies, its specific purpose within the application, and its potential attack surface. Maintaining a clear inventory and a documented rationale for every included dependency is crucial.
- Modifiability: Encourages designing systems with loosely coupled dependencies to facilitate easier updates, patching, or replacement if a vulnerability is discovered, a dependency becomes obsolete, or a more secure alternative is identified. This aligns with architectural modifiability.
- Testability: Involves ensuring that dependencies can be effectively managed during testing (e.g., through mocking, stubbing, or version pinning) and that their integration points are themselves robustly testable.
- Trustworthiness (Authenticity and Integrity): Mandates implementing processes to verify the source and integrity of dependencies (e.g., using signed packages, checksums, and trusted repositories) before their integration into the codebase.
- Reliability: Entails assessing how a dependency's failure modes (e.g., unavailability, performance degradation, security compromise) could impact the overall system's reliability and resilience, and subsequently planning appropriate mitigations.

By embedding these SSEM considerations into how dependencies are selected, integrated, monitored, and updated, security becomes an inherent part of this common and critical development practice.

### 4.2. Natively Extending Development Processes

A key principle for reducing friction and effectively preparing development teams is to integrate security into existing development workflows rather than imposing separate, external security gates. This involves understanding and extending current practices.

Examples include:

- Epic/Feature Creation: Considering security implications and SSEM attributes during the early planning and design phases, which is critical when these features involve interaction with Internet protocols or exposure to Internet-based threats.
- Usability: Framing usability not just as aesthetics but as building trust from a security standpoint (e.g., clear error messages, intuitive permissions management).

### 4.3. The Role of Merge/Pull Request Reviews

While software engineering may lack formal licensing like other engineering disciplines, the merge review (or pull request review) process serves as a crucial point for mentoring, guidance, and validation. For security, this is where securable code review can scale effectively. It acts as an agile training ground where developers learn from peers and receive feedback in a constructive environment. SSEM attributes can provide a concrete basis for these reviews.

### 4.4. Early Integration: Planning and Requirements

Integrating security considerations early in the development lifecycle is paramount. SSEM encourages AppSec participation in requirements gathering and feature planning. This ensures that security is not an afterthought but a foundational aspect of the design. Techniques such as defining Threat Scenarios and Security Acceptance Criteria (discussed further in Section 6.1.2) make expectations explicit from the outset.

## 5. Addressing Common AppSec Anti-Patterns

### 5.1. The "Shoveling Left" Phenomenon

"Shoveling Left" is defined as the practice of supplying impractical information to developers and leaving the responsibility on them to make sense of it. This anti-pattern often manifests in how vulnerabilities are reported, training is conducted, and testing results are delivered. It can undermine AppSec's credibility and lead to developer disengagement.

#### 5.1.1. Ineffective Vulnerability Reporting

A prime example of "Shoveling Left" is dumping raw findings from security scanning tools directly into the development team's backlog. This approach often lacks context, prioritization, and actionable guidance. While initial progress might be observed, momentum is typically lost, and issues may reappear (the "whack-a-mole" effect). Raw tool output, on its own, is rarely impactful enough to drive sustained improvement.

To avoid this, AppSec SHOULD:

1. Focus on True Positives: Validate findings to ensure accuracy.
2. Identify Root Causes: Address systemic issues rather than just symptoms.
3. Prioritize by Impact: Focus on issues that are plentiful or affect sensitive resources.
4. Collaborate on Solutions: Work with development teams on framework-level or architectural changes.
5. Verify Fixes: Ensure remediation is effective and consider automated regression tests.

#### 5.1.2. Pitfalls of Exploit-First Training

Another form of "Shoveling Left" is security training for developers that focuses primarily on exploitation techniques ("learn the hack to stop the attack"). While understanding attack vectors can be beneficial in some security domains, simply knowing how to exploit a vulnerability in software does not equate to knowing the needed engineering solution to prevent or remediate it.

Exploit-centric training often fails to address whether a vulnerability stems from a typo, an architectural flaw, or a misunderstanding of requirements. It does not inherently teach developers how to prevent issues systematically or design more secure systems from an engineering standpoint.

### 5.2. Strategic Use of Security Tooling Output

While scanning and testing tools are valuable for AppSec to understand the current security posture, their output MUST be used strategically. It SHOULD NOT be assumed that security requirements are implicit or that developers should be blamed for missing controls if clear expectations were not set. Without such expectations, what AppSec perceives as a flaw, Development might see as implicitly exposed flexibility.

## 6. Practical Guidance for Secure Software Development

### 6.1. Establishing Clear Expectations

Clear expectations are foundational to building securable products. AppSec can maximize its impact by setting these expectations early and effectively.

#### 6.1.1. Proactive Communication

Basic communication is essential. Development teams SHOULD be informed about new testing initiatives or security programs. Demonstrating tools to interested senior developers can foster collaboration and identify key contacts for strategic fix efforts. Regular synchronization points can help offer support and maintain momentum. Effective soft skills are crucial for AppSec professionals.

#### 6.1.2. Integrating Security into Requirements

Beyond informal communication, AppSec SHOULD participate actively in formal requirements gathering processes. Instead of solely reviewing and auditing after development, participation ensures security is embedded from the start.

Key methods include:

- Threat Scenarios: Describing potential misuse cases or attack paths relevant to the feature being developed. This helps identify necessary controls.
- Security Acceptance Criteria: Defining specific, testable conditions that a feature must meet to be considered secure. These criteria allow QA to perform security testing by verifying requirements.

Integrating security into foundational design decisions through requirements ensures proper realization of trustworthiness attributes like Integrity and Fault Tolerance. Requirements are an often underutilized yet powerful tool for security.

### 6.2. Threat Modeling as a Collaborative Practice

Threat modeling is a valuable team activity, ideally performed early in the development process, similar to requirements gathering. Even a simple framework, such as the "Four Question Framework" (What are we building? What can go wrong? What are we going to do about it? Did we do a good job?), can highlight areas needing more detailed design or specific security requirements.

A key concept emerging from threat modeling is the identification of **trust boundaries**. These are points in the system where data passes between entities with different levels of trust (e.g., user to application, application to database, service to service). Trust boundaries require heightened control and caution.

### 6.3. Managing Flexibility and Control

Software engineers often value flexibility in code, as it can facilitate feature implementation and bug fixing. Attackers, however, seek uncontrolled flexibility—unconventional ways to use software that deviate from intended behavior.

The issue is not flexibility itself, but the lack of appropriate control, especially at trust boundaries and for operations requiring high resilience. An example of excessive, uncontrolled flexibility might be a function capable of executing arbitrary statements with arbitrary parameters without restriction. Control is essential to ensure trustworthy execution, maintain system Integrity, and support Fault Tolerance.

### 6.4. Defensive Coding and System Resilience

Resilience refers to an application's ability to continue running predictably, even under unfavorable circumstances or load. Tactical resilience is achieved through **defensive coding** practices that promote predictable execution.

This drives the need for concrete developer actions such as:

- Filtering and validating all input, especially at trust boundaries. Input validation ensures that data conforms to expected formats, types, lengths, and ranges before processing.
- Properly escaping and encoding all output destined for other systems or interpreters (e.g., HTML, SQL, shell commands). This prevents injection attacks.

These are verifiable actions that AppSec can guide and assess.

### 6.5. Dependency Management

Regularly updating software dependencies is a fundamental tactic for maintaining security. Updates often include fixes for known bugs, including security vulnerabilities. This SHOULD be a routine process, integrated into development sprints or regular maintenance cycles.

Key considerations for dependency management:

- If no direct update fixes a known flaw in a dependency, further analysis is required to identify mitigation strategies (e.g., compensating controls, forking and patching, or reimplementation).
- Organizations SHOULD have a clear policy regarding the use and maintenance of open-source dependencies, including processes for addressing vulnerabilities found within them.
- Reliance solely on CVE (Common Vulnerabilities and Exposures) reporting may not be sufficient. A thorough analysis of dependencies and their transitive "baggage" is recommended.

## 7. Roles and Responsibilities in SSEM Adoption

Understanding different development roles is crucial for tailoring guidance and effectively integrating SSEM.

### 7.1. Empowering Senior Software Engineers

Experienced, top-tier software engineers are critical to the success of any AppSec program. AppSec professionals SHOULD work collaboratively *with* these engineers on architecture and design. They can bridge the gap between security objectives and development realities.

Senior engineers SHOULD:

- Drive the creation of Security Requirements, Acceptance Criteria, and Threat Scenarios.
- Lead merge reviews, emphasizing SSEM attributes, software engineering principles, and the importance of trust boundaries.
- Champion and schedule regular dependency maintenance.
- Extend defensive coding concepts (e.g., Fail Secure design, robust Exception Handling, Security Unit Testing, Defense-in-Depth, comprehensive Logging).
- Lead by example, utilizing and promoting policies, standards, and guidelines.

### 7.2. Guiding Developing Software Engineers

Software engineers who are still gaining experience (Artisan or Ancillary Coders) benefit greatly from mental checklists like SSEM and the methodologies it describes. They may not always intuitively know "What can go wrong?" but can learn effectively through structured guidance, merge reviews, and pair programming.

These engineers SHOULD be encouraged to:

- Ask for clear Security Requirements, Acceptance Criteria, and Threat Scenarios.
- Be cautious about introducing new external dependencies without due diligence.
- Actively seek code reviews from senior team members.
- Write unit tests that cover exceptional conditions and out-of-bounds values.
- Learn and apply defensive coding techniques, particularly input validation.
- Be mindful of trust boundaries in the code they write.
- Focus on becoming strong software engineers, understanding that SSEM attributes like Maintainability, Reliability, and Identity are inherently security concerns.

## 8. Evolution and Adoption of SSEM

### 8.1. Adapting to Emerging Software Engineering Trends

SSEM is positioned to evolve alongside emerging trends in software engineering, ensuring that security remains an integral component.

#### 8.1.1. AI-Driven Software Development

The increasing use of AI-powered tools, particularly Generative AI, for code generation, bug detection, and automated testing presents both significant opportunities and challenges for software security. While these tools can accelerate development, they also risk propagating insecure coding patterns or generating code that is difficult to analyze, modify, and test securely if not properly guided.

SSEM is well-suited to address this by providing a framework for **Prompt Engineering for Securable Code**. This involves crafting prompts for Generative AI tools that explicitly or implicitly request code exhibiting SSEM's core securable attributes:

- Analyzability in Prompts: Prompts can direct AI to generate code that is well-commented, uses clear and consistent naming conventions, adheres to established coding standards, and possesses a logical, understandable structure. For example, a prompt might specify, "Generate a Python function to parse CSV data, ensuring comprehensive comments for each logical step and adherence to PEP 8 style guidelines."
- Modifiability in Prompts: Prompts can guide AI to produce modular code with low coupling and high cohesion, clear interfaces, and an avoidance of duplicated logic. An example could be, "Develop a Java class for user authentication that is easily extensible for new authentication methods and avoids hardcoding configuration parameters."
- Testability in Prompts: Prompts can request the generation of code that is inherently testable, for instance, by asking for functions with clear inputs and outputs, minimal side effects, and even the co-generation of unit tests. For example, "Write a Go function to calculate X, and include unit tests covering valid inputs, invalid inputs, and edge cases."

Beyond these core attributes, prompts can also incorporate broader security considerations derived from SSEM's principles:

- Requesting code that implements specific security controls (e.g., "Generate code to sanitize user input to prevent XSS").
- Asking the AI to consider and mitigate common vulnerabilities relevant to the code's context.
- Specifying adherence to organizational security policies or standards.

Integrating SSEM into prompt engineering aims to shift the output of AI code generators towards producing code that is not only functional but also inherently more secure and maintainable from its inception. This proactive approach complements other AI-enhanced security practices, such as AI-driven static analysis for automated security reviews of both human-written and AI-generated code, predictive security analytics to identify potential vulnerabilities earlier, and AI-assisted threat modeling.

#### 8.1.2. Low-Code and No-Code Platforms

As low-code and no-code development platforms become more prevalent, SSEM principles can be adapted by:

- Establishing security guidelines tailored for citizen developers.
- Embedding automated security checks within these platforms.
- Ensuring that pre-built components and templates adhere to secure coding principles.

#### 8.1.3. Cloud-Native and Serverless Architectures

The shift towards microservices, containers, and serverless computing necessitates an emphasis within SSEM on:

- Secure API design and robust authentication/authorization mechanisms.
- Comprehensive Identity and Access Management (IAM) for distributed systems.
- Resilient architecture principles to mitigate cloud-specific threats.

#### 8.1.4. DevSecOps and Continuous Security

SSEM naturally aligns with DevSecOps philosophies by embedding security into CI/CD pipelines. Future adaptations will likely further strengthen this alignment through:

- Enhanced automation of security testing at various stages of the build and deployment process.
- Improved security observability for real-time monitoring and incident response.
- Continued development of developer-friendly security tooling that integrates seamlessly into their workflows.

#### 8.1.5. Quantum-Resistant Cryptography

As quantum computing capabilities advance, posing a threat to current cryptographic standards, SSEM will need to incorporate guidance on:

- Transitioning to quantum-safe cryptographic algorithms.
- Secure key management strategies suitable for a post-quantum era.
- Resilient data protection mechanisms that anticipate future cryptographic challenges.

#### 8.1.6. Ethical AI and Security Governance

With AI playing a larger role in software development, ethical considerations and robust governance become critical. SSEM may evolve to include:

- Guidelines to ensure AI-generated code adheres to security best practices and ethical standards.
- Frameworks for governing AI-driven development processes from a security perspective.
- Strategies to mitigate bias and adversarial attacks in AI models used within the SDLC.

### 8.2. Organizational Adoption Strategies

Adopting SSEM effectively requires a structured approach:

1. **Assess Current Practices:** Evaluate existing software engineering workflows and security posture to identify gaps where SSEM principles can provide the most benefit. This may involve security audits and maturity assessments.
2. **Educate and Train Teams:** Provide comprehensive training on SSEM principles, secure coding, threat modeling, and dependency management. Training SHOULD be role-specific and integrated into onboarding and continuous learning programs.
3. **Integrate into Workflows:** Embed SSEM into the DevSecOps pipeline. This includes implementing securable code reviews with SSEM-based checklists, automating security testing, and making threat modeling a standard practice.
4. **Establish Secure Architecture Principles:** Ensure that software architecture aligns with SSEM attributes (Analyzability, Modifiability, Testability, etc.). This involves designing secure APIs, managing dependencies rigorously, and implementing resilient data protection.
5. **Foster Collaboration:** Promote strong collaboration between AppSec, Development, and Operations teams. SSEM aims to reduce friction by using a common language; this should be reinforced through shared responsibilities and goals.
6. **Continuously Monitor and Improve:** Security is an ongoing process. Implement real-time security observability and use the gathered insights to continuously refine security strategies and SSEM implementation.

The applicability of SSEM spans various organizational types, including large technology companies integrating it into DevSecOps, financial institutions enhancing data protection, AI and cloud-based companies designing secure architectures, and open-source projects adopting secure development guidelines.

## 9. Security Considerations

This entire document is focused on improving application security. The Securable Software Engineering Model (SSEM) itself is a framework designed to systematically address security throughout the software development lifecycle. By promoting attributes like Analyzability, Modifiability, and Testability, and by advocating for practices such as early integration of security requirements, threat modeling, defensive coding, and robust dependency management, SSEM aims to reduce the likelihood of vulnerabilities and mitigate the potential impact of security incidents.

The successful implementation of SSEM relies on organizational commitment, continuous education, and the active participation of all stakeholders in the SDLC. Failure to address the cultural aspects of collaboration between AppSec and Development, or neglecting the strategic application of security tooling, can undermine the effectiveness of the model.

From an IETF perspective, the adoption of robust software engineering practices like those outlined in SSEM is a significant security consideration. It contributes to the overall trustworthiness and resilience of software that implements Internet standards and participates in the global Internet ecosystem.

## 10. Conclusion

Building securable software is not solely the responsibility of individual programmers; it MUST be a natural and integral part of the Software Engineering discipline. The Securable Software Engineering Model (SSEM) offers a framework to achieve this by fostering a common understanding and language between Application Security and Development teams.

By emphasizing established software engineering principles, promoting clear communication, setting expectations early (especially in requirements), and providing practical, actionable guidance, AppSec can empower development teams to build securable code confidently and autonomously. This collaborative, developer-centric approach, as outlined by SSEM, aims to reduce friction, avoid common pitfalls like "Shoveling Left," and ultimately lead to more secure software outcomes that align with business objectives.

## 11. References

[Howard] Howard, R., "Cyber Security First Principles: A Reboot of Strategy and Tactics", Cybersecurity First Principles, LLC, 2019.

[ISO-25010] ISO/IEC 25010:2011, "Systems and software engineering -- Systems and software Quality Requirements and Evaluation (SQuaRE) -- System and software quality models". International Organization for Standardization.

[OWASP-SAMM] OWASP Software Assurance Maturity Model (SAMM). (Referenced for role-specific guidance concepts).

[RFC3552] Rescorla, E. and B. Korver, "Guidelines for Writing RFC Text on Security Considerations", BCP 72, RFC 3552, DOI 10.17487/RFC3552, July 2003, <https://www.rfc-editor.org/info/rfc3552>. (Illustrates IETF emphasis on security documentation, which SSEM helps fulfill in spirit for software).

[OpenSSF] Open Source Security Foundation (OpenSSF). (Referenced for data on developer security learning curves).

## 12. Author's Address

Editor
[Details TBD]
