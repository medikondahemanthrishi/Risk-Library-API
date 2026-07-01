
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")

db = client["risk_library_db"]

collection = db["risk_library"]

collection.create_index("id", unique=True)
collection.create_index("archetype")
collection.create_index("severity")