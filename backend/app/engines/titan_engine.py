from app.graph.graph_queries import find_node
from app.simulation.propagation_engine import (
    build_dependency_cascade
)
from app.simulation.timeline_generator import (
    generate_timeline
)
from app.ai.executive_briefs import (
    generate_brief
)


def run_dynamic_simulation(search_term):

    node = find_node(search_term)

    if not node:
        return None

    source = node["name"]

    cascade = build_dependency_cascade(source)

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

    timeline = generate_timeline(cascade)

    simulation_result = {
        "scenario": f"{source} Disruption",

        "event": "dynamic_failure",

        "source": source,

        "severity": severity,

        "blast_radius": blast_radius,

        "affected_nodes": affected_nodes,

        "cascade": cascade,

        "timeline": timeline
    }

    brief = generate_brief(
        simulation_result
    )

    return {
        "simulation": simulation_result,
        "executive_brief": brief
    }