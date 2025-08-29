from pydantic import BaseModel, constr

class PaymentCreate(BaseModel):
    client: str
    amount: float
    reference: str
    card_number: constr(min_length=13, max_length=19)  # basic length validation
    cardholder_name: str
    expiry_date: constr(pattern=r"^(0[1-9]|1[0-2])\/\d{2}$")
    cvv: constr(min_length=3, max_length=4)  # 3 or 4 digits

class PaymentOut(BaseModel):
    id: int
    client: str
    amount: float
    status: str
    reference: str

    class Config:
        orm_mode = True
