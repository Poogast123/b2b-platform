from fastapi import APIRouter
from pydantic import BaseModel
import controller


class UserIn(BaseModel):
    name: str
    email: str
    company: str

router = APIRouter()

@router.get("/")
def get_users():
    return controller.get_all_users()

@router.post("/")
def add_user(user: UserIn):
    return controller.create_user(user)


@router.get("/profile")
def get_profile():
    # Exemple simple, adapter selon ton controller
    return {"name": "John Doe", "email": "john@example.com", "company": "BH3 MEDIA"}
