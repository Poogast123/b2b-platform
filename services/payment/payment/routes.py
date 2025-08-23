from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from . import schemas, controllers

router = APIRouter()

@router.post("/", response_model=schemas.PaymentOut)
def make_payment(data: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return controllers.create_payment(db, data)

@router.get("/{reference}", response_model=schemas.PaymentOut)
def check_payment(reference: str, db: Session = Depends(get_db)):
    payment = controllers.get_payment_by_reference(db, reference)
    if not payment:
        raise HTTPException(status_code=404, detail="Paiement introuvable")
    return payment
