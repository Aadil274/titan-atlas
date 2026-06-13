from app.database.neo4j import neo4j_conn


def build_dependency_cascade(source_node):

    cascade = {}
    visited = set()

    def traverse(node_name):

        if node_name in visited:
            return

        visited.add(node_name)

        query = """
        MATCH (n {name:$node_name})<-[:DEPENDS_ON]-(m)
        RETURN m.name AS dependent
        """

        with neo4j_conn.driver.session() as session:

            results = session.run(
                query,
                node_name=node_name
            )

            dependents = [
                record["dependent"]
                for record in results
            ]

        if dependents:
            cascade[node_name] = dependents

        for dependent in dependents:
            traverse(dependent)

    traverse(source_node)

    return cascade