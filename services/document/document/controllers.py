from .models import db, document_helper
from .schemas import DocumentCreate
from bson.objectid import ObjectId

async def create_document(data: DocumentCreate):
    doc = data.dict()
    result = await db.documents.insert_one(doc)
    new_doc = await db.documents.find_one({"_id": result.inserted_id})
    return document_helper(new_doc)

async def get_document_by_id(doc_id: str):
    doc = await db.documents.find_one({"_id": ObjectId(doc_id)})
    if doc:
        return document_helper(doc)
    return None

async def get_documents_by_client(client: str):
    docs = db.documents.find({"client": client})
    return [document_helper(d) async for d in docs]
