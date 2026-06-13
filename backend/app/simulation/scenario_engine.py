from app.simulation.scenario_library import SCENARIOS
from app.graph.graph_queries import find_node
from app.simulation.propagation_engine import (
    build_dependency_cascade
)
from app.simulation.timeline_generator import (
    generate_timeline
)

def simulate_failure(search_term):
    node = find_node(search_term)

    if not node:
        return None

    node_name = node["name"]

    cascade = build_dependency_cascade(node_name)

    timeline = generate_timeline(cascade)

    affected_nodes = set()

    for children in cascade.values():
        affected_nodes.update(children)

    affected_nodes = list(affected_nodes)

    blast_radius = len(affected_nodes)

    severity = "LOW"

    if blast_radius >= 5:
        severity = "HIGH"

    elif blast_radius >= 3:
        severity = "MEDIUM"

    return {
        "event": "failure",
        "source": node_name,
        "severity": severity,
        "blast_radius": blast_radius,
        "affected_nodes": affected_nodes,
        "cascade": cascade,
        "timeline": timeline
    }


def run_scenario(scenario_id):

    scenario = SCENARIOS.get(scenario_id)

    if not scenario:
        return None

    result = simulate_failure(
        scenario["source"]
    )

    result["scenario"] = scenario["name"]
    result["event"] = scenario["event"]

    return result