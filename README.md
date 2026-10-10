# COBRA — EFMW Zoo #40

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Cobra) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Covert Objective and Behavioral Risk Assessment**

COBRA is an experimental EFMW-inspired framework for measuring divergence between declared objectives, explicit constraints, and observed behavior.

## Core question

> Is the system behaving in ways that systematically depart from what its stated objective and rules would predict?

COBRA is deliberately evidence-focused. It measures objective-behavior divergence and risk signals; it does **not** infer hidden intent, deception, sentience, or motive from behavior alone.

## Primary outputs

- objective-behavior divergence
- constraint violation rate
- proxy-optimization score
- reward-hacking indicator
- context-specific divergence
- persistence of divergence
- behavioral risk score
- evidence confidence

## Repository contents

- `theory.md`
- `architecture.md`
- `objective_model.md`
- `limitations.md`
- `cobra.py`
- `benchmark.py`
- `ablations.py`
- `test_cobra.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_cobra.py
```

## Zoo position

PHOENIX #39 evaluates recovery after failure.

**COBRA #40 asks whether a system that appears operational is optimizing in ways that diverge from its declared objective or constraints.**
