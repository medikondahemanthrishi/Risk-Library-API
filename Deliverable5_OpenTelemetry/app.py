import json
import hashlib

from validator import validate_scores
from trustcalculator import calculate_trust_score
from trustcalculator import determine_risk

from tracer import tracer


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

    with tracer.start_as_current_span("Trust Score Calculator"):

        with tracer.start_as_current_span("Input Validation") as span:

            validate_scores(scores)

            span.set_attribute("total_scores", len(scores))
            span.set_attribute("validation.status", "success")

        with tracer.start_as_current_span("Weight Normalization") as span:

            total_weight = round(sum(weights.values()), 2)

            span.set_attribute("weight.sum", total_weight)

            if total_weight != 1.0:
                raise ValueError("Weights must sum to 1.0")

        with tracer.start_as_current_span("Score Calculation") as span:

            trust_score = calculate_trust_score(scores, weights)

            risk = determine_risk(trust_score)

            span.set_attribute("trust.score", trust_score)
            span.set_attribute("risk.level", risk)

        with tracer.start_as_current_span("Evidence Generation") as span:

            evidence = {
                "scores": scores,
                "weights": weights,
                "trust_score": trust_score,
                "risk_level": risk
            }

            with open("evidence.json", "w") as file:
                json.dump(evidence, file, indent=4)

            span.set_attribute("evidence.generated", True)

        with tracer.start_as_current_span("SHA256 Hash Computation") as span:

            with open("evidence.json", "rb") as file:
                file_data = file.read()

            hash_value = hashlib.sha256(file_data).hexdigest()

            evidence["sha256_hash"] = hash_value

            with open("evidence.json", "w") as file:
                json.dump(evidence, file, indent=4)

            span.set_attribute("hash.algorithm", "SHA256")
            span.set_attribute("hash.length", len(hash_value))

        print("=" * 50)
        print("TRUST SCORE CALCULATOR")
        print("=" * 50)
        print("Trust Score :", trust_score)
        print("Risk Level  :", risk)
        print("SHA256 Hash :", hash_value)

except Exception as e:
    print(e)