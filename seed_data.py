# ============================================
# seed_data.py
# Insert Sample Risk Data into MongoDB
# ============================================

from datetime import datetime
from database import collection

# --------------------------------------------
# Sample Risk Data
# --------------------------------------------
risks = [

    # ========================================
    # RAG RISKS
    # ========================================

    {
        "id": "R001",
        "name": "Hallucinated Retrieval",
        "description": "The LLM generates incorrect answers due to irrelevant or inaccurate retrieved documents.",
        "category": "technical",
        "severity": "high",
        "archetype": "RAG",
        "trust_attribute": "Reliability",
        "created_at": datetime.now(),
        "version": "1.0"
    },

    {
        "id": "R002",
        "name": "Sensitive Document Exposure",
        "description": "Sensitive information from the knowledge base may be exposed to unauthorized users.",
        "category": "security",
        "severity": "critical",
        "archetype": "RAG",
        "trust_attribute": "Privacy",
        "created_at": datetime.now(),
        "version": "1.0"
    },

    {
        "id": "R003",
        "name": "Outdated Knowledge Base",
        "description": "Retrieved documents may be outdated, causing inaccurate responses.",
        "category": "business",
        "severity": "medium",
        "archetype": "RAG",
        "trust_attribute": "Accuracy",
        "created_at": datetime.now(),
        "version": "1.0"
    },

    # ========================================
    # AGENTIC RISKS
    # ========================================

    {
        "id": "A001",
        "name": "Prompt Injection",
        "description": "Malicious prompts manipulate the agent into performing unintended actions.",
        "category": "security",
        "severity": "critical",
        "archetype": "Agentic",
        "trust_attribute": "Safety",
        "created_at": datetime.now(),
        "version": "1.0"
    },

    {
        "id": "A002",
        "name": "Infinite Agent Loop",
        "description": "The autonomous agent repeatedly executes the same task without termination.",
        "category": "technical",
        "severity": "high",
        "archetype": "Agentic",
        "trust_attribute": "Reliability",
        "created_at": datetime.now(),
        "version": "1.0"
    },

    {
        "id": "A003",
        "name": "Unauthorized Tool Usage",
        "description": "The agent accesses tools or resources without proper authorization.",
        "category": "compliance",
        "severity": "medium",
        "archetype": "Agentic",
        "trust_attribute": "Governance",
        "created_at": datetime.now(),
        "version": "1.0"
    }

]

# --------------------------------------------
# Insert Risks
# --------------------------------------------
for risk in risks:

    # Skip duplicate IDs
    if collection.find_one({"id": risk["id"]}) is None:

        collection.insert_one(risk)

        print(f"Inserted : {risk['id']}")

    else:

        print(f"Already Exists : {risk['id']}")

print("\nRisk Library Seed Completed Successfully.")