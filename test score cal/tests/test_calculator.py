import unittest

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


class TestTrustCalculator(unittest.TestCase):

    def test_weights(self):
        self.assertEqual(round(sum(weights.values()), 2), 1.0)

    def test_score(self):
        self.assertEqual(
            calculate_trust_score(scores, weights),
            90.85
        )

    def test_low_risk(self):
        self.assertEqual(
            determine_risk(95),
            "Low Risk"
        )

    def test_medium_risk(self):
        self.assertEqual(
            determine_risk(80),
            "Medium Risk"
        )

    def test_high_risk(self):
        self.assertEqual(
            determine_risk(60),
            "High Risk"
        )


if __name__ == "__main__":
    unittest.main()