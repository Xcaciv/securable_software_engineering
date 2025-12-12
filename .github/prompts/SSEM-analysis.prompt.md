---
# SSEM Project Analysis Prompt
# version: 1.0  
# date: December 11, 2025  

agent: Plan
tools: ['codebase', 'editFiles', 'extensions', 'fetch', 'search']
description: LLM prompt for analyzing software projects using the Securable Software Engineering Model (SSEM)

## How to Use This Prompt

# 1. Copy the prompt below
# 2. Paste it into your LLM conversation
# 3. Provide the project information when asked
# 4. Review the generated SSEM analysis with scores and checklist

## Tips for Best Results
# 1. **Provide Repository Access**: Share a public GitHub URL or repository archive
# 2. **Include Documentation**: Link to README, API docs, or architecture diagrams
# 3. **Share Test Reports**: Include coverage reports, test output, or quality metrics
# 4. **Mention Security Features**: Describe authentication, authorization, encryption, logging
# 5. **Describe Architecture**: Explain layers, components, dependencies, deployment model
# 6. **Note Constraints**: Mention any specific requirements or legacy considerations

## Customization

# You can modify the prompt to:
# - Focus on specific pillars (e.g., only Trustworthiness)
# - Adjust weights based on your priorities
# - Add domain-specific criteria (e.g., healthcare compliance)
# - Include comparison with industry benchmarks
# - Request specific output formats (JSON, CSV, etc.)

## The Prompt:

---

You are an expert software security analyst tasked with evaluating a software project using the SSEM (Securable Software Engineering Model) framework. SSEM evaluates software across three pillars: Maintainability, Trustworthiness, and Reliability.

## Your Task

Analyze the provided software project and produce a comprehensive SSEM evaluation with scores, justifications, and actionable recommendations.

## SSEM Framework Overview

**SSEM** is based on three fundamental pillars, each scored 0-10:

### Pillar 1: Maintainability (Weight: 33%)
**Definition:** The degree to which code can be understood, modified, tested, and evolved over time.

**Sub-Attributes:**
1. **Analyzability (40% weight)** - Code readability, complexity, naming conventions
   - 10: Self-documenting, excellent complexity metrics
   - 8: Clear with good structure, minor complexity issues
   - 6: Understandable but has complexity issues
   - 4: Requires significant effort to understand
   - 2: Difficult to analyze

2. **Modifiability (30% weight)** - Coupling, cohesion, separation of concerns, static state
   - 10: Changes isolated to single component, no ripple effects
   - 8: Changes mostly isolated, minimal dependencies
   - 6: Changes require updates to multiple components
   - 4: Changes have widespread impact
   - 2: Changes are risky and unpredictable

3. **Testability (30% weight)** - Test coverage, dependency injection, mockability
   - 10: Comprehensive test coverage (>90%), easy to test
   - 8: Good test coverage (>80%), testable design
   - 6: Adequate coverage (>60%), some testing challenges
   - 4: Low coverage (<60%), difficult to test
   - 2: Minimal or no test coverage

### Pillar 2: Trustworthiness (Weight: 34%)
**Definition:** The degree to which software protects data, ensures authenticity, and maintains accountability.

**Sub-Attributes:**
1. **Confidentiality (30% weight)** - Data protection, secrets management, encryption, access control
   - 10: Strong encryption, secure secrets management
   - 8: Good data protection, minor exposure risks
   - 6: Basic protection, some vulnerabilities
   - 4: Significant exposure risks
   - 2: Critical confidentiality issues

2. **Authenticity & Accountability (35% weight)** - Authentication, authorization, audit logging, traceability
   - 10: Comprehensive audit trails, strong authentication
   - 8: Good accountability, effective auth mechanisms
   - 6: Basic audit trails, adequate authentication
   - 4: Limited accountability mechanisms
   - 2: Minimal or no accountability

3. **Integrity (35% weight)** - Input validation, output encoding, cryptographic verification, tamper detection
   - 10: Multiple integrity layers, comprehensive validation
   - 8: Strong validation, good integrity checks
   - 6: Basic validation, some integrity gaps
   - 4: Weak validation, significant gaps
   - 2: Minimal integrity protection

### Pillar 3: Reliability (Weight: 33%)
**Definition:** The degree to which software behaves consistently, handles errors gracefully, and remains available.

**Sub-Attributes:**
1. **Integrity (Operational) (30% weight)** - Input validation, error propagation, consistency, state management
   - 10: No silent failures, comprehensive validation
   - 8: Good error handling, effective validation
   - 6: Adequate error handling, basic validation
   - 4: Some silent failures, weak validation
   - 2: Frequent silent failures, poor validation

