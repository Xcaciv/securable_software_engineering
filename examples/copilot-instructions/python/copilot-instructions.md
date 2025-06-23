# Copilot Instructions for Securable Python Development

This document provides guidance for generating "securable" Python code, based on the principles of the **Framework for Integrating Application Security into Software Engineering (FIASSE)** and the **Securable Software Engineering Model (SSEM)**. The goal is to produce code that is not just "secure" at a point in time, but "securable" by design, meaning it is maintainable, trustworthy, and reliable.

## Core SSEM Principles

These principles should guide the generation of all code, regardless of the specific language or framework.

### 1. Maintainability

Code must be easy to understand, modify, and test. This is the foundation of securability.

*   **Analyzability:**
    *   Generate well-commented code that clearly explains the "why" behind the logic, not just the "what".
    *   Use clear and consistent naming conventions (PEP 8 for Python).
    *   Keep functions and classes small and focused on a single responsibility.
    *   Avoid code duplication.
*   **Modifiability:**
    *   Produce modular code with low coupling and high cohesion.
    *   Use dependency injection and interfaces to decouple components.
    *   Avoid hardcoding configuration values.
*   **Testability:**
    *   Generate code that is easy to unit test.
    *   Functions should have clear inputs and outputs and minimize side effects.
    *   When generating code, also generate corresponding unit tests that cover valid inputs, invalid inputs, and edge cases.

### 2. Trustworthiness

The system should operate as expected and protect sensitive data.

*   **Confidentiality:**
    *   Protect sensitive data from unauthorized access.
    *   Use modern, strong cryptography for data in transit and at rest.
    *   Implement the principle of least privilege.
*   **Accountability:**
    *   Ensure that actions can be traced to a specific entity.
    *   Implement robust logging and auditing.
*   **Authenticity:**
    *   Verify the identity of users and systems.
    *   Use strong authentication mechanisms, such as multi-factor authentication.
    *   Ensure the integrity of data and communications using digital signatures and certificates.

### 3. Reliability

The system should operate consistently and predictably, even under adverse conditions.

*   **Availability:**
    *   Design the system to be resilient to denial-of-service attacks.
    *   Implement mechanisms for quick recovery from failures.
*   **Integrity:**
    *   Protect data from unauthorized modification or corruption.
    *   Use cryptographic hashing and checksums to verify data integrity.
    *   Implement strong input validation at all trust boundaries.
*   **Resilience:**
    *   Write defensive code that anticipates and handles unexpected inputs and errors gracefully.
    *   Implement robust error handling and recovery mechanisms.
    *   Define clear trust boundaries and enforce strict controls on data and process execution at these boundaries.

---

## Python-Specific Guidance (Python 3.12+)

This section provides specific rules and best practices for secure Python development.

### Identity and Authorization

*   Use modern identity and access management (IAM) libraries like `Authlib` or `FastAPI`'s built-in security features.
*   Implement attribute-based access control (ABAC) or role-based access control (RBAC) for fine-grained authorization.
*   Do not hardcode credentials. Use a secrets management solution like HashiCorp Vault or AWS Secrets Manager.

### Secure Cookie Configuration

*   When using cookies for session management, set the `Secure`, `HttpOnly`, and `SameSite=Strict` attributes.
*   Use a short expiration time for session cookies.
*   Regenerate the session ID after a user authenticates.

### Modern Cryptography

*   Use the `cryptography` library for all cryptographic operations.
*   Use strong, modern algorithms like AES-256-GCM for symmetric encryption and RSA with OAEP padding for asymmetric encryption.
*   Avoid using outdated or weak algorithms like DES, RC4, or MD5.

### Secrets Management

*   Use the `hvac` library to interact with HashiCorp Vault for secrets management.
*   Store secrets in Vault and retrieve them at runtime. Do not store secrets in configuration files or source code.

### Structured Logging

*   Use a structured logging library like `structlog` to produce machine-readable logs.
*   Log all security-relevant events, including authentication successes and failures, access control decisions, and input validation failures.
*   Do not log sensitive information, such as passwords or API keys.

### Injection Prevention

*   Use parameterized queries or Object-Relational Mapping (ORM) libraries like SQLAlchemy to prevent SQL injection.
*   Do not use `eval()` or `exec()` with untrusted input.
*   Sanitize all user input before using it in shell commands or other contexts where it could be interpreted as code.

### Cross-Site Scripting (XSS) Protection

*   Use a templating engine like Jinja2 that provides automatic output escaping to prevent XSS.
*   Set the `Content-Security-Policy` (CSP) header to restrict the sources of content that can be loaded by the browser.

### Secure Serialization

*   Use JSON for data serialization. Avoid using `pickle`, as it can execute arbitrary code.
*   If you must use `pickle`, only unpickle data from a trusted source.

### Security Headers

*   Set the following security headers in all HTTP responses:
    *   `Strict-Transport-Security` (HSTS)
    *   `X-Content-Type-Options`
    *   `X-Frame-Options`
    *   `X-XSS-Protection`
    *   `Content-Security-Policy`
    *   `Referrer-Policy`

