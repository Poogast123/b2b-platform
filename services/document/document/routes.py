from fastapi import APIRouter, HTTPException
from .schemas import DocumentCreate, DocumentOut
from .controllers import create_document, get_document_by_id, get_documents_by_client

router = APIRouter()

@router.post("/", response_model=DocumentOut)
async def add_doc(data: DocumentCreate):
    return await create_document(data)

@router.get("/{doc_id}", response_model=DocumentOut)
async def get_doc(doc_id: str):
    doc = await get_document_by_id(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document introuvable")
    return doc

@router.get("/client/{client}", response_model=list[DocumentOut])
async def get_by_client(client: str):
    return await get_documents_by_client(client)
