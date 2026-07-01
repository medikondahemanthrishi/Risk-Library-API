# ============================================
# crud.py
# CRUD Operations for Risk Library
# ============================================

from database import collection


# ---------------------------------------------------
# Create Risk
# ---------------------------------------------------
def create_risk(risk):

    # Convert Pydantic object into dictionary
    data = risk.model_dump()

    # Insert into MongoDB
    collection.insert_one(data)

    return {
        "message": "Risk Added Successfully"
    }


# ---------------------------------------------------
# Get All Risks
# ---------------------------------------------------
def get_all_risks():

    risks = []

    # Read every document
    for risk in collection.find():

        # Convert ObjectId into string
        risk["_id"] = str(risk["_id"])

        risks.append(risk)

    return risks


# ---------------------------------------------------
# Get Risk By ID
# ---------------------------------------------------
def get_risk_by_id(risk_id):

    risk = collection.find_one({"id": risk_id})

    if risk:

        risk["_id"] = str(risk["_id"])

        return risk

    return {
        "message": "Risk Not Found"
    }


# ---------------------------------------------------
# Update Risk
# ---------------------------------------------------
def update_risk(risk_id, risk):

    result = collection.update_one(
        {"id": risk_id},
        {
            "$set": risk.model_dump()
        }
    )

    if result.modified_count > 0:
        return {
            "message": "Risk Updated Successfully"
        }

    return {
        "message": "Risk Not Found"
    }


# ---------------------------------------------------
# Delete Risk
# ---------------------------------------------------
def delete_risk(risk_id):

    result = collection.delete_one(
        {
            "id": risk_id
        }
    )

    if result.deleted_count > 0:
        return {
            "message": "Risk Deleted Successfully"
        }

    return {
        "message": "Risk Not Found"
    }


# ---------------------------------------------------
# Search Risks
# ---------------------------------------------------
def search_risks(archetype, severity):

    risks = []

    query = {
        "archetype": archetype,
        "severity": severity
    }

    for risk in collection.find(query):

        risk["_id"] = str(risk["_id"])

        risks.append(risk)

    return risks