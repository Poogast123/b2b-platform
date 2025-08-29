from pydantic import BaseModel
from typing import Any

class DocumentCreate(BaseModel):
    type: str
    client: str
    content: dict

class DocumentOut(BaseModel):
    id: str
    type: str
    client: str
    content: dict
