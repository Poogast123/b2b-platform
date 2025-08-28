from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import controller
from dependencies import get_current_user
from database import get_db


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
def get_profile(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = controller.get_user_by_email(db, current_user["email"])
    if not user:
        return {"error": "User not found"}
    return user
