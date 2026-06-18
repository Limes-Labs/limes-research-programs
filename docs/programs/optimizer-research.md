# Optimizer Research

## Question

Which optimizer ideas survive fair comparison against strong cheap baselines
under fixed budget, declared learning-rate grids, and replayable summaries?

## Required Controls

- same objective list
- same seeds
- same learning-rate grid, unless a different grid is justified before results
- same update budget
- same train-selection and held-out scoring split
- divergence and non-finite accounting
- cost accounting for extra state, probes, selectors, teachers, or critics

## First Experiments

1. Publish a tiny optimizer-probe issue with fixed objectives and baselines.
2. Require a no-cheating protocol before any result summary.
3. Promote only if the candidate beats AdamW-like and cheap sign/momentum
   baselines on the declared statistic without worse divergence.

## Negative Results

A failed optimizer is still useful if it narrows the search space, improves the
protocol, or identifies a mechanism that does not transfer.

## Public Homes

- `limes-nanogpt` for tiny neural transfer.
- `limes-parameter-golf` for update-budget and artifact-cost accounting.
- `limes-autoresearch` for ledgers and replay.

