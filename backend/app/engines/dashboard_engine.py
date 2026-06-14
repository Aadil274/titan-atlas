from app.engines.critical_node_engine import (
    get_critical_nodes
)

from app.engines.risk_ranking_engine import (
    generate_network_ranking
)


def build_dashboard():

    critical = get_critical_nodes()

    rankings = generate_network_ranking()

    highest_risk = rankings["rankings"][0]

    return {
        "highest_risk_node":
            highest_risk["node"],

        "highest_risk_score":
            highest_risk["resilience_score"],

        "critical_nodes":
            critical,

        "systemic_rankings":
            rankings["rankings"][:10]
    }