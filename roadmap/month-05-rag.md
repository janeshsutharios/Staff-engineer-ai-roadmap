# Month 05 — Retrieval-Augmented Generation

**Status:** Not started

## Outcome

Answer document questions using retrieved evidence.

## Starting point

Complete month 4: model calls, embedding intuition and a small evaluation dataset.

## Weekly sequence

| Week | Work in this order |
|---|---|
| 1 | Learn retrieval-augmented generation (RAG). Split sample text, generate embeddings and compare a query against a tiny collection. |
| 2 | Use PostgreSQL plus a vector-search extension for ingestion and retrieval. Understand exact search before approximate indexes. |
| 3 | Build answers with source references and missing-evidence behavior. Compare keyword, vector and hybrid retrieval; try reranking only if it addresses observed errors. |
| 4 | Add document update/delete handling and access filtering. Score retrieval separately from answer quality on fixed questions; design background ingestion for implementation in month 7. |

## Ready to move on when

Trace an answer to its source, demonstrate missing-evidence handling, and verify deleted or unauthorized content cannot be retrieved. If this is not yet comfortable, extend this month before continuing.

## Optional / defer

Multiple vector databases, advanced index tuning and large-scale ingestion.

## Topic reference

- Embeddings, chunking and vector databases.
- Semantic retrieval, reranking and context construction.
- Source attribution, document access controls and retrieval evaluation.

## Build

Build the Private Document Assistant in projects/rag-assistant using sample PDFs or documentation.

## Completion checklist

- [ ] Ingest documents and retrieve relevant passages.
- [ ] Return source references and abstain when evidence is missing.
- [ ] Evaluate a fixed set of answerable and unanswerable questions.

## Career & income objective

Seek a narrowly scoped document-search or knowledge-assistant pilot.

## Portfolio & Staff-level evidence

Compare retrieval choices using measured results and document access boundaries.

## Review

- Evidence / demo: To add.
- Key decision and trade-off: To add.
- Feedback and next step: To add.

[Dashboard](../README.md) · [Resources](../resources.md)
