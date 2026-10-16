# Task 13: Environment Variables in Docker

## Objective

Pass environment variables to a Docker container and access them from a Python application.

## Project Structure

```text
task-13-environment-variables/
├── main.py
├── Dockerfile
└── README.md
```

## Python Application

The application reads environment variables using Python's `os.getenv()`.

```python
import os

app_name = os.getenv("APP_NAME", "Default Application")
environment = os.getenv("APP_ENV", "development")

print(f"Application: {app_name}")
print(f"Environment: {environment}")
```

## Dockerfile

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]
```

## Build the Image

```powershell
docker build -t super30-task-13 .
```

## Run with Custom Environment Variables

```powershell
docker run --rm `
  -e APP_NAME="Super30 Docker Demo" `
  -e APP_ENV="testing" `
  --name docker-task-13 `
  super30-task-13
```

### Output

```text
Application: Super30 Docker Demo
Environment: testing
```

## Run with Default Values

```powershell
docker run --rm super30-task-13
```

### Output

```text
Application: Default Application
Environment: development
```

## Key Concepts

- `-e` passes environment variables into a container.
- `os.getenv()` reads environment variables in Python.
- Default values are used when variables are not provided.
- `--rm` automatically removes the container after it exits.

## Verification

- Docker image built successfully.
- Custom environment variables were read correctly.
- Default values worked when no variables were supplied.
- Both executions completed successfully.