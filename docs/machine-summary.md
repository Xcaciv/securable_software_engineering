# Guidance for Generating Securable Software Based on FIASSE/SSEM

This summary is intended to guide an LLM to generate software that is *inherently securable* or *securable by construction*. This is *securability engineering*.

## 0. Core Framing from FIASSE

Use the **Securable Principle** as the primary framing for generated code:

- Do not treat security as a binary state.
- Prefer the question: "Do we meet our defined goals for this securable attribute?"
- Build software with inherent qualities that are durable under change.

Use **Transparency** as a core strategy across all attributes:

- Favor code and system behavior that are observable and auditable to authorized parties.
- Prefer structured logging and instrumentation at trust boundaries.
- Remember transparency is constrained by **Confidentiality**.

The core attribute groups remain:

- **Maintainability**
- **Trustworthiness**
- **Reliability**

## 1. Maintainability

Maintainability is the degree to which software can be modified effectively and efficiently by intended maintainers (ISO/IEC 25010:2011).

### 1.1. Analyzability

Definition (ISO 25010-aligned): the degree to which impact of change and causes of failures can be diagnosed efficiently.

LLM guidance:

- Generate code with clear naming, bounded function/class size, and low complexity.
- Minimize duplication and avoid hidden control flow.
- Prefer comments that explain *why* a decision exists.
- Keep component boundaries understandable so impact analysis is fast.

### 1.2. Modifiability

Definition (ISO 25010-aligned): the degree to which software can be modified without introducing defects or degrading quality.

LLM guidance:

- Favor low coupling and coherent module boundaries.
- Use abstractions so changes stay local and avoid cascading edits.
- Preserve existing behavior with focused tests when modifying code.
- Keep security-critical logic explicit so remediation can be done quickly.

### 1.3. Testability

Definition (ISO 25010-aligned): the degree to which test criteria can be established and tests can be executed effectively.

LLM guidance:

- Prefer deterministic units with clear inputs/outputs.
- Enable isolated testing by injecting dependencies.
- Generate tests for expected behavior, edge cases, and error paths.
- Keep unit coupling low so tests can be authored and run quickly.

## 2. Trustworthiness

Trustworthiness is the degree to which a system can be expected to satisfy requirements, including security requirements (RFC 4949).

### 2.1. Confidentiality

Definition: data is disclosed only to authorized entities (RFC 4949).

LLM guidance:

- Enforce authorization before sensitive operations.
- Avoid exposing secrets or sensitive fields in logs, errors, and URLs.
- Use established cryptographic libraries and modern algorithms when needed.
- Respect trust boundaries where data classification and access rules differ.

### 2.2. Accountability

Definition: actions of an entity are uniquely traceable to that entity (RFC 4949).

LLM guidance:

- Create immutable, structured audit trails for security-sensitive actions.
- Capture who, what, where, when, and outcome in audit events.
- Preserve log integrity and avoid log-forging vectors.
- Ensure attribution remains verifiable for incident response.

### 2.3. Authenticity

Definition: an entity is what it claims to be (ISO/IEC 27000:2018).

LLM guidance:

- Use strong authentication and robust credential/session handling.
- Verify signatures and authenticity claims before trusting payloads.
- Use non-repudiation-supporting mechanisms where appropriate (for example, signed events).
- Log authentication/authorization events to support investigation and trust.

## 3. Reliability

Reliability is the degree to which software performs specified functions under specified conditions for a specified period (ISO/IEC 25010:2011).

### 3.1. Availability

Definition: authorized entities can access and use the system on demand (RFC 4949).

LLM guidance:

- Design for graceful degradation under stress and partial failure.
- Use timeouts, backoff, and recovery paths for dependent services.
- Ensure resource cleanup and bounded resource usage.
- Favor patterns that reduce outage blast radius.

### 3.2. Integrity

Definition: data is not changed, destroyed, or lost in an unauthorized/accidental manner, and the system runs without unauthorized manipulation (RFC 4949).

LLM guidance:

- Apply the **Derived Integrity Principle**: derive critical business/state values in trusted server context, never directly from client input.
- Canonicalize/normalize, sanitize, and validate input at trust boundaries.
- Preserve authoritative state transitions in controlled server logic.
- Use integrity checks and access control to protect data and state.

### 3.3. Resilience

Definition: ability to continue operation through failures and recover to full operation (RFC 4949).

LLM guidance:

- Use defensive coding to keep execution predictable under abnormal conditions.
- Implement robust error handling and explicit recovery behavior.
- Encode/escape output for destination context to avoid interpreter injection.
- Build with fault tolerance and clear trust boundaries.

## 4. Trust Boundary Input Pattern (Section 6.4.1 Aligned)

When generating input-handling code at trust boundaries, prefer this sequence:

1. Canonicalize/normalize input into expected form.
2. Sanitize potentially harmful content for the context.
3. Validate against explicit allowlisted criteria.
4. Ignore or reject out-of-scope request fields based on sensitivity.
5. Log anomalous boundary events with useful context.
