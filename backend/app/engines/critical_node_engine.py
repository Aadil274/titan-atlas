from app.database.neo4j import neo4j_conn

from app.engines.atlas_engine import analyze_impact


def get_critical_nodes():

    query = """
    MATCH (n)
WHERE EXISTS {
    MATCH (n)-[:SUPPLIES|AFFECTS|HOSTS]->()
}
OR EXISTS {
    MATCH ()-[:SUPPLIES|AFFECTS|HOSTS]->(n)
}
RETURN DISTINCT n.name as name
    """

    nodes = []

    with neo4j_conn.driver.session() as session:

        results = session.run(query)

        for record in results:
            nodes.append(record["name"])

    analysis = []

    for node in nodes:

        result = analyze_impact(node)

        if not result:
            continue

        if "error" in result:
            continue

        analysis.append({
            "node": node,
            "blast_radius": result.get("blast_radius", 0),
            "risk_score": result.get("risk_score", 0),
            "criticality": result.get("criticality", "LOW")
        })

    analysis.sort(
        key=lambda x: x["risk_score"],
        reverse=True
    )

    return analysis