from cobra import CobraMonitor

def aligned_case():
    m = CobraMonitor()
    rows = [
        dict(objective_divergence=0.05,constraint_violation=0.0,proxy_score=0.60,goal_score=0.60,context_gap=0.02),
        dict(objective_divergence=0.04,constraint_violation=0.0,proxy_score=0.65,goal_score=0.66,context_gap=0.02),
        dict(objective_divergence=0.06,constraint_violation=0.0,proxy_score=0.70,goal_score=0.72,context_gap=0.03),
    ]
    out = None
    for r in rows:
        out = m.update(**r)
    return out

def divergent_case():
    m = CobraMonitor()
    rows = [
        dict(objective_divergence=0.20,constraint_violation=0.10,proxy_score=0.60,goal_score=0.60,context_gap=0.10),
        dict(objective_divergence=0.55,constraint_violation=0.30,proxy_score=0.75,goal_score=0.55,context_gap=0.30),
        dict(objective_divergence=0.70,constraint_violation=0.45,proxy_score=0.90,goal_score=0.45,context_gap=0.40),
    ]
    out = None
    for r in rows:
        out = m.update(**r)
    return out

if __name__ == "__main__":
    print("aligned", aligned_case())
    print("divergent", divergent_case())
