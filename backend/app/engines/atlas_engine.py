from app.database.neo4j import neo4j_conn

from app.graph.graph_queries import find_node

from app.engines.scoring_engine import (
    calculate_risk_score,
    get_criticality
)


def get_impact_chain(node_name):

    query = """
    MATCH path=
    (n {name:$node_name})
    -[:SUPPLIES|AFFECTS|HOSTS*1..5]->
    (m)

    RETURN path
    ORDER BY length(path) DESC
    LIMIT 1
    """

    with neo4j_conn.driver.session() as session:

        result = session.run(
            query,
            node_name=node_name
        ).single()

        if not result:
            return [node_name]

        path = result["path"]

        chain = []

        for node in path.nodes:
            chain.append(node["name"])

        return chain


def analyze_impact(search_term):

    node = find_node(search_term)

    if not node:
        return {
            "error": "Node not found"
        }

    node_name = node["name"]

    query = """
    MATCH path=
    (n {name:$node_name})
    -[:SUPPLIES|AFFECTS|HOSTS*1..5]->
    (m)

    RETURN DISTINCT m.name as affected
    """

    affected = []

    with neo4j_conn.driver.session() as session:

        results = session.run(
            query,
            node_name=node_name
        )

        for record in results:
            affected.append(record["affected"])

    blast_radius = len(affected)

    risk_score = calculate_risk_score(
        blast_radius
    )

    criticality = get_criticality(
        risk_score
    )

    impact_chain = get_impact_chain(
        node_name
    )

    return {
        "source": node_name,
        "impact_chain": impact_chain,
        "affected_nodes": affected,
        "blast_radius": blast_radius,
        "risk_score": risk_score,
        "criticality": criticality
    }