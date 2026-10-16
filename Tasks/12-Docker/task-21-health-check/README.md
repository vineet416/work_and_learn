# Task 21 — FastAPI Health Check with Docker

## Overview

This project demonstrates how to create a health endpoint in FastAPI and configure Docker to monitor the application's health.

## Technologies

- Python
- FastAPI
- Uvicorn
- Docker

## Project Structure

```text
task-21-health-check/
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Health status |

Example response from `/health`:

```json
{
  "status": "healthy"
}
```

## Build the Image

Run from this directory:

```powershell
docker build -t super30-task-21 .
```

## Run the Container

```powershell
docker run -d --name docker-task-21 -p 8021:8000 super30-task-21
```

## Test the Health Endpoint

Open:

- http://localhost:8021/health
- http://localhost:8021/docs

Or use PowerShell:

```powershell
Invoke-RestMethod http://localhost:8021/health
```

## Check Docker Health Status

```powershell
docker ps
docker inspect --format='{{.State.Health.Status}}' docker-task-21
```

Docker may initially report `starting`. Wait for the health-check interval, then check again. A successful check should report `healthy`.

## Cleanup

```powershell
docker stop docker-task-21
docker rm docker-task-21
```

## What I Learned

- Creating a FastAPI health endpoint.
- Adding a Docker `HEALTHCHECK` instruction.
- Monitoring a container's health status.
- Testing API endpoints from a browser and PowerShell.