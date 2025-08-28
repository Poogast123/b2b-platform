from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from . import schemas, controllers, security
from .database import get_db
from jose import JWTError

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return controllers.create_user(db, user)

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = controllers.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = security.create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/verify")
def verify_token(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.replace("Bearer ", "")
    try:
        payload = security.decode_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = controllers.get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return {"status": "valid", "email": email}
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))
