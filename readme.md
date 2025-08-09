# A Framework for Integrating Application Security into Software Engineering (FIASSE)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

**Note:** This repository is an ongoing work. Contributions are welcome!

## Overview

This repository contains resources and materials for the OWASP Framework for Integrating Application Security into Software Engineering (FIASSE). FIASSE (pronounced /feiz/) promotes a **developer-centric, principled approach** to build **securable** software — recognizing that security is a dynamic, ongoing process like development. It introduces the Securable Software Engineering Model (SSEM) as a **common design language** that uses established software engineering terms to integrate security into software architecture, software design and programming. It aims to build resilient applications that withstand threats.

## Purpose

To provide practical guidelines that **empower developers** to create securable software without requiring deep security expertise, and to guide security professionals in effectively integrating their security experience into software engineering. FIASSE achieves this through a **Software Engineering lens**, reducing cognitive load and fostering collaboration between development and security teams.

## How is it Different?

Think of the SSEM as an *allow* list rather than a *block* list. While the OWASP Top 10 highlights what to avoid (a block list), OWASP FIASSE provides a set of positive attributes and practices to follow (an allow list). This approach leverages existing software engineering skills to build securable software, rather than requiring developers to learn exploit techniques or adopt a vulnerability-focused mindset. The emphasis is on enabling practical, secure coding through familiar engineering principles.

This framework highlights that business value is captured when security requirements are clearly defined within the *source* of work for development. By establishing expectations this way, the likelihood of security flaws being discovered and needing remediation later is significantly reduced.

## Key Principles

- **The Securable Paradigm**: Acknowledging that software security is a dynamic, ongoing process, not a static "secure" state. Focuses on building inherent qualities into software to adapt to evolving threats.
- **Developer-Centric Security**: Empowering software engineers to autonomously build securable systems using familiar software engineering principles, rather than requiring them to adopt a penetration tester's mindset.
- **SSEM as a Common Design Language**: Utilizing the Securable Software Engineering Model (SSEM) which employs established software engineering terms (e.g., Analyzability, Modifiability, Testability) to define and discuss security attributes, making security more accessible to developers.
- **Aligning Security with Development & Business Goals**: Integrating security considerations seamlessly into the SDLC and ensuring that security efforts support overarching business objectives and risk appetite.
- **Resiliently Add Computing Value**: Ensuring software not only meets functional requirements but also possesses securable qualities that allow it to adapt, persist, and maintain integrity over time and under stress.
- **Requirements as a First-Class Citizen in AppSec**: Grounding secure software engineering in clearly defined security expectations and requirements from the outset.

## Repository Contents

- Definition and Documentation of the Securable Software Engineering Model (SSEM)
- Implementation guides for the FIASSE methodology
- Examples of secure coding requirements and practices including Generative AI artifacts

## Getting Started

1. Review the documentation in the `/docs` directory
2. Explore the examples in the `/examples` directory

- Bonus: Check out the `/examples/copilot-instructions` directory for examples of how to apply FIASSE principles in the context of Generative AI development and how to prompt for an instruction file of your own.

## Summary

This repository defines securable software as systems designed for resilience and adaptability. It emphasizes true security is an ongoing process, not a static achievement. It introduces the Securable Software Engineering Model (SSEM), which frames security as an inherent quality of well-engineered software. To do this it focuses on attributes like Maintainability, Trustworthiness, and Reliability (which includes Resilience). FIASSE advocates for integrating security practices directly into the development workflow. This moves from a "security as an afterthought" or a "shift left" approach to a proactive, collaborative model. The idea is that product owners, developers, and security professionals work together from the earliest stages of design, particularly through activities like security requiremnts definition, collaborative threat modeling, and acceptance criteria. This sets clear expectations for code activities and testing. Software engineers are given guidance on balancing flexibility and control. They are also given a definitive model for making security decisions. Ultimately, this empowers all stakeholders to contribute to building more robust, resilient, and inherently securable systems.

The way this differs from existing approaches is that it does not require developers to become security experts or adopt an adversarial mindset. This approach aims to reduce the cognitive load on developers while ensuring that security can be confident their concerns are being addressed through specific attributes of code and software engineering processes.

FIASSE intends to be open, approachable and collaborative without hiding behind a pay-wall or ellitist practices.

## Complementary Resources

This repository complements the soon to be established [FIASSE website](https://fiasse.org).

The OWASP FIASSE project is part of the [OWASP Foundation](https://owasp.org/www-project-fiasse/), a non-profit organization focused on the mission of no more insecure software. The OWASP Foundation provides a wealth of resources and frameworks that align with the principles of FIASSE.

This framework is focused on securable Software Engineering and is complemented by assurance frameworks from OWASP:

- Assurance verification: [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
- Assurance maturity: [OWASP Software Assurance Maturity Model (SAMM)](https://owasp.org/www-project-software-assurance-maturity-model/)

OWASP also hosts neumerous projects that document security requirements and features, such as [OWASP Mobile Application Security](https://mas.owasp.org/). Various other OWASP resources are explained in the [OWASP Developer Guide](https://owasp.org/www-project-developer-guide/), which is a comprehensive resource for secure software practices.

NIST [Secure Software Development Framework (SSDF)](https://csrc.nist.gov/publications/detail/sp/800-218/final) defines four phases that represent different facets for implementing secure software development practices. It aligns with FIASSE's principles by emphasizing the integration of security into the software development lifecycle.

The NCSC's [Software Security Code of Practice](https://www.ncsc.gov.uk/collection/software-security-code-of-practice-implementation-guidance) defines desired outcomes and some key strategies. While FIASSE framework focuses on first-level follow-on principles and strategies for achieving securable outcomes, intended for Development and Assurance teams to align with business strategies. SSEM specifies the attributes that are used to produce the desired outcomes, and the FIASSE methodology provides practical guidance for implementing these attributes in software engineering practices.

Carnegie Mellon University's [CERT](https://www.cert.org/) is a set of language-level rules providing both "what not to do" examples showing vulnerable code patterns and "what to do" examples. FIASSE complements these rules by providing a principled approach covering areas where rules do not by helping programmers to understand the "why?" behind securable code.

## Contributing

Contributions to improve documentation and examples are welcome. Please see our [contributing guidelines](CONTRIBUTING.md) for details.

## License

Attribution 4.0 International (CC BY 4.0) - see the [LICENSE](licence.txt) file for details.
