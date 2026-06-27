# Limes Research Programs

Limes Research Programs is the public research agenda for Limes Labs.

The purpose of this repository is discipline, not hype. Limes Labs is building
falsifiable experiments, reusable evaluation infrastructure, and public research
protocols before making frontier-capability claims.

## Position

Limes Labs is not claiming to be a frontier lab today. The current objective is
to build the habits and artifacts that make serious research possible:

- preregistered experiments
- clear baselines and controls
- negative-result logs
- benchmark designs that resist easy saturation
- promotion gates before scale-up
- reusable templates for public contributors

Public claims should stay proportional to public evidence. A result can be
interesting before it is decisive; it should be labeled that way.

## Research Agenda

Start with the agenda overview:

- [Public research agenda](docs/research-agenda.md)
- [Long-horizon RL](docs/programs/long-horizon-rl.md)
- [Small-model efficiency](docs/programs/small-model-efficiency.md)
- [Optimizer research](docs/programs/optimizer-research.md)
- [Benchmark design](docs/programs/benchmark-design.md)
- [Agentic LLM challenges](docs/programs/agentic-llm-challenges.md)
- [AutoResearch](docs/programs/autoresearch.md)
- [European applied evals](docs/programs/european-applied-evals.md)

## Public Protocols

These templates are meant to be copied into experiment repos before results are
known:

- [No-cheating protocol template](templates/no-cheating-protocol.md)
- [Promotion-gate template](templates/promotion-gate.md)

## Extraction Map

The public extraction map turns private research themes into sanitized public
work items without publishing private code, raw logs, secrets, or unreviewed
claims:

- [Sanitized private-to-public extraction map](docs/private-extraction-map.md)
- [First public experiments](docs/first-public-experiments.md)

## Related Public Repositories

- [limes-autoresearch](https://github.com/Limes-Labs/limes-autoresearch)
- [limes-dataforge](https://github.com/Limes-Labs/limes-dataforge)
- [limes-kernelforge](https://github.com/Limes-Labs/limes-kernelforge)
- [limes-nanogpt](https://github.com/Limes-Labs/limes-nanogpt)
- [limes-parameter-golf](https://github.com/Limes-Labs/limes-parameter-golf)
- [eurobench](https://github.com/Limes-Labs/eurobench)
- [model-card-template](https://github.com/Limes-Labs/model-card-template)
- [limes-constitution](https://github.com/Limes-Labs/limes-constitution)

## Contributor Rule Of Thumb

A good contribution makes one question easier to test. It does not need to make
the lab sound bigger than it is.

Prefer small, replayable work:

1. State the question.
2. Lock the metric, baselines, budget, and selection rule.
3. Run the smallest meaningful experiment.
4. Publish the artifact and limitations.
5. Promote only if the gate was declared before looking at the result.

## Status

This repository is an initial public scaffold. It is useful when it creates
issues, reports, templates, and experiments that other Limes repositories can
run and review.
