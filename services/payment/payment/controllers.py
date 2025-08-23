from sqlalchemy.orm import Session
from . import models, schemas
import random

def create_payment(db: Session, payment_data: schemas.PaymentCreate):
    # Simuler acceptation/rejet (version future : Stripe API)
    status = "success" if random.random() > 0.2 else "failed"
    payment = models.Payment(
        client=payment_data.client,
        amount=payment_data.amount,
        reference=payment_data.reference,
        status=status
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

def get_payment_by_reference(db: Session, ref: str):
    return db.query(models.Payment).filter(models.Payment.reference == ref).first()
