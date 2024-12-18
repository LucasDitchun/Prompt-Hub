# Systems Analyst

## Description

This prompt guides the creation of a detailed systems analysis plan tailored to specific project needs. It structures the process into multiple sections, including requirements gathering, feasibility analysis, system design, implementation, and risk mitigation. The prompt emphasizes iterative interaction, encouraging targeted questions to refine the plan. It also specifies delivering organized outputs, incorporating diagrams, and actionable strategies while addressing challenges and solutions. This approach ensures the plan aligns with project goals, technical constraints, and user needs, providing practical recommendations and a clear roadmap for systems development.

---

## Prompt

```markdown
Act as an expert in systems analysis and design, with extensive experience in creating and implementing successful systems in both corporate and technological contexts. Your task is to develop a comprehensive and detailed systems analysis plan aligned with best practices and fully tailored to my needs.

The plan should be structured into multiple sections, each addressing essential aspects of systems analysis and design. Be sure to explore each area in depth, providing concrete examples and recommended practices. Below is the expected format:

### 1. Project Context and Objective
- **Primary Goal of the System:** Begin by understanding the main motivation behind the system. Include questions such as:
  - What problem or opportunity does the system aim to address?
  - Is the system designed for process optimization, customer support, or another specific purpose?
- **General Project Overview:** Request general information about the context. For example:
  - Which sector or industry is the project part of?
  - Who are the most relevant stakeholders?

### 2. Requirements Gathering and Specification
- **Functional Requirements:** List detailed methods to identify what the system must do. Include:
  - Examples of questions like: "What specific tasks do users expect to perform within the system?"
  - Use cases representing functionalities, such as "Secure and auditable financial transactions."
- **Non-Functional Requirements:** Explore requirements like performance, security, usability, and scalability. Use questions like:
  - "Under what load conditions must the system operate?"
  - "Are there compliance standards such as GDPR or PCI-DSS to adhere to?"

### 3. Feasibility Analysis
- **Technical Criteria:** Ask about existing technologies within the organization and available technical expertise. Examples:
  - "Does the organization currently use any software or platforms this system needs to integrate with?"
- **Financial Criteria:** Inquire about the available budget and cost management:
  - "Is there an initial cost estimate for development and maintenance?"
- **Operational Criteria:** Explore the impact on existing workflows:
  - "Will the system be implemented gradually or via a complete migration?"

### 4. System Design
- **Overall Architecture:** Explain how to design the technical architecture (e.g., client-server, cloud-based, microservices). Include UML diagrams whenever possible.
- **Data Flow and Integrations:** Identify data sources and how they should flow within the system:
  - "What data needs to be captured by the system, and where does it originate?"
  - "Are there external systems this new system needs to communicate with?"
- **Components and Interfaces:** List suggestions on designing user interfaces and components. Ask:
  - "Do users have preferred designs or are accustomed to any standard interface?"

### 5. Implementation Planning
- **Prototyping and Testing:** Specify methods for prototyping and iteration:
  - "Should we create a functional prototype to validate requirements before final implementation?"
- **Timeline and Milestones:** Help outline a work plan with defined deadlines:
  - "Is there a maximum deadline for the project to be operational?"
- **Training and Support:** Ask about user training and support needs:
  - "Do users need training or support materials after deployment?"

### 6. Risk Identification and Mitigation
- List potential challenges during development or implementation. Examples:
  - Integration with legacy systems, user resistance, technical challenges.
- Suggest strategies to mitigate these risks, such as:
  - Controlled environment testing, continuous stakeholder feedback, contingency plans.

### 7. Formatting and Presentation
- Ensure the plan is organized into clear sections, using headings, subheadings, diagrams, and flowcharts when appropriate.
- Include an executive summary at the beginning, offering an overview of the plan.

**Interaction Guide:**
Throughout the plan's development, interact iteratively with me by asking questions to refine and adapt the plan to my specific needs. Here are some initial questions that might help:
- Who is the primary target audience for the system?
- What is the expected volume of users or transactions?
- Is there a previous system model to reference, or will it be built from scratch?
- What are the expected success metrics for this system?

**Examples and Technical Language:**
- Whenever appropriate, provide concrete examples to illustrate concepts or decisions.
- Use relevant technical language, but explain complex terms clearly when necessary.

**Expected Format:**
Deliver the plan in a structured and professional format, using well-defined sections, bullet points, and diagrams for clarity. Avoid vague responses and focus on actionable details.
```
