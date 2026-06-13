INDUSTRY_MAP = {
    "TSMC": "Semiconductors",
    "ASML": "Semiconductors",
    "NVIDIA": "Semiconductors",
    "AMD": "Semiconductors",

    "AWS": "Cloud Computing",
    "Azure": "Cloud Computing",
    "Google Cloud": "Cloud Computing",

    "OpenAI": "Artificial Intelligence",
    "Anthropic": "Artificial Intelligence",
    "Cohere": "Artificial Intelligence"
}

def generate_brief(simulation_result):

    scenario = simulation_result["scenario"]
    severity = simulation_result["severity"]

    source = simulation_result["source"]

    affected_nodes = simulation_result.get(
        "affected_nodes",
        []
    )

    timeline = simulation_result.get(
        "timeline",
        {}
    )

    day_0 = timeline.get("day_0", [])
    day_7 = timeline.get("day_7", [])
    day_30 = timeline.get("day_30", [])

    industries = set()

    for node in affected_nodes:

        industry = INDUSTRY_MAP.get(node)

        if industry:
            industries.add(industry)

    summary = (
        f"A disruption at {source} propagates through "
        f"the dependency network and affects downstream organizations."
    )

    findings = []

    if day_0:
        findings.append(
            f"Immediate impact on: {', '.join(day_0)}"
        )

    if day_7:
        findings.append(
            f"Secondary impacts within 7 days: {', '.join(day_7)}"
        )

    if day_30:
        findings.append(
            f"Long-term impacts within 30 days: {', '.join(day_30)}"
        )

    most_exposed = []

    most_exposed.extend(day_0)
    most_exposed.extend(day_7)
    most_exposed.extend(day_30)

    most_exposed = most_exposed[:5]

    return {
        "title": scenario,

        "severity": severity,

        "primary_bottleneck": source,

        "affected_industries": list(industries),

        "most_exposed_entities": most_exposed,

        "summary": summary,

        "key_findings": findings,

        "recommendation":
            "Reduce dependency concentration and diversify critical infrastructure suppliers."
    }