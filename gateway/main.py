from fastapi import FastAPI, Request
from proxy import forward_request
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="API Gateway")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Proxy routes
@app.api_route("/app/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_auth(request: Request, path: str):
    return await forward_request(request, f"http://auth:8000/{path}")

@app.api_route("/user/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_user(request: Request, path: str):
    return await forward_request(request, f"http://user:8000/{path}")

@app.api_route("/payment/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_payment(request: Request, path: str):
    return await forward_request(request, f"http://payment:8000/{path}")

@app.api_route("/document/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_document(request: Request, path: str):
    return await forward_request(request, f"http://document:8000/{path}")
