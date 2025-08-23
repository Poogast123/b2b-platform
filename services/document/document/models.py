from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["b2b_documents"]

def document_helper(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "type": doc["type"],
        "client": doc["client"],
        "content": doc["content"],
    }
