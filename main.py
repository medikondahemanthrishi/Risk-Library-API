# ============================================
# main.py
# FastAPI Entry Point
# ============================================

from fastapi import FastAPI, Query
from models import Risk
from crud import (
    create_risk,
    get_all_risks,
    get_risk_by_id,
    update_risk,
    delete_risk,
    search_risks
)

# Create FastAPI Application
app = FastAPI(
    title="Risk Library API",
    description="API for Managing AI Risks",
    version="1.0"
)

# ---------------------------------------------------
# Home Route
# ---------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to Risk Library API"
    }


# ---------------------------------------------------
# About Route
# ---------------------------------------------------
@app.get("/about")
def about():
    return {
        "project": "Risk Library API",
        "backend": "FastAPI + MongoDB",
        "version": "1.0"
    }


# ---------------------------------------------------
# Create Risk
# ---------------------------------------------------
@app.post("/risks")
def add_risk(risk: Risk):
    return create_risk(risk)


# ---------------------------------------------------
# Get All Risks
# ---------------------------------------------------
@app.get("/risks")
def read_all_risks():
    return get_all_risks()


# ---------------------------------------------------
# Get Risk By ID
# ---------------------------------------------------
@app.get("/risks/{risk_id}")
def read_risk(risk_id: str):
    return get_risk_by_id(risk_id)


# ---------------------------------------------------
# Update Risk
# ---------------------------------------------------
@app.put("/risks/{risk_id}")
def edit_risk(risk_id: str, risk: Risk):
    return update_risk(risk_id, risk)


# ---------------------------------------------------
# Delete Risk
# ---------------------------------------------------
@app.delete("/risks/{risk_id}")
def remove_risk(risk_id: str):
    return delete_risk(risk_id)


# ---------------------------------------------------
# Search Risk
# Example:
# /search?archetype=RAG&severity=High
# ---------------------------------------------------
@app.get("/search")
def search(
    archetype: str = Query(...),
    severity: str = Query(...)
):
    return search_risks(archetype, severity)