from fastapi import FastAPI
from document.routes import router

app = FastAPI()
app.include_router(router, prefix="/document", tags=["Document"])
