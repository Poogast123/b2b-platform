from sqlalchemy.orm import Session
from . import models, schemas, security

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = security.hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user and security.verify_password(password, user.hashed_password):
        return user
    return None

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
