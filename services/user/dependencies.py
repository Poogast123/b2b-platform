from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import requests
import os

# OAuth2 scheme, points to your auth login endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://auth_service:8000/login")

# Use the Docker service name and container port (inside Docker)
AUTH_URL = os.getenv("AUTH_URL", "http://auth_service:8000/auth/verify")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Call the auth microservice to verify the token
        resp = requests.get(
            AUTH_URL,  # use the variable instead of hardcoded localhost
            headers={"Authorization": f"Bearer {token}"}
        )
        if resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid token")
        return resp.json()  # contains {"status": "valid", "email": ...}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
