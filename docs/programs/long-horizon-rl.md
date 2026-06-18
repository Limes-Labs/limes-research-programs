# Long-Horizon RL

## Question

When do critic-based methods such as PPO become more useful than group-relative
methods such as GRPO for long-horizon, multi-turn, tool-using tasks?

## Working Hypotheses

- Group-relative methods can be attractive when memory, implementation, and
  short-horizon comparison costs dominate.
- Long-horizon tasks create variable trace lengths, delayed rewards, tool calls,
  state compaction, and sub-trajectory credit-assignment problems.
- A critic can use more temporal structure from each rollout, but only if value
  training and process supervision remain stable.
- Distillation or policy-improvement methods may complement RL methods; they
  should not be treated as direct replacements without an experiment.

## First Experiments

1. Define a toy variable-length task with delayed reward and distractor states.
2. Compare a group-relative baseline with a critic-based baseline under equal
   rollout budgets.
3. Report token, trajectory, wall-clock, and selection costs.
4. Add a process-supervision ablation only after the base comparison is fixed.

## Non-Claims

- This program does not claim that PPO is always better than GRPO.
- It does not claim frontier agent capability.
- It does not treat tool-use toy tasks as real deployment evidence.

## Promotion Gate

Promote from toy to tiny neural only if the declared primary metric improves
without worse instability, and if the result survives a seed expansion or replay
by a second contributor.

