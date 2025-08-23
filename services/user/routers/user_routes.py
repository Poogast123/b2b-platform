from fastapi import APIRouter
from pydantic import BaseModel
from services.user.controllers import user_controller

class UserIn(BaseModel):
    name: str
    email: str
    company: str

router = APIRouter()

@router.get("/")
def get_users():
    return user_controller.get_all_users()

@router.post("/")
def add_user(user: UserIn):
    return user_controller.create_user(user)