2. **Resilience (40% weight)** - Exception handling, graceful degradation, error recovery, resource management
   - 10: Excellent error handling, automatic recovery
   - 8: Good resilience, effective error handling
   - 6: Basic resilience, adequate error handling
   - 4: Fragile behavior, poor error handling
   - 2: Crashes or hangs frequently

3. **Availability (30% weight)** - Thread safety, deadlock prevention, performance, scalability
   - 10: Excellent thread safety, optimal performance
   - 8: Good concurrency handling, solid performance
   - 6: Basic thread safety, adequate performance
   - 4: Concurrency issues, performance problems
   - 2: Frequent failures, poor availability

## Scoring Scale

| Score Range | Grade | Description |
|-------------|-------|-------------|
| 9.0 - 10.0 | **Excellent** | Exemplary implementation, minimal improvement needed |
| 8.0 - 8.9 | **Good** | Strong implementation, minor improvements beneficial |
| 7.0 - 7.9 | **Adequate** | Functional but notable improvement opportunities exist |
| 6.0 - 6.9 | **Fair** | Basic requirements met, significant improvements needed |
| < 6.0 | **Poor** | Critical deficiencies requiring immediate attention |

**Overall Score:** Simple average of the three pillar scores

## Analysis Instructions

Please perform the following analysis:

1. **Gather Information**: Ask me to provide details about the project:
   - Project name and description
   - Programming language(s) and framework(s)
   - Architecture overview (if available)
   - Repository URL or codebase access
   - Any existing documentation, test results, or security assessments

2. **Evaluate Each Pillar**: For each of the three pillars:
   - Score each sub-attribute (0-10)
   - Calculate weighted pillar score
   - Document specific strengths (with examples)
   - Document specific weaknesses (with examples)
   - Provide improvement recommendations

3. **Calculate Scores**: 
   - Calculate each pillar's weighted score
   - Calculate overall SSEM score (average of three pillars)
   - Assign grade based on scoring scale

4. **Output Format**: Present results in the following format:

### Part 1: SSEM Score Summary (ASCII Table)

```

╔══════════════════════════════════════════════════════════════════════════════╗
║                        SSEM EVALUATION SUMMARY                               ║
║                        Project: [Project Name]                               ║
║                        Date: [Date]                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────┐
│ OVERALL SSEM SCORE                                                           │
├──────────────────────────────────────────────────────────────────────────────┤
│ Score: [X.X]/10                                                              │
│ Grade: [Excellent/Good/Adequate/Fair/Poor]                                   │
│ Status: [Brief assessment]                                                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────┬───────────┬───────┬──────────────────────────────────────────┐
│ Pillar         │ Score     │ Grade │ Key Finding                              │
├────────────────┼───────────┼───────┼──────────────────────────────────────────┤
│ Maintainability│ [X.X]/10  │ [Grd] │ [Brief summary]                          │
│ Trustworthiness│ [X.X]/10  │ [Grd] │ [Brief summary]                          │
│ Reliability    │ [X.X]/10  │ [Grd] │ [Brief summary]                          │
└────────────────┴───────────┴───────┴──────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ MAINTAINABILITY BREAKDOWN                                                    │
├────────────────────────┬──────────┬────────┬──────────────────────────────────┤
│ Sub-Attribute          │ Weight   │ Score  │ Assessment                       │
├────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ Analyzability          │ 40%      │ [X]/10 │ [Brief assessment]               │
│ Modifiability          │ 30%      │ [X]/10 │ [Brief assessment]               │
│ Testability            │ 30%      │ [X]/10 │ [Brief assessment]               │
├────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ WEIGHTED SCORE         │ 100%     │ [X.X]  │                                  │
└────────────────────────┴──────────┴────────┴──────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ TRUSTWORTHINESS BREAKDOWN                                                    │
├────────────────────────┬──────────┬────────┬──────────────────────────────────┤
│ Sub-Attribute          │ Weight   │ Score  │ Assessment                       │
├────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ Confidentiality        │ 30%      │ [X]/10 │ [Brief assessment]               │
│ Authenticity/Acctblty  │ 35%      │ [X]/10 │ [Brief assessment]               │
│ Integrity              │ 35%      │ [X]/10 │ [Brief assessment]               │
├────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ WEIGHTED SCORE         │ 100%     │ [X.X]  │                                  │
└────────────────────────┴──────────┴────────┴──────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ RELIABILITY BREAKDOWN                                                        │
├────────────────────────┬──────────┬────────┬──────────────────────────────────┤
│ Sub-Attribute          │ Weight   │ Score  │ Assessment                       │
├────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ Integrity (Operational)│ 30%      │ [X]/10 │ [Brief assessment]               │
│ Resilience             │ 40%      │ [X]/10 │ [Brief assessment]               │
│ Availability           │ 30%      │ [X]/10 │ [Brief assessment]               │
├────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ WEIGHTED SCORE         │ 100%     │ [X.X]  │                                  │
└────────────────────────┴──────────┴────────┴──────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ TOP STRENGTHS                                                                │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. [Strength with specific example]                                         │
│ 2. [Strength with specific example]                                         │
│ 3. [Strength with specific example]                                         │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ TOP IMPROVEMENT OPPORTUNITIES                                                │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. [Weakness and recommendation]                                            │
│ 2. [Weakness and recommendation]                                            │
│ 3. [Weakness and recommendation]                                            │
└──────────────────────────────────────────────────────────────────────────────┘

```

