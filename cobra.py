from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class CobraConfig:
    persistence: float = 0.8
    w_divergence: float = 0.4
    w_violation: float = 0.3
    w_proxy: float = 0.2
    w_context: float = 0.1

class CobraMonitor:
    def __init__(self, config: Optional[CobraConfig] = None):
        self.config = config or CobraConfig()
        self.persistent_divergence = 0.0
        self.prev_proxy = None
        self.prev_goal = None

    @staticmethod
    def clip01(x):
        return max(0.0, min(1.0, float(x)))

    def update(
        self,
        objective_divergence: float,
        constraint_violation: float,
        proxy_score: Optional[float] = None,
        goal_score: Optional[float] = None,
        context_gap: float = 0.0,
        evidence_confidence: float = 1.0
    ):
        d = self.clip01(objective_divergence)
        v = self.clip01(constraint_violation)
        cgap = self.clip01(context_gap)
        conf = self.clip01(evidence_confidence)

        self.persistent_divergence = (
            self.config.persistence * self.persistent_divergence
            + (1-self.config.persistence) * d
        )

        proxy_div = 0.0
        if proxy_score is not None and goal_score is not None:
            p = float(proxy_score)
            g = float(goal_score)
            if self.prev_proxy is not None and self.prev_goal is not None:
                dp = p - self.prev_proxy
                dg = g - self.prev_goal
                proxy_div = max(0.0, dp) * max(0.0, -dg)
            self.prev_proxy = p
            self.prev_goal = g

        raw_risk = (
            self.config.w_divergence * self.persistent_divergence +
            self.config.w_violation * v +
            self.config.w_proxy * self.clip01(proxy_div) +
            self.config.w_context * cgap
        )

        risk = self.clip01(raw_risk * conf)

        return {
            "objective_divergence": d,
            "constraint_violation": v,
            "proxy_divergence": proxy_div,
            "persistent_divergence": self.persistent_divergence,
            "context_gap": cgap,
            "risk_score": risk,
            "evidence_confidence": conf
        }
