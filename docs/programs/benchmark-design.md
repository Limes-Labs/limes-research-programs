# Benchmark Design

## Question

How can Limes Labs build European benchmarks that remain useful as models
improve?

## Design Targets

- multilingual reasoning across EU languages
- law-adjacent and public-administration tasks with careful limitations
- citation-grounded answers with distractors
- long-context retrieval and contradiction handling
- regional and low-resource language coverage
- safe cyber and software-engineering tasks
- agentic workflows with tools, files, and state
- contamination checks and versioned public/private splits

## Benchmark Discipline

- Separate public exemplars from any held-out evaluation.
- Publish schemas, rubrics, and result-card formats.
- Report failures and limitations.
- Avoid fake precision from automatic scoring.
- Prefer task review and source-rights documentation over large unverified task
  dumps.

## Public Home

Benchmark implementation should live in `eurobench`. This repository owns the
cross-program design rules and promotion gates.

