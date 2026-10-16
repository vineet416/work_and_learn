# Task 11: Essential Dockerfile Instructions

## Objective
Understand the purpose of `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, and `CMD` in a Dockerfile.

## Dockerfile Example

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Explanation

### 1. WORKDIR
Sets `/app` as the working directory for subsequent instructions. Docker creates the directory if it doesn't exist.

### 2. COPY
Copies files from the build context into the image. For example, `COPY main.py .` copies `main.py` into `/app`.

### 3. RUN
Executes a command while building the image. Here, it installs the Python dependencies from `requirements.txt`.

### 4. EXPOSE
Documents that the application listens on port 8000. It does not publish the port to the host by itself.

### 5. CMD
Defines the default command to run when a container starts. Here, it launches the FastAPI application using Uvicorn.