# No-Cheating Protocol Template

Copy this file into an experiment repo before running the primary measurement.

## Experiment

- Name:
- Owner:
- Date locked:
- Public issue:
- Repository:

## Question

State one falsifiable question.

## Primary Metric

- Metric:
- Direction:
- Unit:
- Why this metric answers the question:

## Baselines

List every baseline before measurement.

| Baseline | Why included | Expected cost |
| --- | --- | --- |
| | | |

## Candidate Method

Describe only the method being tested. Do not include fallback tuning rules that
depend on seeing held-out results.

## Fixed Budget

- Seeds:
- Train-selection split:
- Held-out split:
- Update or sample budget:
- Wall-clock budget:
- Hardware:
- Learning-rate or hyperparameter grid:
- Artifact-size limit, if any:

## Selection Rule

Explain how hyperparameters are selected without using held-out labels,
leaderboard feedback, or private test results.

## Invalid Runs

Declare how to score:

- non-finite losses
- timeouts
- crashes
- missing artifacts
- partial runs

## Required Artifacts

- config file
- command line
- raw result log or ledger path
- summary JSON
- environment notes
- limitations section

## Allowed Follow-Up

Exploratory follow-up is allowed, but it must be logged separately and cannot
replace the primary result.

## Claim Limits

State exactly what wording is allowed if the result is positive, mixed, or
negative.

