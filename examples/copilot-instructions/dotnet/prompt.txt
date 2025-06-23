Generate a copilot-instructions.md for dotnet.

Your task is to create a comprehensive `copilot-instructions.md` file for secure .NET development, combining high-level security principles with specific, actionable rules.

1.  **Foundation:** 
    *   Fetch the FIASSE RFC to establish guiding principles for generating "securable" software. @fetch https://raw.githubusercontent.com/Xcaciv/securable_software_engineering/refs/heads/main/docs/FIASSE-RFC.md
    *   Generate Instructions: The instructions should be based on the **Securable Software Engineering Model (SSEM)**, focusing on influencing code generation at a fundamental level rather than just listing rules. The core SSEM pillars are **Maintainability, Trustworthiness, and Reliability**.

2.  **.NET Specialization:** Enhance the foundational principles with specific, modern .NET security practices.
    *   Fetch the **OWASP .NET Security Cheat Sheet**: `@fetch https://raw.githubusercontent.com/OWASP/CheatSheetSeries/refs/heads/master/cheatsheets/DotNet_Security_Cheat_Sheet.md`
    *   From the cheat sheet, extract and include guidelines applicable to **.NET 8.x/9.x and later**. Focus on areas like ASP.NET Core Identity, authorization attributes, secure cookie configuration, modern cryptography (`AesGcm`, `IDataProtector`), secrets management (Azure Key Vault), structured logging, injection prevention, XSS protection in Razor, secure serialization with `System.Text.Json`, and proper security header configuration.

3.  **Structure:** Organize the final `copilot-instructions.md` file with the general SSEM principles first, followed by a clearly marked section for the specific .NET guidance.

The final output should be a single, well-structured markdown file that guides Copilot to produce code that is securable by design.