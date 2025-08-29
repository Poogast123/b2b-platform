from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, controllers


router = APIRouter()

@router.post("/", response_model=schemas.PaymentOut)
def make_payment(data: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return controllers.create_payment(db, data)

@router.get("/transactions", response_model=list[schemas.PaymentOut])
def list_transactions(db: Session = Depends(get_db)):
    # Fetch all payments from the database
    payments = controllers.get_all_payments(db)
    return payments


@router.get("/{reference}", response_model=schemas.PaymentOut)
def check_payment(reference: str, db: Session = Depends(get_db)):
    payment = controllers.get_payment_by_reference(db, reference)
    if not payment:
        raise HTTPException(status_code=404, detail="Paiement introuvable")
    return payment

