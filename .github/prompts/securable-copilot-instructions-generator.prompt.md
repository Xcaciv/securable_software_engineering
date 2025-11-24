---
mode: "agent"
tools: ['codebase', 'editFiles', 'extensions', 'fetch', 'search']
description: "Enhances copilot-instructions with securable software engineering principles and specific security practices."
---
Your task is to create or update a copilot instructions file. (if an instructions file is not given in the context update or create `copilot-instructions.md`) Combine high-level security principles with specific, actionable rules, and include language- or framework-specific security practices as appropriate for the codebase.

1.  **Foundation:** 
    *   Fetch the FIASSE RFC to establish guiding principles for generating "securable" software. @fetch https://raw.githubusercontent.com/Xcaciv/securable_software_engineering/refs/heads/main/docs/FIASSE-RFC.md
    *   Generate Instructions: The instructions should be based on the **Securable Software Engineering Model (SSEM)**, focusing on influencing code generation at a fundamental level rather than just listing rules. The core SSEM pillars are **Maintainability, Trustworthiness, and Reliability**.

2.  **Specialization:** Enhance the foundational principles with specific, modern security practices.
    *   Fetch the apropriate **OWASP Security Cheat Sheet** for the context if it exists: `@fetch https://raw.githubusercontent.com/OWASP/CheatSheetSeries/refs/heads/master/cheatsheets/`
    *   From the cheat sheet, extract and include guidelines applicable to **the current language version or later**. Focus on areas like Identity, authorization attributes, secure cookie configuration, modern cryptography, secrets management (Vault), structured logging, injection prevention, XSS protection, secure serialization with JSON, and proper security header configuration.

3.  **Structure:** Organize the final `copilot-instructions.md` file with the general SSEM principles first, followed by a clearly marked section for the specific current language or framework guidance.

The final output should be a single, well-structured markdown file that guides Copilot to produce code that is securable by design.