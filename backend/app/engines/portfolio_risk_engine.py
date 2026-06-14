from collections import Counter

from app.engines.dependency_engine import (
    get_dependency_chain
)


def analyze_portfolio(nodes):

    dependency_counter = Counter()

    node_chains = {}

    for node in nodes:

        chain = get_dependency_chain(node)

        if not chain:
            continue

        dependencies = chain.get(
            "full_dependency_chain",
            []
        )

        node_chains[node] = dependencies

        for dependency in dependencies[1:]:

            dependency_counter[
                dependency
            ] += 1

    shared_dependencies = []

    for dependency, count in dependency_counter.items():

        if count > 1:
            shared_dependencies.append(
                dependency
            )

    shared_dependencies.sort()

    concentration_score = 0

    if nodes:

        scores = []

        portfolio_size = len(nodes)

        for dependency in shared_dependencies:

            count = dependency_counter[dependency]

            scores.append(
                (count / portfolio_size) * 100
            )

        concentration_score = (
            int(sum(scores) / len(scores))
            if scores
            else 0
        ) if dependency_counter else 0

    if concentration_score >= 70:
        risk_level = "HIGH"

    elif concentration_score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {

        "portfolio": nodes,

        "portfolio_risk":
            risk_level,

        "concentration_score":
            concentration_score,

        "shared_dependencies":
            shared_dependencies,

        "single_points_of_failure":
            shared_dependencies,

        "dependency_chains":
            node_chains
    }