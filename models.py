# ============================================
# models.py
# Pydantic Model for Risk Library
# ============================================

from pydantic import BaseModel
from datetime import datetime


class Risk(BaseModel):
    """
    Risk Model

    This model defines the structure of every
    Risk document that will be stored in MongoDB.
    """

    # Unique Risk ID
    id: str

    # Risk Name
    name: str

    # Detailed Description
    description: str

    # Category
    # business / technical / security /
    # compliance / deployment
    category: str

    # Severity
    # critical / high / medium / low
    severity: str

    # Archetype
    # RAG / Agentic
    archetype: str

    # Trust Attribute
    # Safety / Privacy / Reliability /
    # Transparency / Fairness etc.
    trust_attribute: str

    # Creation Date
    created_at: datetime

    # Version
    version: str