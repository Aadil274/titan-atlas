from app.engines.titan_engine import (
    run_dynamic_simulation
)

from app.engines.hidden_dependency_engine import (
    find_hidden_dependencies
)


def calculate_systemic_risk(node_name):

    simulation = run_dynamic_simulation(
        node_name
    )

    if not simulation:
        return None

    blast_radius = simulation["simulation"][
        "blast_radius"
    ]

    hidden = find_hidden_dependencies(
        node_name
    )

    dependency_depth = hidden[
        "dependency_depth"
    ]

    hidden_count = len(
        hidden["hidden_dependencies"]
    )

    score = (
        blast_radius * 8
        + dependency_depth * 8
        + hidden_count * 8
    )

    score = min(score, 100)

    if score >= 80:
        level = "CRITICAL"
    elif score >= 60:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "node": node_name,
        "systemic_risk_score": score,
        "risk_level": level,
        "blast_radius": blast_radius,
        "dependency_depth": dependency_depth,
        "hidden_dependencies":
            hidden["hidden_dependencies"]
    }