from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router as auth_router

app = FastAPI()

# Include auth routes under /auth
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Crée les tables
Base.metadata.create_all(bind=engine)
