from fastapi import FastAPI
from document.routes import router

app = FastAPI()

app.include_router(router, prefix="/document", tags=["Document"])

@app.get("/")
async def root():
    return {"message": "B2B Platform API is running"}