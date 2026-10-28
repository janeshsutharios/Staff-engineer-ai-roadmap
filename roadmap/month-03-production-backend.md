# Month 03 — Production Backend

**Status:** Not started

## Outcome

Make the Expense Tracker reproducible and operationally understandable.

## Starting point

Complete month 2: a working PostgreSQL-backed expense workflow.

## Weekly sequence

| Week | Work in this order |
|---|---|
| 1 | Distinguish authentication from authorization. Implement login using established libraries and test user-level access. |
| 2 | Learn processes, ports, environment variables and container images; package the API and database with Docker. |
| 3 | Add structured logs, consistent errors, integration tests and basic continuous integration (CI) to run tests on changes. |
| 4 | Test failures and document setup. Learn cache and rate-limit concepts; try Redis only after the core service works. |

## Ready to move on when

Run from a clean checkout, demonstrate isolated user data, and explain how to diagnose a failed request. If this is not yet comfortable, extend this month before continuing.

## Optional / defer

Redis implementation and advanced OAuth flows; do not design cryptography or token formats yourself.

## Topic reference

- JWT/OAuth concepts and authorization.
- Docker, Redis caching and rate limiting.
- Logging, error handling and unit/integration tests.

## Build

Extend the Expense Tracker with authentication, Docker, automated checks and a documented local setup. Redis is an optional extension.

## Completion checklist

- [ ] Verify users cannot access each other’s expenses.
- [ ] Test failure paths; if caching is added, document and test invalidation.
- [ ] Run the backend from a clean checkout and capture test results.

## Career & income objective

Offer combined iOS bug fixing and backend work with clear scope and acceptance criteria.

## Portfolio & Staff-level evidence

Write an architecture decision and a short failure-recovery runbook.

## Review

- Evidence / demo: To add.
- Key decision and trade-off: To add.
- Feedback and next step: To add.

[Dashboard](../README.md) · [Resources](../resources.md)
