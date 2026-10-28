# Staff Engineer + AI Roadmap

A 12-month, project-led development plan for an experienced iOS engineer starting with **no backend or AI engineering knowledge**. Existing programming and iOS skills are the foundation; AI concepts are introduced from first principles.

**Direction:** iOS Engineer → Mobile + Backend Engineer → AI Systems Engineer → Staff-level technical ownership.

## Start here

Begin with [Month 01 — Python](roadmap/month-01-python.md) and follow each monthly **weekly sequence**. The topic reference lists what to revisit; optional sections are not required to advance.

**Prerequisite chain:** Python and HTTP → SQL and APIs → secure, tested backend → AI foundations and model APIs → retrieval → tools and agents → background workflows → cloud operations → system design → advanced AI reliability → on-device AI → validated portfolio.

Plan around **8–10 focused hours per week** as a starting assumption: roughly 3 hours learning, 5 building/testing and 1–2 reviewing. This is a planning budget, not a completion estimate. Extend a month until its readiness check passes; the sequence matters more than finishing in exactly one year.

## Goals

- Develop the ability to design, build, deploy and evaluate complete AI-powered products.
- Explore side income through existing iOS expertise first, then backend and AI integration services.
- Build evidence of architecture, reliability, collaboration and measurable impact alongside technical learning.

The months are a suggested sequence, not fixed calendar deadlines. Income objectives are aspirations; Staff-level progression depends on demonstrated scope and impact.

## Progress dashboard

**Current status:** Plan created; learning and project completion have not yet been recorded.

| Done | Month | Focus | Deliverable |
|---|---|---|---|
| ☐ | [01](roadmap/month-01-python.md) | Python, Git & APIs | Small REST API |
| ☐ | [02](roadmap/month-02-backend.md) | FastAPI & PostgreSQL | Expense Tracker backend |
| ☐ | [03](roadmap/month-03-production-backend.md) | Production Backend | Authenticated, containerized backend |
| ☐ | [04](roadmap/month-04-llm.md) | AI Foundations & LLM APIs | Evaluated AI Notes integration |
| ☐ | [05](roadmap/month-05-rag.md) | Retrieval-Augmented Generation | Private Document Assistant |
| ☐ | [06](roadmap/month-06-agents.md) | AI Agents & Tool Calling | Invoice reminder agent |
| ☐ | [07](roadmap/month-07-ai-automation.md) | Background Jobs & Business Automation | Reliable ingestion and business workflow |
| ☐ | [08](roadmap/month-08-aws.md) | AWS, Deployment & CI/CD | Deployed system and CI/CD |
| ☐ | [09](roadmap/month-09-system-design.md) | System Design & Distributed Systems | Measured scaling case study |
| ☐ | [10](roadmap/month-10-production-ai.md) | Production AI Engineering | Evaluated, observable AI system |
| ☐ | [11](roadmap/month-11-on-device-ai.md) | On-device AI & iOS | Local/cloud iOS AI prototype |
| ☐ | [12](roadmap/month-12-final-project.md) | Flagship Product & Portfolio | AI Business Assistant and portfolio |

## Learning journal

Start with [Day 1 — Python basics](ai-learning/month-01-python/day-01.md). Keep dated notes, practice code and completion evidence in [ai-learning/](ai-learning/README.md), and track actual progress in the [learning log](ai-learning/progress.md).

## Working rhythm

1. Open the current month and choose a small weekly deliverable.
2. Learn what is needed, build it, and record decisions in the relevant notes file.
3. Commit progress with evidence: a demo, measurement, test result or design review.
4. Complete the monthly checklist, link the evidence, and update the dashboard to ☑.

Throughout the year, practice writing design proposals, reviewing trade-offs, seeking peer feedback and mentoring. Record actual outcomes rather than claiming experience from coursework alone.

## Repository guide

| Location | Purpose |
|---|---|
| [roadmap/](roadmap/) | Monthly outcomes, learning topics and completion criteria |
| [notes/python.md](notes/python.md) | Python concepts and Swift comparisons |
| [notes/backend.md](notes/backend.md) | APIs, databases, authentication and operations |
| [notes/ai-engineering.md](notes/ai-engineering.md) | LLMs, retrieval, agents and evaluations |
| [notes/system-design.md](notes/system-design.md) | Requirements, RFCs and architectural trade-offs |
| [notes/aws.md](notes/aws.md) | Deployment, access control, cost and recovery |
| [projects/expense-tracker/](projects/expense-tracker/) | Months 1–3: mobile and backend foundation |
| [projects/rag-assistant/](projects/rag-assistant/) | Month 5 onward: document retrieval and grounded answers |
| [projects/ai-agent/](projects/ai-agent/) | Month 6 onward: approved workflows and flagship integration |
| [resources.md](resources.md) | Focused learning references and resource log |

## What this prepares you for

The initial target is **AI application engineering**: building software around models, retrieval and tools, then evaluating and operating it. Model research, large-model training and advanced GPU infrastructure are separate specializations.

Staff-level progression also requires demonstrated technical direction, collaboration and organizational impact. Record design reviews and feedback throughout the year; a completed curriculum does not guarantee a title or job.

## Keep the scope manageable

- Use one backend stack, one model provider and one cloud provider initially.
- Start evaluations in month 4 and improve them continuously; month 10 deepens an existing practice.
- Start with deterministic workflows and one agent. Multi-agent frameworks, fine-tuning, Kubernetes and GPU hosting are optional extensions.
- Paid courses are optional. See [resources](resources.md) for when the two reviewed curricula fit.

## Portfolio standard

Each project starts as a planning placeholder. As it is implemented, add setup instructions, architecture, a demo, tests or evaluations, measured results and limitations. Use sample or permission-cleared data and keep credentials out of version control.

Prefer improving these projects and integrating them into one flagship product over accumulating unrelated tutorials.
