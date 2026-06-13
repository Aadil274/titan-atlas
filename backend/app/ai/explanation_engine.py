from app.graph.graph_queries import find_node
import re

SCENARIO_PATTERNS = {
    "taiwan": "taiwan-crisis",
    "tsmc": "taiwan-crisis",

    "aws": "cloud-outage",

    "azure": "azure-outage",

    "nvidia": "ai-compute-shortage"
}

def interpret_query(user_query):

    query = user_query.lower()

    for keyword, scenario in SCENARIO_PATTERNS.items():

        if keyword in query:
            return scenario

    return None



def extract_entity(question):

    question = re.sub(r"[^\w\s]", "", question)

    words = question.lower().split()

    for size in [3, 2, 1]:

        for i in range(len(words) - size + 1):

            phrase = " ".join(words[i:i + size])

            print("Searching:", phrase)

            node = find_node(phrase)

            if node:
                return node["name"]

    return None