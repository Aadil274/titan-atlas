from app.engines.risk_ranking_engine import (
    generate_network_ranking
)

from app.engines.critical_node_engine import (
    get_critical_nodes
)

def generate_network_summary():

    rankings_data = generate_network_ranking()
    
    critical_nodes = get_critical_nodes()
    
    rankings = rankings_data["rankings"]

    if not rankings:
        return None
    
    highest_risk = rankings[0]["node"]

    highest_score = rankings[0][
        "resilience_score"
    ]

    total_score = sum(
        item["resilience_score"]
        for item in rankings
    )

    average_resilience = round(
        total_score / len(rankings),
        2
    )

    critical_names = []

    for node in critical_nodes:

        if node["criticality"] == "HIGH":

            critical_names.append(
                node["node"]
            )
    
    if average_resilience >= 80:
        network_health = "HEALTHY"

    elif average_resilience >= 60:
        network_health = "MODERATE"

    else:
        network_health = "FRAGILE"

    summary = (
        f"The ecosystem contains "
        f"{len(rankings)} entities. "
        f"The highest risk node is "
        f"{highest_risk}. "
        f"There are "
        f"{len(critical_names)} critical "
        f"concentration points in the network."
    )

    return {

        "network_health":
            network_health,

        "highest_risk_node":
            highest_risk,

        "highest_risk_score":
            highest_score,

        "average_resilience":
            average_resilience,

        "critical_nodes":
            critical_names,

        "total_nodes":
            len(rankings),

        "executive_summary":
            summary
    }