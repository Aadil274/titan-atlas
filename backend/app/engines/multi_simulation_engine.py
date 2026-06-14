from app.engines.titan_engine import run_dynamic_simulation


def run_multi_simulation(nodes):

    results = []

    for node in nodes:

        result = run_dynamic_simulation(node)

        if result:
            results.append(result)

    return results