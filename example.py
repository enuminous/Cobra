from cobra import CobraMonitor

monitor = CobraMonitor()

observations = [
    {
        "objective_divergence":0.10,
        "constraint_violation":0.0,
        "proxy_score":0.50,
        "goal_score":0.50,
        "context_gap":0.05
    },
    {
        "objective_divergence":0.35,
        "constraint_violation":0.15,
        "proxy_score":0.70,
        "goal_score":0.48,
        "context_gap":0.20
    },
    {
        "objective_divergence":0.55,
        "constraint_violation":0.25,
        "proxy_score":0.85,
        "goal_score":0.40,
        "context_gap":0.25
    }
]

for obs in observations:
    print(monitor.update(**obs))
