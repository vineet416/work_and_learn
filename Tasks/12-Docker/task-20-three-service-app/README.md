# Task 20 — Three-Service Docker Application

## Overview

This project demonstrates a three-service application using Docker Compose. The frontend communicates with a FastAPI backend, which connects to a PostgreSQL database.

## Architecture

```text
User's Browser
      |
      v
Frontend (Nginx)
Port 8020
      |
      | /api/ requests
      v
FastAPI Backend
Container port 8000
      |
      v
PostgreSQL Database
Container port 5432
```

All three services communicate through a custom Docker Compose network.

## Technologies Used

- Docker
- Docker Compose
- HTML, CSS and JavaScript
- Nginx
- Python
- FastAPI
- PostgreSQL
- psycopg

## Project Structure

```text
task-20-three-service-app/
├── frontend/
│   ├── index.html
│   ├── nginx.conf
│   └── Dockerfile
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Configuration

Create a `.env` file with these variables:

```dotenv
POSTGRES_DB=super30app
POSTGRES_USER=super30user
POSTGRES_PASSWORD=your-local-demo-password
```

Use `.env.example` as a template. Do not commit `.env` or real credentials to GitHub.

## Run the Application

Run these commands from this project directory:

```powershell
docker compose up --build -d
```

Check the running services:

```powershell
docker compose ps
```

View logs:

```powershell
docker compose logs frontend
docker compose logs api
docker compose logs db
```

## Access the Application

- Frontend: http://localhost:8020/
- Database connectivity check through the frontend: http://localhost:8020/api/db-check
- FastAPI documentation is available internally at `/docs` on the API service. To access it directly from the host, a port mapping would need to be configured.

Click **Check Backend & Database** on the frontend to verify the complete connection.

Expected database-check response:

```json
{
  "status": "connected",
  "database": "super30app",
  "user": "super30user"
}
```

## What I Learned

- Building a frontend Docker image with Nginx.
- Containerizing a FastAPI backend.
- Running PostgreSQL in a separate container.
- Connecting services using Docker Compose networking.
- Using environment variables for database configuration.
- Forwarding frontend API requests to the backend through Nginx.
- Starting and inspecting multiple containers with Docker Compose.

## Stop the Application

```powershell
docker compose down
```

The named PostgreSQL volume is retained when running `docker compose down`, so database data can persist between container recreations.