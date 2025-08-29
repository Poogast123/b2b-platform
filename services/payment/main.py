from fastapi import FastAPI
from payment.database import Base, engine
from payment import routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(routes.router, prefix="/payment", tags=["Payment"])
