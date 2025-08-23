from sqlalchemy import Column, Integer, String, Float
from database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    client = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")
    reference = Column(String, unique=True, nullable=False)
