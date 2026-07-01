import json
import hashlib

from validator import validate_scores
from trustcalculator import calculate_trust_score
from trustcalculator import determine_risk

scores = {
    "accuracy": 95,
    "reliability": 90,
    "fairness": 85,
    "security": 92,
    "privacy": 88,
    "transparency": 90
}

weights = {
    "accuracy": 0.30,
    "reliability": 0.20,
    "fairness": 0.15,
    "security": 0.15,
    "privacy": 0.10,
    "transparency": 0.10
}

try: 
    validate_scores(scores)
    trust_score = calculate_trust_score(scores, weights)

    risk = determine_risk(trust_score)


    evidence = {
        "scores": scores,
        "weights": weights,
        "trust_score": trust_score,
        "risk_level": risk
    }
    with open("evidence.json", "w") as file:
        json.dump(evidence, file, indent=4)

    with open("evidence.json", "rb") as file:
        file_data = file.read()

    hash_value = hashlib.sha256(file_data).hexdigest()

    evidence["sha256_hash"] = hash_value

    with open("evidence.json", "w") as file:
        json.dump(evidence, file, indent=4)

    print("=" * 40)
    print("TRUST SCORE CALCULATOR")
    print("=" * 40)

    print("Trust Score :", trust_score)
    print("Risk Level  :", risk)
    print("SHA256 Hash :", hash_value)

except Exception as e:
    print(e)