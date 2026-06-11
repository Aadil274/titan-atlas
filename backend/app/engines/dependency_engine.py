from app.database.neo4j import neo4j_conn
from app.graph.graph_queries import find_node


def get_dependency_chain(search_term):

    node = find_node(search_term)

    if not node:
        return None

    node_name = node["name"]

    query = """
    MATCH path =
    (n {name:$node_name})
    <-[:DEPENDS_ON|HOSTS|SUPPLIES*1..5]-
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
            return {
                "node": node_name,
                "direct_dependencies": [],
                "full_dependency_chain": [node_name],
                "depth": 0
            }

        path = result["path"]

        chain = []

        for node in path.nodes:
            chain.append(node["name"])

        return {
            "node": node_name,
            "full_dependency_chain": chain,
            "depth": len(chain) - 1
        }