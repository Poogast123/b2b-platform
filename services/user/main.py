from fastapi import FastAPI
from database import Base, engine
import routes

app = FastAPI()

# Crée les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

app.include_router(routes.router, prefix="/user", tags=["User"])
