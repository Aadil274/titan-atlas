from app.engines.atlas_engine import (
    analyze_impact
)


def calculate_resilience_score(node_name):

    impact = analyze_impact(node_name)

    if not impact:
        return None

    blast_radius = impact["blast_radius"]

    score = max(
        0,
        100 - (blast_radius * 10)
    )

    risk = "LOW"

    if score < 50:
        risk = "HIGH"
    elif score < 70:
        risk = "MEDIUM"

    return {
        "node": node_name,
        "resilience_score": score,
        "risk_level": risk,
        "blast_radius": blast_radius
    }