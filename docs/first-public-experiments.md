# First Public Experiments

These are starter tasks for public issues. Each one should use the
[no-cheating protocol template](../templates/no-cheating-protocol.md) and, when
moving to a larger setting, the [promotion-gate template](../templates/promotion-gate.md).

## EXP-001: Long-Horizon RL Toy Credit Assignment

- Program: long-horizon RL
- Public home: this repo, then `limes-autoresearch`
- Question: does a critic-based baseline use delayed-reward information more
  effectively than a group-relative baseline on a variable-length toy task?
- Primary metric: held-out task reward under equal rollout budget
- Required baselines: random policy, group-relative baseline, critic baseline
- First artifact: report plus summary JSON

## EXP-002: Auxiliary-Head Tiny LM Ablation

- Program: small-model efficiency
- Public home: `limes-nanogpt`
- Question: does an auxiliary future-token or multi-state head improve validation
  loss or BPB under the same update budget?
- Primary metric: validation BPB or loss under fixed updates
- Required baselines: existing tiny char baseline and candidate with charged
  extra parameters
- First artifact: eval JSON and limitations note

## EXP-003: Optimizer Fairness Smoke

- Program: optimizer research
- Public home: `limes-parameter-golf` or `limes-nanogpt`
- Question: does a candidate optimizer beat AdamW-like and cheap sign/momentum
  baselines under the declared grid and seed set?
- Primary metric: declared median rank or validation loss
- Required baselines: AdamW-like, sign/momentum, simple gradient method
- First artifact: raw ledger, summary JSON, no-cheating protocol

## EXP-004: EuroBench Hard Result Card

- Program: benchmark design and European applied evals
- Public home: `eurobench`
- Question: can one open-weight model run through the hard public tasks with a
  result card that reports limitations honestly?
- Primary metric: rubric label counts and qualitative failures
- Required baselines: dummy backend or prior example output, if applicable
- First artifact: result card and reproducibility command

## EXP-005: AutoResearch Ledger Round Trip

- Program: AutoResearch
- Public home: `limes-autoresearch`
- Question: can a research-question spec create a run, parse declared metrics,
  append a ledger entry, and generate a report without manual editing?
- Primary metric: successful replay and schema validation
- Required baselines: mock experiment and one real adapter target
- First artifact: ledger JSONL and generated report

