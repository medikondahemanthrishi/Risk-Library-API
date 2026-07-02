
from pydantic import BaseModel
from datetime import datetime


class Risk(BaseModel):
    """
    Risk Model

    This model defines the structure of every
    Risk document that will be stored in MongoDB.
    """

    id: str

    name: str

    description: str


    category: str

    severity: str

    archetype: str
    trust_attribute: str

    created_at: datetime

    version: str