from app.engines.dependency_engine import (
    get_dependency_chain
)


def find_hidden_dependencies(node_name):

    chain = get_dependency_chain(node_name)

    if not chain:
        return None

    dependencies = chain.get(
        "full_dependency_chain",
        []
    )

    depth = max(
        len(dependencies) - 1,
        0
    )

    if len(dependencies) <= 2:

        return {
            "node": node_name,
            "dependency_depth": depth,
            "direct_dependency":
                dependencies[1]
                if len(dependencies) > 1
                else None,
            "hidden_dependencies": []
        }

    hidden = dependencies[2:]

    return {
        "node": node_name,
        "dependency_depth": depth,
        "direct_dependency":
            dependencies[1],
        "hidden_dependencies":
            hidden
    }