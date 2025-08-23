from fastapi import FastAPI
from database import Base, engine
from auth import models, routes

app = FastAPI()

# Crée les tables
Base.metadata.create_all(bind=engine)

app.include_router(routes.router, prefix="/auth", tags=["Auth"])
