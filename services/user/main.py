from fastapi import FastAPI
from routers import user_routes
from database import Base, engine

app = FastAPI()

# Crée les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router, prefix="/user", tags=["User"])
