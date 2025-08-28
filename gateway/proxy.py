import httpx
from fastapi import Request, Response, HTTPException

async def forward_request(request: Request, target_url: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            method = request.method
            body = await request.body()

            # Clean headers to avoid conflicts
            headers = {
                k: v for k, v in request.headers.items()
                if k.lower() not in ["host", "content-length", "transfer-encoding"]
            }

            response = await client.request(
                method,
                target_url,
                content=body,
                headers=headers,
            )

            # Return response from the microservice
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers={k: v for k, v in response.headers.items() if k.lower() != "transfer-encoding"},
            )
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Microservice unavailable")
