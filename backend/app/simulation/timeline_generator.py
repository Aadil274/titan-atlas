def generate_timeline(cascade):

    timeline = {
        "day_0": [],
        "day_7": [],
        "day_30": []
    }

    level_map = {}

    roots = set(cascade.keys())

    children = set()

    for nodes in cascade.values():
        children.update(nodes)

    source_nodes = roots - children

    if not source_nodes:
        return timeline

    source = list(source_nodes)[0]

    queue = [(source, 0)]

    visited = set()

    while queue:

        node, depth = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)

        if depth > 0:

            if depth == 1:
                timeline["day_0"].append(node)

            elif depth == 2:
                timeline["day_7"].append(node)

            else:
                timeline["day_30"].append(node)

        for child in cascade.get(node, []):

            queue.append(
                (child, depth + 1)
            )

    return timeline