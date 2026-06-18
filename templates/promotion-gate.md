# Promotion-Gate Template

Use this gate before moving an experiment from a cheap setting to a more
expensive setting.

## Candidate

- Experiment:
- Current evidence level:
- Proposed next level:
- Public issue or PR:

## Gate Conditions

| Condition | Required evidence | Pass/Fail | Link |
| --- | --- | --- | --- |
| Protocol was locked before measurement | | | |
| Baselines were fair and documented | | | |
| Primary metric improved in the declared direction | | | |
| Costs were charged to the candidate | | | |
| Instability did not get worse | | | |
| Result survived replay or seed expansion | | | |
| Negative and failed runs are documented | | | |
| Limitations are explicit | | | |

## Decision

Choose one:

- Do not promote.
- Promote to replicated toy experiment.
- Promote to tiny neural experiment.
- Promote to public benchmark experiment.
- Promote to product-candidate evaluation.

## Rationale

Explain why the decision follows from the gate, including what would falsify the
next step.

## Next Protocol Changes

List any changes that must be locked before the next run.

