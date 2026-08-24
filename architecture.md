# COBRA Architecture

## Pipeline

1. Objective/Constraint Loader
2. Behavioral Observation Ingestor
3. Expected-Behavior Model
4. Divergence Engine
5. Constraint Violation Analyzer
6. Proxy/Goal Comparator
7. Persistence Tracker
8. Context Comparison Layer
9. Evidence Confidence Layer
10. Risk Reporter

## Inputs

- declared objectives
- hard/soft constraints
- observed actions/outcomes
- proxy metrics
- goal metrics
- context labels
- evidence confidence

## Outputs

```json
{
  "objective_divergence": 0.42,
  "constraint_violation": 0.25,
  "proxy_divergence": 0.31,
  "persistent_divergence": 0.28,
  "context_gap": 0.18,
  "risk_score": 0.33,
  "evidence_confidence": 0.90
}
```

## Design principle

COBRA reports behavioral inconsistency.

It should never convert:

"behavior diverges from objective"

into:

"the system secretly intends something else."

That inference is not justified by the observable data alone.

## Integration

CHAMELEON can identify context-specific divergence.

ELEPHANT can preserve objective and policy history.

SALMON can trace a divergent behavior to its historical source.

MAGPIE can audit the evidence supporting the risk claim.
