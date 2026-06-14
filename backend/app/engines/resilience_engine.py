from app.engines.atlas_engine import analyze_impact
from app.graph.graph_queries import (
    get_all_nodes
)


def find_single_points_of_failure():

    nodes = get_all_nodes()

    results = []

    for node in nodes:

        impact = analyze_impact(node)

        if not impact:
            continue

        blast_radius = impact.get(
            "blast_radius",
            0
        )

        if blast_radius > 0:

            severity = "LOW"

            if blast_radius >= 5:
                severity = "HIGH"
            elif blast_radius >= 3:
                severity = "MEDIUM"

            results.append({
                "node": node,
                "blast_radius": blast_radius,
                "severity": severity
            })

    results.sort(
        key=lambda x: x["blast_radius"],
        reverse=True
    )

    return results[:10]

def recommend_mitigation(node_name):

    recommendations = {

        "TSMC": [
            "Diversify semiconductor manufacturing",
            "Add Samsung as alternate supplier",
            "Increase chip inventory reserves"
        ],

        "NVIDIA": [
            "Use multiple AI accelerator vendors",
            "Reduce compute concentration"
        ],

        "AWS": [
            "Adopt multi-cloud strategy",
            "Deploy workloads on Azure"
        ],

        "Azure": [
            "Adopt multi-cloud strategy",
            "Deploy workloads on AWS"
        ]
    }

    return {
        "node": node_name,
        "recommendations":
            recommendations.get(
                node_name,
                ["No recommendation available"]
            )
    }