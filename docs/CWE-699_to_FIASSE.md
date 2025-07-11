# Comprehensive CWE-699 to FIASSE SSEM Mapping Table

| CWE Category (Base/Class) | Example CWEs | SSEM Attribute(s) | FIASSE RFC Section(s) |
| :-- | :-- | :-- | :-- |
| **API / Function Errors (CWE-1228)** | 242, 676, 474 | Maintainability (Analyzability, Modifiability) | §3.2.1.1, §3.2.1.2, §6.4 |
| **Audit / Logging Errors (CWE-1210)** | 117, 222, 778 | Trustworthiness (Accountability) | §3.2.2.2, §6.1.2 |
| **Authentication Errors (CWE-1211)** | 295, 301, 306 | Trustworthiness (Authenticity) | §3.2.2.3, §6.4.1, §6.2 |
| **Authorization Errors (CWE-1212)** | 425, 639, 862 | Trustworthiness (Confidentiality, Accountability) | §3.2.2.1, §3.2.2.2, §6.1 |
| **Bad Coding Practices (CWE-1006)** | 489, 561, 807 | Maintainability (Testability, Analyzability) | §3.2.1.3, §4.3 |
| **Behavioral Problems (CWE-438)** | 691, 697 | Reliability (Integrity) | §3.2.3.2, §6.4 |
| **Business Logic Errors (CWE-840)** | 841, 842 | Trustworthiness (Integrity) | §5, §6.3 |
| **Communication Channel Errors (CWE-417)** | 118, 353, 441 | Reliability (Availability, Integrity) | §3.2.3.1, §3.2.3.2, §6.4.1 |
| **Complexity Issues (CWE-1226)** | 397, 710 | Maintainability (Analyzability) | §3.4.1 |
| **Concurrency Issues (CWE-557)** | 412, 820 | Reliability (Resilience) | §3.2.3.3, §6.4 |
| **Credentials Management (CWE-255)** | 259, 798 | Trustworthiness (Confidentiality) | §3.2.2.1, §6.5, §6.4.1 |
| **Cryptographic Issues (CWE-310) / Key Management (CWE-320)** | 326, 327, 330 | Trustworthiness (Confidentiality, Authenticity) | §3.2.2.1, §3.2.2.3, §8.1.5 |
| **Data Integrity Issues (CWE-1214)** | 345, 346 | Reliability (Integrity) | §3.2.3.2, §6.4 |
| **Data Validation Issues (CWE-1215)** | 20, 116, 1188 | Reliability (Integrity) | §6.4.1, §3.2.3.2 |
| **Memory Errors (CWE-1218)** | 119, 787 | Reliability (Resilience, Integrity) | §3.2.3.2, §3.2.3.3, §6.4 |
| **Numeric Errors (CWE-189)** | 190, 191 | Reliability (Integrity) | §3.2.3.2, §6.4 |
| **Pointer Issues (CWE-465)** | 466, 467 | Reliability (Resilience) | §3.2.3.3, §6.4 |
| **Resource Management Errors (CWE-399)** | 400, 401, 404 | Reliability (Availability, Resilience) | §3.2.3.1, §3.2.3.3, §6.4 |
| **State Issues (CWE-371)** | 372, 374 | Reliability (Integrity, Resilience) | §3.2.3.2, §3.2.3.3, §6.4 |
| **String Errors (CWE-133)** | 134, 135 | Reliability (Integrity) | §3.2.3.2, §6.4 |
| **Type Errors (CWE-136)** | 843, 844 | Reliability (Integrity) | §3.2.3.2, §6.4 |
| **User Interface Security Issues (CWE-355)** | 451, 454 | Trustworthiness (Authenticity, Accountability) | §3.2.2, §6.3 |
| **Configuration Errors (CWE-16)** | 260, 276, 494 | Trustworthiness (Confidentiality, Accountability) | §3.2.2.1, §3.2.2.2, §6.5 |
| **Code Injection (CWE-74)** | 77, 78, 94 | Reliability (Integrity) | §6.4.1, §3.2.3.2 |
| **Path Traversal (CWE-22)** | 23, 24 | Trustworthiness (Confidentiality) | §3.2.2.1, §6.4.1 |
| **Cross-Site Scripting (CWE-79)** | 80, 81 | Trustworthiness (Confidentiality, Authenticity) | §3.2.2.1, §3.2.2.3, §6.4.1 |
| **Improper Input Handling (CWE-20)** | 20, 74, 77 | Reliability (Integrity) | §6.4.1, §3.2.3.2 |
| **Improper Output Handling (CWE-116)** | 116, 117 | Trustworthiness (Confidentiality, Accountability) | §3.2.2.1, §3.2.2.2, §6.4.1 |
| **Session Management Errors (CWE-384)** | 613, 614 | Trustworthiness (Authenticity, Confidentiality) | §3.2.2.3, §3.2.2.1, §6.4.1 |
| **Improper Access Control (CWE-284)** | 285, 287, 639 | Trustworthiness (Confidentiality, Accountability) | §3.2.2.1, §3.2.2.2, §6.1 |
| **Improper Error Handling (CWE-388)** | 390, 391 | Maintainability (Analyzability), Trustworthiness (Accountability) | §3.2.1.1, §3.2.2.2, §6.4 |
| **Race Conditions (CWE-362)** | 364, 366 | Reliability (Resilience) | §3.2.3.3, §6.4 |
| **Improper Certificate Validation (CWE-295)** | 297, 298 | Trustworthiness (Authenticity) | §3.2.2.3, §8.1.5 |
| **Insecure Dependency (CWE-1104)** | 1104, 829 | Maintainability (Modifiability), Trustworthiness (Confidentiality) | §3.2.1.2, §3.2.2.1, §6.5 |
| **Improper Initialization (CWE-665)** | 666, 667 | Reliability (Integrity, Resilience) | §3.2.3.2, §3.2.3.3, §6.4 |
| **Improper Resource Shutdown or Release (CWE-404)** | 404, 405 | Reliability (Availability, Resilience) | §3.2.3.1, §3.2.3.3, §6.4 |
| **Improper Neutralization of Special Elements (CWE-707)** | 74, 78, 79 | Reliability (Integrity), Trustworthiness (Confidentiality) | §6.4.1, §3.2.3.2, §3.2.2.1 |
| **Improper Restriction of Operations within the Bounds of a Memory Buffer (CWE-119)** | 120, 121 | Reliability (Resilience, Integrity) | §3.2.3.3, §3.2.3.2, §6.4 |
| **Improper Validation of Array Index (CWE-129)** | 130, 131 | Reliability (Integrity) | §3.2.3.2, §6.4 |
| **Improper Handling of Exceptional Conditions (CWE-755)** | 456, 459 | Maintainability (Analyzability), Reliability (Resilience) | §3.2.1.1, §3.2.3.3, §6.4 |
| **Improper Privilege Management (CWE-269)** | 270, 271 | Trustworthiness (Accountability, Confidentiality) | §3.2.2.2, §3.2.2.1, §6.1 |

