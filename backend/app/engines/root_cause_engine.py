from app.engines.dependency_engine import get_dependency_chain


def explain_dependency(node_name):

    return get_dependency_chain(node_name)