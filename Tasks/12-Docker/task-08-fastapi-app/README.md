# Task 08: Containerize a FastAPI Application

## Objective
Create a simple FastAPI application and package it into a Docker image.

## Project Structure

```text
task-08-fastapi-app/
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Dependencies

```text
fastapi
uvicorn[standard]
```

## Dockerfile

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Build the Image

```powershell
docker build -t super30-fastapi-app .
```

## Verification

The image built successfully and is available locally as `super30-fastapi-app:latest`.