# Objective Model

## Objective schema

```json
{
  "name": "minimize_error",
  "target_metric": "error_rate",
  "direction": "minimize"
}
```

## Constraint schema

```json
{
  "name": "latency_limit",
  "metric": "latency",
  "operator": "<=",
  "value": 0.8,
  "weight": 1.0
}
```

## Observation schema

```json
{
  "proxy_score": 0.94,
  "goal_score": 0.71,
  "latency": 0.92,
  "safety_score": 0.55
}
```

## Divergence

COBRA can compare:
- desired direction of change
- actual direction of change
- constraint compliance
- proxy versus goal performance

## Persistent mismatch

Repeated mismatch across time should be tracked separately from one-off exceptions.

## Evidence confidence

Risk should be discounted when:
- data quality is low,
- objective is underspecified,
- expected behavior envelope is broad.
