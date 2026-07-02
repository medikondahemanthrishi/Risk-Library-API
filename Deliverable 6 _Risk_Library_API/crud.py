
from database import collection


def create_risk(risk):


    data = risk.model_dump()


    collection.insert_one(data)

    return {
        "message": "Risk Added Successfully"
    }
def get_all_risks():

    risks = []

    for risk in collection.find():

        risk["_id"] = str(risk["_id"])

        risks.append(risk)

    return risks


def get_risk_by_id(risk_id):

    risk = collection.find_one({"id": risk_id})

    if risk:

        risk["_id"] = str(risk["_id"])

        return risk

    return {
        "message": "Risk Not Found"
    }

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