# Developer API Security Checklist

A every-day-carry checklist developers can use independently to build secure APIs.

## Maintainability

- [ ] Modularize security logic (auth, validation, error handling) for clean reuse and updates.
- [ ] Centralize security configs under version control — no hardcoding.
- [ ] Standardize error/response schemas and log structures across services.
- [ ] Document decisions and security trade-offs using OpenAPI or Markdown files.
- [ ] Add regression tests for known vulnerabilities and past pentest findings.

## Resilience

- [ ] Apply **rate limiting and throttling** (per token/IP/etc.) with clear failure responses (`429`).
- [ ] Use **circuit breakers** and fallback logic for dependencies and external services.
- [ ] Gracefully handle errors without crashing; log details, return stable responses.
- [ ] Implement liveness/readiness **health checks** and configure upstream timeouts.
- [ ] Periodically **load test** and simulate failures to verify API behavior under stress.

## Authentication & Authorization

- [ ] Use **OAuth 2.0 with PKCE** or **OpenID Connect**; avoid Basic Auth.
- [ ] Enforce strong JWT validation (`alg`, expiration, issuer).
- [ ] Store secrets in a **vault** — never in code or configs.
- [ ] Apply **RBAC**: check user permissions on every request.
- [ ] Validate `redirect_uri` and use the `state` parameter in OAuth flows.
- [ ] Secure all endpoints by default; document exceptions explicitly.

## Data Protection

- [ ] Enforce **HTTPS (TLS 1.2 or higher)** and use strong cipher suites.
- [ ] Add **HSTS headers** with preload and `includeSubDomains`.
- [ ] Encrypt sensitive data at rest with **AES‑256 GCM** or equivalent.
- [ ] Don’t log or expose secrets, tokens, or PII in URLs or error messages.
- [ ] Use vetted cryptographic libraries (e.g. libsodium, BouncyCastle).

## Input Validation

- [ ] Validate **all inputs** server-side (headers, body, query, etc.).
- [ ] Use JSON Schema or shared validators across services.
- [ ] Enforce proper `Content-Type` and `Accept` headers.
- [ ] Use **parameterized queries** — never build SQL strings manually.
- [ ] Disable DTDs and external entities in XML parsers.

## Logging & Error Handling

- [ ] Log authentication failures, denied access, and system errors.
- [ ] Avoid logging secrets, passwords, or sensitive identifiers.
- [ ] Send users **generic error messages** (e.g., “Invalid input”); log details internally.
- [ ] Use **correlation IDs** in logs to trace request chains.

## Testing & Deployment

- [ ] Write tests for authentication, validation, and error-handling flows.
- [ ] Include negative tests (e.g., tampered tokens, malformed input).
- [ ] Store configs (e.g., allowed HTTP methods, token expiry) in version control.
- [ ] Keep dependencies updated; review security PRs with intention.

---

Encourage developers to treat this as part of their definition of done for every API. It’s fast, focused, and aligned with real-world threats.

