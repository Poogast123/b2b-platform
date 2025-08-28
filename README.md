# Setup (Step by Step)

## 1) Install prerequisites
- Install Docker Desktop (Windows/macOS) or Docker Engine (Linux).
- Ensure Docker Compose is available (Docker Desktop includes it).

docker --version

docker compose version

## 2) Clone the repository
git clone https://github.com/Poogast123/b2b-platform.git

cd b2b-platform

## 3) Build and start the stack
docker compose up --build -d

## 4) Check containers & health
docker compose ps

docker compose logs -f

