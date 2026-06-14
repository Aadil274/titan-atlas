from app.graph.graph_queries import find_node


FAILURE_WORDS = [
    "fail",
    "fails",
    "failure",
    "down",
    "offline",
    "outage",
    "disruption",
    "collapses",
    "collapse"
]


def extract_entities(question):

    words = question.split()

    entities = []

    for size in [3, 2, 1]:

        for i in range(len(words) - size + 1):

            phrase = " ".join(words[i:i+size])

            node = find_node(phrase)

            if node and node["name"] not in entities:
                entities.append(node["name"])

    return entities

def classify_query(question):

    q = question.lower()

    if "why" in q:
        return "root_cause"

    if (
        " and " in q
        and any(
            word in q
            for word in FAILURE_WORDS
        )
    ):
        return "multi_failure"

    if "lose" in q or "loses" in q:
        return "dependency_failure"

    for word in FAILURE_WORDS:

        if word in q:
            return "failure"

    return "unknown"

def analyze_question(question):

    entities = extract_entities(question)

    query_type = classify_query(question)

    return {
        "query_type": query_type,
        "entities": entities
    }