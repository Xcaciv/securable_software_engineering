# Developing Securable Code

Alton Crossley
Product Security Consultant
Guidepoint Security
Level: Intermediate

---

## Introduction: The Challenge of Secure Software

The Goal: Create software that **operates securely** and can be **configured securely** in an *intuitive* way.

The Problem: How do we give developers a way to **confidently achieve** this?

- Simply telling them they're doing a good job feels **disingenuous** and can trigger subconscious rejection.
- Security-centric **jargon** is often rooted in a testing mindset, which can be **alienating**.

The Solution: We can provide a framework using concepts they are already comfortable with.

---

## The Securable Principle

> There is no static state of secure.

This is the foundational concept.

- Security is **not a one-time checklist**; it's an ongoing characteristic of the software.
- Securable Code: Software that is built to be **secure from the start** and, crucially, can be ***kept* secure** as it evolves.

---

## Finding a Common Language: Beyond ISO 25010

- The Need: We require a model that is *familiar* to software engineers and **doesn't need "translation"** from security jargon.
- A Starting Point: ISO 25010 provides a complete Software Engineering context, and it does mention security.
- The Gap: The security-specific attributes in ISO 25010 don't cover all the qualities that are required to make software truly securable.

---

## The Securable Software Engineering Model (SSEM)

- This is where the **Securable Software Engineering Model (SSEM)** comes in.
- It is a core part of the **OWASP FIASSE project** (Framework for Integrating Application Security into Software Engineering).
- **SSEM's Purpose:**
  - To use standardized, well-known Software Engineering attributes to address security concerns.
  - To empower developers to build securable software without needing years of security experience or translation.

---

## SSEM Attribute 1: Maintainability

- The Critical Question: Can unmaintainable code be secure?
- The Answer: NO. Because there is NO static state of secure.
  - Code that isn't maintainable cannot be changed with confidence.
  - Therefore, it is not securable.
- This is a Software Engineering responsibility, not just an AppSec assurance task.
- Key Pillars of Maintainability:
  - Analyzable: You can understand the code.
  - Modifiable: You can change the code confidently without breaking other things.
  - Testable: The code has discrete, testable units (which also aids threat modeling).
- Guiding Principle:
  
    > Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler
- Relevance to AI: If your generative assistant is producing Maintainable code, it is easier for you to verify its output and understand its limitations.

---

## SSEM Attribute 2: Trustworthiness

While "Trust" is a concept security professionals understand, it can be hard to relate directly to code.
The attributes are embodied in a **logical** fashion, cooperating as a system.

In SSEM, Trustworthiness means:

- There is a clear, understandable architecture.
- Cooperation requires planning.

**The Takeaway:**
If you are not planning (with at least some requirements and architecture), you ***cannot be securable***.

Trustworthiness also requires transparency to enable verification.

---

## SSEM Attribute 3: Reliability

- This is a system-level attribute set that affects all functionality, down to the line level.
- It is built upon the foundation of Maintainability and Trustworthiness.
- **Definition:**
    > “Reliability promotes the ability to keep running predictably under unfavorable circumstances and load.”
- **Important Note:** **Resilience** is a sub-attribute of Reliability. It gets a lot of attention, but it's only one piece of the puzzle. Don't be distracted.

---

## Putting the SSEM into Practice

- **Your Task:** Take this model and internalize it.
  - Understand the terms intimately.
  - Think about how each attribute relates to your security concerns.
  - Build your own confidence by asking, "What can go wrong, and how can this SSEM attribute help prevent it?"
- **Change the Conversation:**
  - Shift from asking, "Did we do a good job?"
  - To asking, "**Does this code meet our goals for this attribute?**"
- Best practices are not enough. We need to prove we are achieving our goals. This is where AppSec provides assurance through testing.

---

## SSEM in the Age of Agentic AI

- These attributes are not just for human-written code; they work exceptionally well for prompt engineering.
- **Observation:** You never get secure code from Generative AI unless you ask for it to be secured in a particular way.
- By using the language of SSEM in your prompts, you can guide AI assistants to generate code that is more inherently Maintainable, Trustworthy, and Reliable.

---

## Conclusion: Building a Securable Future

- **The Securable Principle:** Remember, there is no static state of secure. Our work is never done.
- **The SSEM:** Use this as a shared language to bridge the gap between Software Engineering and Security.
- **The Core Attributes:**
  - **Maintainability:** Can we change it with confidence?
  - **Trustworthiness:** Is it well-planned and transparent?
  - **Reliability:** Does it run predictably under stress?
- **Your Call to Action:**
  - Change the conversation in your teams. Focus on these engineering attributes during design and code review.
  - Apply the SSEM to your interactions with AI, demanding better, more securable code from your assistants.
Code that is not maintainable cannot be changed with confidence
And therefore, is not securable

But is AppSec’s responsibility?
No because AppSec is assurance

Software Engineering are the only ones who can directly influence the tenants of the SSEM
