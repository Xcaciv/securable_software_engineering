# Guiding Principles for Generating Securable Software

This document provides guiding principles based on the **Framework for Integrating Application Security into Software Engineering (FIASSE)** and the **Securable Software Engineering Model (SSEM)**. The goal is to influence code generation on a fundamental level to produce software that is inherently "securable"—adaptable and resilient to evolving threats.

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

By applying these SSEM principles, you will help produce code that is not just "patched" against current vulnerabilities but is fundamentally more securable by design.