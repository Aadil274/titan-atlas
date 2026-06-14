from app.engines.risk_exposure_engine import (
    generate_risk_exposure_report
)


def compare_risk(node1, node2):

    report1 = generate_risk_exposure_report(
        node1
    )

    report2 = generate_risk_exposure_report(
        node2
    )

    score1 = report1["resilience_score"]
    score2 = report2["resilience_score"]

    if score1 > score2:
        safer = node1
        riskier = node2
    elif score2 > score1:
        safer = node2
        riskier = node1
    else:
        safer = None
        riskier = None
    
    reason = ""

    if riskier:

        riskier_report = (
            report1
            if riskier == node1
            else report2
        )

        reason = (
            f"{riskier} has a lower resilience score "
            f"and greater systemic exposure."
        )

    return {
        "node_1": node1,
        "node_2": node2,

        "node_1_score": score1,
        "node_2_score": score2,

        "safer_entity": safer,
        "riskier_entity": riskier,

        "score_difference":
            abs(score1 - score2),
        
        "analysis": reason
    }