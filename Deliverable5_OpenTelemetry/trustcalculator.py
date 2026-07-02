def calculate_trust_score(scores, weights):
    """
    Calculates the weighted trust score.
    """
    
    if round(sum(weights.values()), 2) != 1.0:
        raise ValueError("Error: Weights must sum to 1.0")

    trust_score = 0

    for key in scores:
        trust_score += scores[key] * weights[key]

    return round(trust_score, 2)


def determine_risk(score):
    """
    Determines the risk level.
    """

    if score >= 90:
        return "Low Risk"

    elif score >= 70:
        return "Medium Risk"

    else:
        return "High Risk"