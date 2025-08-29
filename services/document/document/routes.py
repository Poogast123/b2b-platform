from fastapi import APIRouter, HTTPException
from .schemas import DocumentCreate, DocumentOut
from .controllers import create_document, get_document_by_id, get_documents_by_client, get_all_documents
from bson import ObjectId

router = APIRouter()

# Get all documents - FIXED ROUTE
@router.get("/documents", response_model=list[DocumentOut])
async def list_documents():
    return await get_all_documents()

# Add a document - FIXED ROUTE
@router.post("/documents", response_model=DocumentOut)
async def add_doc(data: DocumentCreate):
    return await create_document(data)

# Get documents by client - FIXED ROUTE
@router.get("/documents/client/{client}", response_model=list[DocumentOut])
async def get_by_client(client: str):
    return await get_documents_by_client(client)

# Get single document by ID - FIXED ROUTE
@router.get("/documents/{doc_id}", response_model=DocumentOut)
async def get_doc(doc_id: str):
    if not ObjectId.is_valid(doc_id):
        raise HTTPException(status_code=400, detail="Invalid document ID")
    doc = await get_document_by_id(doc_id)  # Removed ObjectId() conversion
    if not doc:
        raise HTTPException(status_code=404, detail="Document introuvable")
    return doc