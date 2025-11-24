# Guidance for Generating Securable Software based on FIASSE/SSEM

This document provides a summary of the Securable Software Engineering Model (SSEM) attributes, tailored for guiding a Large Language Model (LLM) like Copilot to generate code that is inherently more securable. The core principle is that securable software is built upon the pillars of **Maintainability**, **Trustworthiness**, and **Reliability**.

## 1. Maintainability

**Principle**: Code that cannot be changed with confidence is not securable. The LLM should generate code that is easy for humans to understand, modify, and test.

### 1.1. Analyzability

**Definition**: The ease with which code can be understood to diagnose issues or assess the impact of changes.

**LLM Guidance**:

- **Generate Clear Code**: Produce code with meaningful variable/function names and comprehensive comments that explain the "why," not just the "what."
- **Control Complexity**: Keep functions and classes small, focused on a single responsibility, and with low cyclomatic complexity.
- **Adhere to Standards**: Follow established language-specific style guides (e.g., PEP 8 for Python, GoF patterns for Java) to ensure consistency.
- **Avoid Duplication**: Refactor repeated logic into reusable functions or classes.

*Example Prompt Fragment*: "...generate a Python function that is highly analyzable, with clear comments explaining the logic, low complexity, and adherence to PEP 8."

### 1.2. Modifiability

**Definition**: The ability to modify code without introducing defects or degrading quality.

**LLM Guidance**:

- **Promote Modularity**: Generate modular code with low coupling (minimal dependencies) and high cohesion (related logic is grouped together).
- **Use Abstractions**: Employ interfaces and abstract classes to decouple implementation details from the core logic.
- **Externalize Configuration**: Avoid hardcoding values like connection strings, API keys, or feature flags. Generate code that reads them from configuration files or environment variables.

*Example Prompt Fragment*: "...design a Java class for payment processing that is easily modifiable. Use an interface for the payment gateway so different gateways can be added later without changing the core class."

### 1.3. Testability

**Definition**: The ease with which code can be tested to verify it meets requirements.

**LLM Guidance**:

- **Write Pure Functions**: Where possible, generate functions with clear inputs and outputs that have no side effects.
- **Enable Dependency Injection**: Generate code that allows dependencies to be "injected" (passed as parameters) rather than instantiated internally. This makes mocking and testing in isolation possible.
- **Generate Unit Tests**: When generating a function or class, also generate a corresponding set of unit tests that cover valid inputs, edge cases, and error conditions.

*Example Prompt Fragment*: "...write a Go function to validate an email address, and also generate a comprehensive suite of unit tests for it using the standard `testing` package. The function should not have external dependencies."

## 2. Trustworthiness

**Principle**: The system should operate as expected and meet its security requirements. The LLM should generate code that protects data and ensures actions are authentic and traceable.

### 2.1. Confidentiality

**Definition**: Ensuring data is not disclosed to unauthorized entities.

**LLM Guidance**:

- **Implement Access Controls**: Generate code that enforces authorization checks before accessing data or performing sensitive actions.
- **Use Modern Cryptography**: When encryption is needed, use strong, current, and well-vetted cryptographic libraries and algorithms. Avoid generating custom crypto implementations.
- **Prevent Data Leakage**: Ensure sensitive data is not exposed in logs, error messages, or URLs.

*Example Prompt Fragment*: "...generate a C# code snippet to retrieve user profile data. Ensure it first checks if the currently authenticated user has the 'Admin' role or if their ID matches the requested profile ID."

### 2.2. Accountability

**Definition**: Ensuring actions of an entity can be traced uniquely to that entity.

**LLM Guidance**:

- **Generate Detailed Audit Logs**: For sensitive operations (e.g., login, data modification, permission changes), generate structured logs that include who performed the action, what was changed, the timestamp, and the source IP address.
- **Ensure Log Integrity**: Do not include user-controlled data in a way that could corrupt or manipulate the log format (log injection).

*Example Prompt Fragment*: "...when a user's password is changed, generate a structured JSON log entry for accountability that includes the user ID, a static event message, and the timestamp."

### 2.3. Authenticity

**Definition**: Ensuring an entity (user or system) is what it claims to be.

**LLM Guidance**:

- **Use Secure Authentication Mechanisms**: Implement standard, secure authentication patterns. For tokens, use libraries that properly validate signatures and claims (e.g., expiration).
- **Verify Data Integrity**: When receiving data with a signature (like a JWT or a webhook payload), generate code to cryptographically verify the signature before trusting the content.

*Example Prompt Fragment*: "...generate a Node.js function using the 'jsonwebtoken' library to verify a JWT. It must validate the signature against a secret from an environment variable and check the token's expiration."

## 3. Reliability

**Principle**: The system should perform its specified functions correctly and consistently, even under adverse conditions or attack.

### 3.1. Availability

**Definition**: The system is accessible and usable upon demand by an authorized entity.

**LLM Guidance**:

- **Implement Timeouts and Retries**: For network requests to external services, generate code that includes sensible timeouts and a retry mechanism with exponential backoff.
- **Handle Resource Management**: Ensure resources like database connections or file handles are properly closed in all execution paths (e.g., using `try-with-resources` in Java or `defer` in Go).

*Example Prompt Fragment*: "...generate a Python function using the `requests` library to call an external API. It should have a 5-second timeout and retry up to 3 times on failure."

### 3.2. Integrity

**Definition**: Data and systems are protected from unauthorized or accidental modification.

**LLM Guidance**:

- **Apply the Derived Integrity Principle**: Never trust client-supplied data for critical logic. Generate code that derives or recalculates authoritative values (like price, permissions, or object state) on the server-side.
- **Use Parameterized Queries**: To prevent SQL injection, exclusively use parameterized queries or prepared statements for database interactions. Never generate code that concatenates user input into SQL strings.
- **Validate All Inputs**: Generate strict, allowlist-based validation for all data crossing a trust boundary.

*Example Prompt Fragment*: "...generate a PHP script to update a product's inventory. The product ID and new quantity should be passed as parameters to a prepared statement. Do not trust any price information from the client."

### 3.3. Resilience

**Definition**: The ability of a system to operate during and recover from failures or attacks. This is achieved through **defensive coding**.

**LLM Guidance**:

- **Implement Robust Error Handling**: Generate code that anticipates and gracefully handles potential errors (e.g., invalid input, network failures, file-not-found) instead of crashing.
- **Sanitize Input and Encode Output**: Generate code that validates and sanitizes all input at trust boundaries. Ensure all data written to a different context (HTML, SQL, shell) is properly encoded to prevent injection attacks.
- **Fail Securely**: In case of an unrecoverable error, ensure the system fails to a secure state that does not expose sensitive information.

*Example Prompt Fragment*: "...generate a Java servlet that reads a 'username' parameter. It must validate the input against a strict alphanumeric pattern and use output encoding to display it safely on an HTML page to prevent XSS."