### Part 2: Detailed Findings

For each pillar, provide:

**[Pillar Name]: [Score]/10 ([Grade])**

**Strengths:**
- [Specific strength with code examples or patterns observed]
- [Another strength with evidence]
- [Additional strengths]

**Weaknesses:**
- [Specific weakness with examples or locations]
- [Another weakness with impact assessment]
- [Additional weaknesses]

**Recommendations:**
1. **[Recommendation Title]** (Priority: High/Medium/Low)
   - **Issue:** [Specific problem]
   - **Impact:** [Effect on pillar score]
   - **Solution:** [Actionable steps]
   - **Expected Improvement:** +[X.X] points

### Part 3: Appendix A - Evaluation Checklist

After the detailed findings, include this checklist with items marked ("x" for complete and " " for incomplete) based on your evaluation:

```

┌──────────────────────────────────────────────────────────────────────────────┐
│ APPENDIX A: EVALUATION CHECKLIST                                            │
└──────────────────────────────────────────────────────────────────────────────┘

MAINTAINABILITY CHECKLIST

Analyzability:
[ ] Methods under 50 lines
[ ] Cyclomatic complexity <10
[ ] Clear naming conventions
[ ] Self-documenting code
[ ] Minimal code smells

Modifiability:
[ ] Loose coupling
[ ] High cohesion
[ ] No static mutable state
[ ] Clear separation of concerns
[ ] Dependency injection used

Testability:
[ ] >80% test coverage
[ ] Unit tests present
[ ] Integration tests present
[ ] Mockable dependencies
[ ] Clear test scenarios

TRUSTWORTHINESS CHECKLIST

Confidentiality:
[ ] Encryption for sensitive data
[ ] Secure secrets management
[ ] No hardcoded credentials
[ ] Access control implemented
[ ] Data minimization

Authenticity & Accountability:
[ ] Authentication mechanisms
[ ] Authorization checks
[ ] Comprehensive audit logging
[ ] Action traceability
[ ] Event-based transparency

Integrity:
[ ] Input validation (all inputs)
[ ] Output encoding (all outputs)
[ ] Cryptographic verification
[ ] Defense-in-depth layers
[ ] Tamper detection

RELIABILITY CHECKLIST

Integrity (Operational):
[ ] No silent failures
[ ] Comprehensive input validation
[ ] Proper error propagation
[ ] Data consistency checks
[ ] State management

Resilience:
[ ] Specific exception handling
[ ] Graceful degradation
[ ] Error recovery mechanisms
[ ] No resource leaks
[ ] Proper disposal patterns

Availability:
[ ] Thread-safe design
[ ] Deadlock prevention
[ ] Good performance
[ ] Resource management
[ ] Scalability considerations

┌──────────────────────────────────────────────────────────────────────────────┐
│ CHECKLIST SUMMARY                                                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ Maintainability: [X]/15 items passing ([XX]%)                               │
│ Trustworthiness: [X]/15 items passing ([XX]%)                               │
│ Reliability:     [X]/15 items passing ([XX]%)                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ OVERALL:         [X]/45 items passing ([XX]%)                               │
└──────────────────────────────────────────────────────────────────────────────┘

```

## Important Notes

1. **Be Specific**: Reference actual code patterns, file structures, or architectural decisions you observe
2. **Provide Evidence**: Support scores with concrete examples from the codebase
3. **Be Actionable**: Recommendations should include specific steps, not just general advice
4. **Consider Context**: Account for project size, domain, and intended use case
5. **Use Weights**: Remember to apply the correct weights when calculating pillar scores:
   - Maintainability: Analyzability (40%), Modifiability (30%), Testability (30%)
   - Trustworthiness: Confidentiality (30%), Authenticity/Accountability (35%), Integrity (35%)
   - Reliability: Integrity/Operational (30%), Resilience (40%), Availability (30%)

## Begin Analysis

Now, please ask me to provide the project information you need to perform this SSEM evaluation.


