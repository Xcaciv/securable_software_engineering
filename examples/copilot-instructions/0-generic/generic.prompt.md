Generate a copilot-instructions.md for <curent language>.

Your task is to create a comprehensive `copilot-instructions.md` file for secure <curent language> development, combining high-level security principles with specific, actionable rules.

1.  **Foundation:** 
    *   Fetch the FIASSE RFC to establish guiding principles for generating "securable" software. @fetch https://raw.githubusercontent.com/Xcaciv/securable_software_engineering/refs/heads/main/docs/FIASSE-RFC.md
    *   Generate Instructions: The instructions should be based on the **Securable Software Engineering Model (SSEM)**, focusing on influencing code generation at a fundamental level rather than just listing rules. The core SSEM pillars are **Maintainability, Trustworthiness, and Reliability**.

2.  **<curent language or framework> Specialization:** Enhance the foundational principles with specific, modern <curent language> security practices.
    *   Fetch the **OWASP <curent language> Security Cheat Sheet**: `@fetch https://raw.githubusercontent.com/OWASP/CheatSheetSeries/refs/heads/master/cheatsheets/`(link to your language cheatsheet)
    *   From the cheat sheet, extract and include guidelines applicable to **<curent language version> and later**. Focus on areas like Identity, authorization attributes, secure cookie configuration, modern cryptography, secrets management (Vault), structured logging, injection prevention, XSS protection, secure serialization with JSON, and proper security header configuration.

3.  **Structure:** Organize the final `copilot-instructions.md` file with the general SSEM principles first, followed by a clearly marked section for the specific <curent language> guidance.

The final output should be a single, well-structured markdown file that guides Copilot to produce code that is securable by design.