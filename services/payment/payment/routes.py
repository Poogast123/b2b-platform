import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, controllers


router = APIRouter()

# Mock 3rd-party API URL (can be replaced with Stripe)
THIRD_PARTY_API_URL = "https://jsonplaceholder.typicode.com/posts"

@router.post("/process", response_model=schemas.PaymentOut)
def make_payment(data: schemas.PaymentCreate, db: Session = Depends(get_db)):
    try:
        # Step 1: Contact third-party API
        response = httpx.post(
            THIRD_PARTY_API_URL,
            json={
                "amount": data.amount,
                "card_number": data.card_number,
                "cardholder_name": data.cardholder_name,
                "expiry_date": data.expiry_date,
                "cvv": data.cvv,
            },
            timeout=10
        )

        # Step 2: Check API response
        if response.status_code not in (200, 201):
            raise HTTPException(status_code=400, detail="Paiement refusé par la banque")

        # Step 3: Save payment in local DB
        payment = controllers.create_payment(db, data)
        return payment

    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"Erreur réseau avec la banque: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur interne: {str(e)}")

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

