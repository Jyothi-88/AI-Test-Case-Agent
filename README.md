# AI Test Case Agent

An AI-powered Quality Engineering framework that uses Generative AI to analyze software requirements, generate test cases, evaluate their quality, and progressively evolve toward an agentic testing workflow.

## Project Overview

The **AI Test Case Agent** is a practical Quality Engineering project focused on applying Generative AI and LLM evaluation techniques to software testing.

The framework accepts software requirements, user stories, or acceptance criteria and uses an AI-powered workflow to:

* Analyze requirements
* Generate software test cases
* Review generated test cases
* Evaluate AI output quality
* Identify missing scenarios and potential hallucinations
* Measure test coverage and output consistency
* Apply quality gates
* Support improvement and regeneration

The project will progressively evolve from an AI-powered test case generator into an **agentic Quality Engineering workflow**.

## High-Level Workflow

```text
Requirement / User Story
          ↓
Requirement Analysis
          ↓
AI Test Case Generator
          ↓
Generated Test Cases
          ↓
AI Test Case Reviewer
          ↓
AI Evaluation
          ↓
Quality Metrics
          ↓
Quality Gate
          ↓
Report / Feedback
          ↓
   Improvement / Regeneration
```

## Technology Stack

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | Core development language    |
| Pytest            | Automated testing            |
| Google Gemini API | Generative AI / LLM          |
| DeepEval          | LLM and AI output evaluation |
| Git               | Version control              |
| GitHub            | Source code and portfolio    |
| VS Code           | Development environment      |

## AI Testing Focus

The project will evaluate AI-generated test cases across multiple quality dimensions.

### Test Case Quality

* Correctness
* Relevance
* Completeness
* Clarity
* Consistency
* Duplicate detection

### Test Coverage

* Positive scenarios
* Negative scenarios
* Boundary conditions
* Edge cases
* Error handling
* Functional scenarios

### AI-Specific Quality

* Hallucination detection
* Requirement adherence
* Factual consistency
* Prompt sensitivity
* Output consistency
* Regression behavior

### Agentic Testing

As the project evolves, the framework will also cover:

* Agent decision making
* Workflow execution
* State management
* Tool interactions
* Error recovery
* Guardrails
* Unexpected input handling
* Agent output quality

## Project Architecture

The planned framework will contain modular components such as:

```text
Requirement Input
       ↓
Requirement Analyzer
       ↓
Test Case Generator
       ↓
Test Case Reviewer
       ↓
Evaluation Engine
       ↓
Quality Gate
       ↓
Reporting
```

Additional capabilities such as prompt management, test data management, CI/CD integration, and agent orchestration will be introduced incrementally.

## Testing Strategy

The project combines multiple testing and evaluation layers.

### Functional Validation

Validate that the framework correctly processes requirements and generates expected outputs.

### Automated Testing

Use Pytest for deterministic application and framework behavior.

### LLM Evaluation

Use DeepEval and suitable evaluation metrics to assess AI-generated outputs.

### Regression Evaluation

Run repeatable evaluation scenarios when prompts, models, agents, or application logic change.

### Quality Gates

Define measurable thresholds to determine whether generated test cases meet the required quality level.

## Project Development Approach

The project follows an incremental Quality Engineering approach:

```text
Learn
  ↓
Design
  ↓
Build
  ↓
Test
  ↓
Evaluate
  ↓
Document
  ↓
Commit
  ↓
Push
```

Each module will be developed, tested, reviewed, documented, and committed to GitHub.

## Repository Structure

```text
AI-Test-Case-Agent/
│
├── 01_Framework/
│   └── Core framework implementation
│
├── 02_Documentation/
│   └── Project documentation
│
├── 03_Test_Data/
│   └── Requirements and test data
│
├── 04_Screenshots/
│   └── Local development evidence
│
├── 05_Test_Reports/
│   └── Local test and evaluation reports
│
├── 06_GitHub/
│   └── GitHub-related project artifacts
│
└── README.md
```

Some folders are intentionally excluded from the public repository because they contain local development, tracking, or generated artifacts.

## Current Status

### Module 1 — Project Foundation

* Python environment setup
* Virtual environment
* VS Code configuration
* Project structure
* Git initialization
* `.gitignore`
* Project documentation
* GitHub repository setup
* Initial project push

### Next

**AI Test Case Agent framework implementation**

## Detailed Documentation

For the detailed technical project overview, see:

`02_Documentation/Project_Overview.md`

## Future Enhancements

The framework is planned to evolve with:

* Requirement analysis agents
* AI-powered test case generation
* AI test case review
* DeepEval-based evaluation
* Automated quality scoring
* Quality gates
* Regression evaluation
* Agent orchestration
* CI/CD integration
* Test execution integration
* Reporting and dashboards

## Portfolio Objective

This project demonstrates practical application of:

* Quality Engineering
* Software Testing
* Test Automation
* Generative AI
* LLM Evaluation
* AI Testing
* Agentic AI
* Python
* Pytest
* DeepEval

The goal is to demonstrate how AI can be incorporated into a structured Quality Engineering workflow rather than using AI only for test case generation.

---

## Author

**Jyothi Aradhya**

QA Lead | Quality Engineering | AI in QA | Test Automation | LLM Evaluation

This project is a personal portfolio project developed and maintained by Jyothi Aradhya.
