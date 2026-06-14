from app.engines.atlas_engine import analyze_impact


def generate_recommendations(node_name):

    impact = analyze_impact(node_name)

    if not impact:
        return None

    blast_radius = impact["blast_radius"]

    recommendations = []

    risk_type = "Localized Risk"

    if blast_radius >= 5:

        risk_type = "Systemic Risk"

        recommendations.append({
            "action":
                "Diversify suppliers",
            "reason":
                f"{node_name} impacts a large portion of the network."
        })

        recommendations.append({
            "action":
                "Introduce redundancy",
            "reason":
                "A single failure creates cascading effects."
        })

    elif blast_radius >= 3:

        risk_type = "Concentration Risk"

        recommendations.append({
            "action":
                "Add secondary providers",
            "reason":
                "Dependencies are concentrated around one entity."
        })

    else:

        recommendations.append({
            "action":
                "Monitor dependency health",
            "reason":
                "Current impact is limited but still measurable."
        })

    return {
        "node": node_name,
        "risk_type": risk_type,
        "blast_radius": blast_radius,
        "recommendations": recommendations
    }