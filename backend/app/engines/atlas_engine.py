from app.database.neo4j import neo4j_conn

def analyze_impact(node_name):

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

    return {
        "source": node_name,
        "affected_nodes": affected,
        "blast_radius": len(affected)
    }