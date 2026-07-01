# ============================================
# database.py
# MongoDB Connection
# ============================================

from pymongo import MongoClient

# ---------------------------------------------------
# Connect to MongoDB
# ---------------------------------------------------
# MongoDB is running locally on port 27017
client = MongoClient("mongodb://localhost:27017")

# ---------------------------------------------------
# Create / Connect to Database
# ---------------------------------------------------
db = client["risk_library_db"]

# ---------------------------------------------------
# Create / Connect to Collection
# ---------------------------------------------------
collection = db["risk_library"]

# ---------------------------------------------------
# Create Indexes
# These improve search performance.
# ---------------------------------------------------
collection.create_index("id", unique=True)
collection.create_index("archetype")
collection.create_index("severity")