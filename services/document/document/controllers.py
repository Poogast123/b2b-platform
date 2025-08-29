from .database import db
from bson import ObjectId

def document_helper(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "type": doc["type"],
        "client": doc["client"],
        "content": doc["content"],
    }

async def get_all_documents():
    documents = []
    cursor = db.documents.find({})
    async for doc in cursor:
        documents.append(document_helper(doc))  # Use helper to format
    return documents

async def get_document_by_id(doc_id: str):
    if not ObjectId.is_valid(doc_id):
        return None
    doc = await db.documents.find_one({"_id": ObjectId(doc_id)})
    if doc:
        return document_helper(doc)  # Use helper to format
    return None

async def get_documents_by_client(client: str):
    documents = []
    cursor = db.documents.find({"client": client})
    async for doc in cursor:
        documents.append(document_helper(doc))  # Use helper to format
    return documents

async def create_document(document_data: dict):
    result = await db.documents.insert_one(document_data)
    new_doc = await db.documents.find_one({"_id": result.inserted_id})
    return document_helper(new_doc)  # Use helper to format