**Legend:**

- **SSEM Attributes:**
  - Maintainability: Analyzability, Modifiability, Testability
  - Trustworthiness: Confidentiality, Accountability, Authenticity
  - Reliability: Availability, Integrity, Resilience
- **FIASSE RFC Sections:**
  - §3.2.x: Core SSEM attribute definitions
  - §3.4.x: Measuring these attributes
  - §4.x, §5.x, §6.x: Practical guidance and anti-patterns

## How to Use This Table

1. **Find the CWE**: Use the CWE category or number.
2. **See the SSEM Attribute**: Understand which quality of securable software is at risk.
3. **Jump to the RFC Section**: Get actionable, developer-centric advice for remediation.

## Example: Applying the Mapping

**Suppose your SAST tool flags CWE-79 (Cross-Site Scripting):**

- **SSEM Attribute**: Trustworthiness (Confidentiality, Authenticity)
- **FIASSE RFC Sections**:
  - §3.2.2.1 (Confidentiality)
  - §3.2.2.3 (Authenticity)
  - §6.4.1 (Input Handling)

**Remediation (FIASSE approach):**

- Review input/output handling per §6.4.1.
- Ensure proper escaping and context-aware encoding.
- Add regression tests as per §3.2.1.3 (Testability).
- Use merge review checklists (§4.3) to verify no raw user input reaches output.

## Notes

- This mapping covers all major second-level categories in CWE-699. For any new or niche CWE, use the same logic: map to the SSEM attribute most directly affected, then consult the corresponding RFC section.
- For a full list of all 672 CWEs, see the [CWE-699 Software Development View](https://cwe.mitre.org/data/definitions/699.html).
