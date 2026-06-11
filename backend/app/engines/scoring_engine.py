def calculate_risk_score(blast_radius: int):

    score = blast_radius * 20

    return min(score, 100)


def get_criticality(score: int):

    if score >= 80:
        return "HIGH"

    if score >= 50:
        return "MEDIUM"

    return "LOW"