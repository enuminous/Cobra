from benchmark import aligned_case, divergent_case

if __name__ == "__main__":
    good = aligned_case()
    bad = divergent_case()
    print("full aligned risk:", good["risk_score"])
    print("full divergent risk:", bad["risk_score"])
    print("instant-only divergent:", bad["objective_divergence"])
