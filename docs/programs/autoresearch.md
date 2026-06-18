# AutoResearch

## Question

How can automated research loops produce real signal instead of polished noise?

## Scope

AutoResearch should coordinate experiments; it should not be used to inflate
claims. A useful loop proposes one change, runs a bounded experiment, parses
declared metrics, writes to an immutable ledger, and generates a reviewable
report.

## Near-Term Features

- research-question specs
- experiment ledgers
- backend detection and CPU/GPU fallbacks
- adapters for EuroBench, Parameter Golf, and nanoGPT
- report generation
- issue templates for experiment proposals
- safety boundaries for automated agents

## First Experiments

1. Define a research-question spec for one small-model efficiency task.
2. Run a smoke experiment with a declared metric and ledger output.
3. Generate a report that includes limitations and failed attempts.

## Promotion Gate

An AutoResearch loop should be promoted only if humans can replay the result,
inspect the metric parser, and identify which choices were made before and after
measurement.

