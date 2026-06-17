from app.database.neo4j import neo4j_conn


def get_all_nodes():

    query = """
    MATCH (n)
    RETURN DISTINCT n.name AS name
    ORDER BY name
    """

    nodes = []

    with neo4j_conn.driver.session() as session:

        results = session.run(query)

        for record in results:

            if record["name"]:
                nodes.append(
                    record["name"]
                )

    return nodes


def get_network_stats():

    query = """
    MATCH (n)
    WITH count(n) AS total_nodes

    MATCH ()-[r]->()
    WITH total_nodes,
         count(r) AS total_relationships

    RETURN
        total_nodes,
        total_relationships
    """

    with neo4j_conn.driver.session() as session:

        result = session.run(
            query
        ).single()

        if not result:

            return {
                "total_nodes": 0,
                "total_relationships": 0
            }

        return {
            "total_nodes":
                result["total_nodes"],

            "total_relationships":
                result[
                    "total_relationships"
                ]
        }