from pydantic import BaseModel

class PaymentCreate(BaseModel):
    client: str
    amount: float
    reference: str

class PaymentOut(BaseModel):
    id: int
    client: str
    amount: float
    status: str
    reference: str

    class Config:
        orm_mode = True
