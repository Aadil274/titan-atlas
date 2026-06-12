from app.database.neo4j import neo4j_conn
from app.graph.graph_queries import find_node


def get_dependency_chain(search_term):

    node = find_node(search_term)

    if not node:
        return None

    current = node["name"]

    chain = [current]

    visited = set()
    visited.add(current)

    with neo4j_conn.driver.session() as session:
        
        direct_dependencies = []

        while True:

            query = """
            MATCH (n {name:$node_name})-[:DEPENDS_ON]->(m)
            RETURN m.name AS dependency
            LIMIT 1
            """

            result = session.run(
                query,
                node_name=current
            ).single()

            if not result:
                break

            dependency = result["dependency"]

            if not dependency:
                break

            if dependency in visited:
                break

            if len(chain) == 1:
                direct_dependencies.append(dependency)

            chain.append(dependency)

            visited.add(dependency)

            current = dependency

    return {
        "node": node["name"],
        "direct_dependencies": direct_dependencies,
        "full_dependency_chain": chain,
        "depth": len(chain) - 1
    }