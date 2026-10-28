# Month 06 — AI Agents & Tool Calling

**Status:** Not started

## Outcome

Coordinate a bounded workflow with explicit permissions.

## Starting point

Complete month 5: a working RAG application and basic evaluations.

## Weekly sequence

| Week | Work in this order |
|---|---|
| 1 | Build a deterministic invoice workflow first. Define typed tool inputs/outputs and execute a tool call from a model response. |
| 2 | Add a bounded single-agent loop, step limits, timeouts and approval before side effects. Test retries without duplicate sends. |
| 3 | Learn context engineering: what enters each request, token budgets and short/long-term memory. Add explicit memory retention and deletion rules. |
| 4 | Learn Model Context Protocol (MCP) as a tool integration interface. Connect one local read-only tool, keep authorization in the application, and evaluate tool choice and arguments. |

## Ready to move on when

Explain when a workflow is enough, demonstrate one bounded agent, and prevent unapproved or duplicate actions. If this is not yet comfortable, extend this month before continuing.

## Optional / defer

Multi-agent implementations and orchestration frameworks. First record when a single agent fails and whether additional agents would help.

## Topic reference

- Tool schemas, agent loops, state, memory and planning.
- Permissions, human approval and audit trails.
- Retries, idempotency and failure recovery.

## Build

Build an invoice assistant in projects/ai-agent: retrieve unpaid invoices → prepare reminders → request approval → send through a test integration.

## Completion checklist

- [ ] Use sample invoices and a test email destination.
- [ ] Require approval before sending and prevent duplicate actions.
- [ ] Record tool calls and demonstrate a failed-tool recovery.
- [ ] Connect one read-only MCP tool and test permission boundaries.

## Career & income objective

Package a small AI automation service with a defined outcome.

## Portfolio & Staff-level evidence

Document tool permissions, approval boundaries and recovery behavior.

## Review

- Evidence / demo: To add.
- Key decision and trade-off: To add.
- Feedback and next step: To add.

[Dashboard](../README.md) · [Resources](../resources.md)
