# Public Research Agenda

Limes Labs should build public evidence before making large claims. The first
research programs are selected because they can produce useful artifacts with
modest compute: reports, toy experiments, result cards, benchmark tasks, and
experiment ledgers.

## Research Principles

- Claims must be falsifiable.
- Baselines must be named before measurement.
- Hidden selection rules are not acceptable.
- Negative and mixed results remain useful.
- Scale-up requires a promotion gate.
- Public artifacts should help someone else reproduce or criticize the work.
- Large-model adaptation is downstream of evaluation, safety, and experiment
  infrastructure.

## Program Map

| Program | Near-term artifact | Primary public repo |
| --- | --- | --- |
| Long-horizon RL | PPO vs GRPO vs distillation report and toy tasks | This repo, then `limes-nanogpt` and `limes-autoresearch` |
| Small-model efficiency | BPB, artifact-size, and update-budget experiments | `limes-parameter-golf`, `limes-nanogpt` |
| Optimizer research | Preregistered optimizer probes and negative-result summaries | `limes-nanogpt`, `limes-parameter-golf` |
| Benchmark design | Harder European task schemas and result cards | `eurobench` |
| AutoResearch | Specs, ledgers, replayable experiment loops, report generation | `limes-autoresearch` |
| European applied evals | Public-administration, law-adjacent, multilingual, and tool-use evals | `eurobench` |

## Evidence Ladder

Use this ladder to label results:

| Level | Meaning | Allowed public wording |
| --- | --- | --- |
| Idea | A plausible direction with no result yet | "Research question" |
| Toy signal | Works on a declared toy setup | "Toy evidence" |
| Replicated toy signal | Survives replay or seed expansion | "Replicated toy evidence" |
| Tiny neural signal | Survives a small neural experiment with fixed budgets | "Tiny-model evidence" |
| External benchmark signal | Improves a public benchmark or held-out task under a declared protocol | "Benchmark evidence" |
| Product candidate | Improves a user-facing workflow with safety and reliability checks | "Candidate capability" |

Do not skip labels. Do not call toy evidence a model breakthrough.

## First 90 Days

1. Publish the protocols and issue templates in this repository.
2. Open first experiment issues for each program.
3. Run at least one tiny, replayable experiment through AutoResearch.
4. Publish at least one EuroBench result card with limitations.
5. Add at least one optimizer or auxiliary-head task to nanoGPT.
6. Add an efficiency-track task to Parameter Golf.

