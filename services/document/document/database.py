from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
DATABASE_NAME = os.getenv("MONGO_DB", "b2b_platform")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]