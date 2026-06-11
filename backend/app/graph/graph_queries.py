from app.database.neo4j import neo4j_conn


def find_node(search_term):

    query = """
    MATCH (n)
    WHERE
        toLower(n.name) = toLower($search)
        OR
        any(alias IN coalesce(n.aliases, [])
            WHERE toLower(alias) = toLower($search))

    RETURN n.name as name,
           labels(n)[0] as node_type
    LIMIT 1
    """

    with neo4j_conn.driver.session() as session:

        result = session.run(
            query,
            search=search_term
        ).single()

        if not result:
            return None

        return {
            "name": result["name"],
            "type": result["node_type"]
        }
    
def get_node_dependencies(node_name):

    query = """
    MATCH (n {name:$node_name})-[r]->(m)
    RETURN type(r) as relationship,
           m.name as dependency
    """

    results = []

    with neo4j_conn.driver.session() as session:

        records = session.run(
            query,
            node_name=node_name
        )

        for record in records:

            results.append({
                "relationship": record["relationship"],
                "dependency": record["dependency"]
            })

    return results