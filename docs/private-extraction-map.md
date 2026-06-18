# Sanitized Private-To-Public Extraction Map

This map converts private research themes into public tasks. It does not publish
private source code, raw logs, secrets, cloud scripts, detailed internal notes,
or unreviewed claims.

## Publicization Rule

Before any private material becomes public, it needs:

- a cleaned README
- license and attribution review
- secret and token scan
- claim downgrading to the public evidence level
- passing tests or an explicit "not runnable yet" status
- one public issue describing the next falsifiable experiment

## Theme Routing

| Sanitized private theme | Public destination | Public artifact |
| --- | --- | --- |
| Sparse memory, route-index, compressed-attention, and cache-cost probes | `limes-nanogpt`, `limes-parameter-golf` | Issue: cost-accounted attention or memory probe |
| Optimizer switching, curvature diagnostics, and stability tests | `limes-nanogpt`, `limes-parameter-golf` | Issue: preregistered optimizer comparison |
| Multi-state, future-token, and auxiliary-process supervision | `limes-nanogpt`, long-horizon RL program | Issue: auxiliary-head ablation with fixed budget |
| No-cheating protocols, result ledgers, and promotion gates | `limes-autoresearch`, this repo | Template and adapter tasks |
| Heavy-tail, noisy-gradient, and outlier robustness probes | `limes-parameter-golf`, `limes-nanogpt` | Issue: robust optimizer smoke test |
| Routing-budget and proxy-oracle-gap methodology | `eurobench`, `limes-autoresearch` | Issue: benchmark selection-bias audit |
| Architecture-search negative results | this repo, `limes-nanogpt` | Report: negative-result summary and next falsifier |
| Paper-style optimizer material | this repo first, then a dedicated public repo if warranted | Report: cleaned related-work and evidence statement |

## What Not To Extract Yet

- raw private experiment logs
- vendor-specific cloud scripts
- unpublished paper drafts with unresolved attribution
- private repo history
- names, tokens, or infrastructure details from private environments
- claims that rely on private-only evidence

## First Extraction Tasks

1. Open one public issue per theme using the experiment template.
2. Attach a no-cheating protocol before measurement.
3. Reimplement minimal experiments in public repos when needed; do not copy
   private source wholesale.
4. Publish negative results and failed transfers as first-class outputs.

