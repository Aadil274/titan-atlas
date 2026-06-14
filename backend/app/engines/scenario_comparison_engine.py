from app.engines.titan_engine import (
    run_dynamic_simulation
)


def compare_scenarios(nodes):

    comparisons = []

    highest_risk = None
    highest_radius = -1

    for node in nodes:

        result = run_dynamic_simulation(node)

        if not result:
            continue

        blast_radius = result["simulation"][
            "blast_radius"
        ]

        severity = result["simulation"][
            "severity"
        ]

        comparisons.append({
            "node": node,
            "blast_radius": blast_radius,
            "severity": severity
        })

        if blast_radius > highest_radius:

            highest_radius = blast_radius

            highest_risk = node

    return {
        "highest_risk_scenario":
            highest_risk,

        "comparison":
            comparisons
    }