from app.engines.hidden_dependency_engine import (
    find_hidden_dependencies
)

from app.api.atlas import (
    dependencies
)

from app.engines.vulnerability_engine import (
    calculate_vulnerability
)

from app.engines.resilience_score_engine import (
    calculate_resilience_score
)

from app.ai.alternative_engine import (
    get_alternatives
)

from app.ai.recommendation_engine import (
    generate_recommendations
)


def generate_risk_exposure_report(node_name):

    vulnerability = calculate_vulnerability(
        node_name
    )

    hidden = find_hidden_dependencies(
        node_name
    )

    score = calculate_resilience_score(
        node_name
    )

    alternatives = get_alternatives(
        node_name
    )

    recommendations = generate_recommendations(
        node_name
    )

    hidden_dependencies = hidden.get(
        "hidden_dependencies",
        []
    )

    summary = (
        f"{node_name} has a "
        f"{score['risk_level']} risk profile "
        f"with {len(hidden_dependencies)} "
        f"hidden dependencies."
    )

    primary_hidden_risk = (
        hidden_dependencies[-1]
        if hidden_dependencies
        else None
    )

    canonical_name = dependencies[0]   

    return {
        "node": canonical_name,

        "summary": summary,

        "primary_hidden_risk":
            primary_hidden_risk,

        "direct_dependency":
            hidden.get(
                "direct_dependency"
            ),

        "hidden_dependencies":
            hidden_dependencies,

        "resilience_score":
            score["resilience_score"],
        
        "vulnerability_score":
            vulnerability["vulnerability_score"],

        "vulnerability_level":
            vulnerability["vulnerability_level"],

        "risk_level":
            score["risk_level"],

        "alternatives":
            alternatives["alternatives"],

        "recommendations":
            recommendations["recommendations"]
    }