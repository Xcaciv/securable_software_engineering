# Guiding Principles for Generating Securable .NET Software

This document provides guiding principles for .NET development, based on the **Framework for Integrating Application Security into Software Engineering (FIASSE)** and the **Securable Software Engineering Model (SSEM)**. The goal is to influence code generation on a fundamental level to produce software that is inherently "securable"—adaptable and resilient to evolving threats.

The primary directive is to **"Resiliently add computing value."** This means generating code that is not only functional but also possesses intrinsic qualities that allow it to be maintained and secured over its lifecycle.

---

## The Securable Paradigm

Security is not a static state but a dynamic process. When generating code, prioritize qualities that allow the software to be evolved, corrected, and adapted to new threats efficiently and without introducing new vulnerabilities.

---

## The Securable Software Engineering Model (SSEM)

Focus on the following three core pillars of securable software when generating or modifying code.

### 1. Maintainability

**Goal:** Create code that can be easily understood, modified, and tested, as this is the foundation for long-term security.

-   **Analyzability:** Generate code that is simple, readable, and has low cyclomatic complexity. Use clear and consistent naming conventions. The easier the code is to understand, the easier it is to spot and fix security flaws.
-   **Modifiability:** Produce modular, loosely coupled, and highly cohesive code. This ensures that changes in one part of the system do not have unintended security consequences elsewhere.
-   **Testability:** Write code that is inherently testable. Use pure functions where possible and apply dependency injection. Code with high test coverage is more likely to be secure.

### 2. Trustworthiness

**Goal:** Create code that behaves as expected, protects sensitive data, and ensures that actions are legitimate and traceable.

-   **Confidentiality:** Protect data from unauthorized disclosure. Never hardcode secrets (credentials, API keys). Use placeholders for secrets and rely on secure configuration management or vault systems. Employ strong, modern encryption for data in transit and at rest.
-   **Authenticity & Accountability:** Ensure users and services are who they claim to be and that their actions are traceable. Implement strong authentication and authorization checks for all sensitive operations. Generate detailed audit logs for security-relevant events (e.g., login attempts, access control decisions, data modification).
-   **Integrity:** Protect data and system resources from unauthorized modification.

### 3. Reliability

**Goal:** Create code that operates correctly, resists failure, and can recover from attacks.

-   **Integrity (as part of Reliability):** All inputs are potential vectors for attack. Implement rigorous input validation at the boundaries of your application. Use parameterized queries and safe APIs to prevent injection attacks. Prefer safe serialization formats.
-   **Resilience:** Implement robust and graceful error handling. Fail safely without leaking sensitive information in error messages. Code should be resilient to unexpected inputs and states.
-   **Availability:** Ensure the system remains operational. Be mindful of resource consumption and potential denial-of-service vectors (e.g., unbounded operations, resource leaks).

---

## Language-Specific Guidance: C# and .NET (8.x and 9.x)

The following are specific rules and best practices for applying the SSEM principles in a .NET environment.

### Applying Trustworthiness

-   **Authentication:** Use **ASP.NET Core Identity** as the default for authentication. It provides secure password hashing (PBKDF2) and salt generation out of the box.
-   **Authorization:**
    -   Apply `[Authorize]` attributes to all controllers and endpoints by default. Use method-level or controller-level authorization as appropriate.
    -   When accessing resources by an ID, always verify that the authenticated user has the right to access or modify that specific resource.
-   **Session Management & Cookies:**
    -   When configuring cookies, always set `HttpOnly = true` and `Secure = true` (in production).
    -   Set a reasonable session timeout (`ExpireTimeSpan`) and disable sliding expiration (`SlidingExpiration = false`) unless there is a strong justification.
-   **Cryptography:**
    -   **Never write your own cryptographic functions.**
    -   For password hashing outside of ASP.NET Core Identity, use `Microsoft.AspNetCore.Cryptography.KeyDerivation.Pbkdf2`.
    -   For symmetric encryption, use `System.Security.Cryptography.AesGcm`. Ensure a unique nonce is used for every encryption operation.
    -   Use the built-in Data Protection APIs (`IDataProtector`) for most encryption and decryption tasks, as it handles key management and rotation automatically.
-   **Secrets Management:** Never hardcode secrets. Use the `secrets.json` file for local development and Azure Key Vault or another secure vault for production environments.
-   **Logging:** Use the `ILogger` interface for structured logging. Ensure that sensitive data (passwords, API keys, PII) is never logged. Log failed login attempts and access control failures.

### Applying Reliability

-   **Input Validation & Injection Prevention:**
    -   **SQL Injection:** Use Entity Framework Core with parameterized queries. Never use string concatenation or interpolation to build SQL queries.
    -   **Cross-Site Scripting (XSS):** Razor views in ASP.NET Core automatically encode output, which prevents XSS. Do not use `@Html.Raw()` unless the data is from a trusted source and has been sanitized. Implement a strict Content Security Policy (CSP).
    -   **OS Command Injection:** When using `System.Diagnostics.Process.Start`, do not pass untrusted input directly as arguments. Validate all inputs against a strict allowlist.
-   **Serialization:**
    -   **Never use `BinaryFormatter`**. It is insecure and obsolete.
    -   Use `System.Text.Json` for all JSON serialization and deserialization. It is memory-safe and high-performance. Avoid `Newtonsoft.Json`'s `TypeNameHandling` features, which can lead to deserialization vulnerabilities.
-   **Error Handling & Headers:**
    -   Ensure `app.UseDeveloperExceptionPage()` is only used in the development environment.
    -   Implement security headers. In `Startup.cs` or `Program.cs`, use `app.UseHsts()`, `app.UseHttpsRedirection()`, and add headers like `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, and a Content Security Policy.
-   **Anti-Forgery Tokens:** For web applications, use the built-in anti-forgery token support. Add `services.AddMvc(options => { options.Filters.Add(new AutoValidateAntiforgeryTokenAttribute()); });` to automatically protect against Cross-Site Request Forgery (CSRF) attacks on all non-GET requests.

---

By applying these SSEM principles and .NET-specific guidelines, you will help produce code that is not just "patched" against current vulnerabilities but is fundamentally more securable by design.