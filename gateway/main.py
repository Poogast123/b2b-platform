from fastapi import FastAPI, Request
from proxy import forward_request

app = FastAPI()

@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_auth(request: Request, path: str):
    return await forward_request(request, f"http://auth:8000/{path}")

@app.api_route("/user/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_user(request: Request, path: str):
    return await forward_request(request, f"http://user:8000/{path}")

@app.api_route("/payment/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_payment(request: Request, path: str):
    return await forward_request(request, f"http://payment:8000/{path}")

@app.api_route("/document/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_document(request: Request, path: str):
    return await forward_request(request, f"http://document:8000/{path}")
