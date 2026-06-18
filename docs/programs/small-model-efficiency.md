# Small-Model Efficiency

## Question

Which methods improve capability per parameter, byte, euro, watt, or update
under strict public constraints?

## Focus Areas

- tokenizer-agnostic bits-per-byte scoring
- artifact-size limits
- fixed wall-clock and update budgets
- auxiliary prediction heads
- multilingual tokenizer experiments
- speculative-decoding support experiments
- low-overhead evaluation artifacts

## Public Homes

- Use `limes-parameter-golf` for hard budget and scoring rules.
- Use `limes-nanogpt` for tiny language-model training experiments.
- Use this repository for protocols, gates, and cross-program reports.

## First Experiments

1. Add a baseline result card for a tiny char-level language model.
2. Add an auxiliary-head proposal with locked budget, metric, and ablation.
3. Compare artifact-size, BPB, and update-budget costs against a simple
   baseline before adding any new method.

## Non-Claims

Small-model efficiency work is not a claim that tiny models replace larger
models. It is a way to build experimental taste and contributor discipline.

