from ..models.user import User
from ..database import SessionLocal
from sqlalchemy.orm import Session

def get_all_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def create_user(user_data):
    db: Session = SessionLocal()
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user
