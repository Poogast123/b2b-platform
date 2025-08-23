import httpx
from fastapi import Request, Response

async def forward_request(request: Request, target_url: str):
    async with httpx.AsyncClient() as client:
        method = request.method
        body = await request.body()
        headers = dict(request.headers)

        response = await client.request(
            method,
            target_url,
            content=body,
            headers=headers,
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
