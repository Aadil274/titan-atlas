from app.graph.graph_queries import (
    get_all_nodes
)

from app.engines.resilience_score_engine import (
    calculate_resilience_score
)


def generate_network_ranking():

    rankings = []

    nodes = get_all_nodes()

    for node in nodes:

        score = calculate_resilience_score(
            node
        )

        if score:

            rankings.append({
                "node":
                    node,

                "resilience_score":
                    score["resilience_score"],

                "risk_level":
                    score["risk_level"],

                "blast_radius":
                    score["blast_radius"]
            })

    rankings.sort(
        key=lambda x: x["resilience_score"]
    )

    for rank, item in enumerate(
        rankings,
        start=1
    ):
        item["rank"] = rank

    return {
        "highest_risk_node":
            rankings[0]["node"],

        "lowest_risk_node":
            rankings[-1]["node"],

        "total_nodes":
            len(rankings),

        "rankings":
            rankings
    }