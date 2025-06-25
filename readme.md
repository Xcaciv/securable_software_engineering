# A Framework for Integrating Application Security into Software Engineering (FIASSE)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Note:** This repository is an ongoing work. Contributions are welcome!

## Overview

This repository contains resources and materials for the Framework for Integrating Application Security into Software Engineering (FIASSE, pronounced /feiz/). FIASSE promotes a **developer-centric approach** to build **securable** software — recognizing that security is a dynamic, ongoing process like development. It introduces the Securable Software Engineering Model (SSEM) as a **common design language** that uses established software engineering terms to integrate security seamlessly into the development lifecycle, aiming to build resilient applications that protect data and withstand threats.

## Purpose

To provide practical guidelines that **empower developers** to create securable software without requiring deep security expertise, and to guide security professionals in effectively integrating security into software engineering. FIASSE achieves this through a **Software Engineering lens**, reducing cognitive load and fostering collaboration between development and security teams.

## Key Principles

- **The Securable Paradigm**: Acknowledging that software security is a dynamic, ongoing process, not a static "secure" state. Focuses on building inherent qualities into software to adapt to evolving threats.
- **Developer-Centric Security**: Empowering software engineers to autonomously build securable systems using familiar software engineering principles, rather than requiring them to adopt a penetration tester's mindset.
- **SSEM as a Common Design Language**: Utilizing the Securable Software Engineering Model (SSEM) which employs established software engineering terms (e.g., Analyzability, Modifiability, Testability) to define and discuss security attributes, making security more accessible to developers.
- **Aligning Security with Development & Business Goals**: Integrating security considerations seamlessly into the SDLC and ensuring that security efforts support overarching business objectives and risk appetite.
- **Resiliently Add Computing Value**: Ensuring software not only meets functional requirements but also possesses securable qualities that allow it to adapt, persist, and maintain integrity over time and under stress.
- **Requirements as a First-Class Citizen in AppSec**: Grounding secure software engineering in clearly defined security expectations and requirements from the outset.

## Complementary Resources

This repository complements the soon to be established [FIASSE website](https://fiasse.org).
This framework is focused on Software Engineering and is complemented by assurance frameworks from OWASP:

- Assurance example: [OWASP Software Assurance Reference Model (SARM)](https://owasp.org/www-project-software-assurance-reference-model/)
- Assurance verification: [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
- Assurance maturity: [OWASP Software Assurance Maturity Model (SAMM)](https://owasp.org/www-project-software-assurance-maturity-model/)

## Repository Contents

- Definition and Documentation of the Securable Software Engineering Model (SSEM)
- Implementation guides for the FIASSE methodology
- Examples of secure coding requirements and practices including Generative AI artifacts

## Getting Started

1. Review the documentation in the `/docs` directory
2. Explore the examples in the `/examples` directory

## Summary

This source defines securable software as systems designed for resilience and adaptability, emphasizing that true security is an ongoing process, not a static achievement. It introduces the Securable Software Engineering Model (SSEM), which frames security not as a separate discipline but as an inherent quality of well-engineered software, focusing on attributes like Maintainability, Trustworthiness, and Reliability (including Resilience). The FIASSE RFC advocates for integrating security practices directly into the development workflow—moving from a "security as an afterthought" approach to a proactive, collaborative model where product owners, developers, and security professionals work together from the earliest stages of design, particularly through collaborative threat modeling and by applying concepts like the "jellybean analogy" for managing flexibility and control. Ultimately, the goal shifts from an impossible "zero breaches" to reducing the probability of material impact from cyber events, empowering all stakeholders to contribute to building more robust, resilient, and inherently securable systems.

## Contributing

Contributions to improve documentation and examples are welcome. Please see our [contributing guidelines](CONTRIBUTING.md) for details.

## License

Attribution 4.0 International (CC BY 4.0) - see the [LICENSE](licence.txt) file for details.
