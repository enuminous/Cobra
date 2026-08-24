# COBRA Theory

## 1. Problem

A system can satisfy a narrow metric while violating the broader objective that metric was intended to represent.

Examples include:
- optimizing a proxy instead of the intended goal,
- gaming an evaluation metric,
- exploiting underspecified constraints,
- producing superficially compliant but harmful outcomes,
- behaving differently under evaluation versus deployment.

COBRA evaluates these divergences behaviorally.

## 2. Declared objective

Let the declared objective be:

`J_declared(x,a)`

Let explicit constraints be:

`C_k(x,a) <= 0`

Observed action is:

`a_t`

## 3. Expected behavior envelope

Define the set of acceptable actions:

`A_expected(x_t)`

based on the declared objective and constraints.

## 4. Objective-behavior divergence

For observed action `a_t`:

`D_t = distance(a_t, A_expected(x_t))`

or task-specific loss relative to an expected policy.

Higher `D_t` means greater mismatch.

## 5. Constraint violation

Let:

`V_t = weighted_fraction_of_violated_constraints`

## 6. Proxy optimization

Suppose a measurable proxy is `P` and intended outcome is `G`.

If:

`P_t increases`

while:

`G_t stagnates or declines`

then a proxy-divergence signal can be:

`Q_t = positive_delta(P_t) * positive_delta(-G_t)`

## 7. Persistence

One anomalous action may be noise.

Recursive divergence state:

`R_t = lambda*R_{t-1} + (1-lambda)*D_t`

Persistent divergence is more concerning than an isolated mismatch.

## 8. Context dependence

COBRA should compare divergence across contexts:

`D(c_1), D(c_2), ...`

Large evaluation/deployment gaps may indicate poor objective generalization.

This still does not establish strategic deception.

## 9. Composite risk

Candidate score:

`Risk_t = w1*R_t + w2*V_t + w3*Q_t + w4*ContextGap_t`

after normalization.

## 10. EFMW interpretation

The EFMW-inspired element is recursive comparison among:
- stated objective,
- explicit constraints,
- observed behavior,
- downstream outcomes,
- context.

## 11. Falsifiable prediction

COBRA should add value when:
- proxies are imperfect,
- constraints are incomplete,
- behavior drifts over time,
- contexts differ.

If standard specification testing and reward-hacking benchmarks capture the same issues, COBRA adds no justified complexity.
