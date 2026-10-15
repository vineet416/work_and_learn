# Task 06: First Python Docker Image

## Objective
Create a Python application and package it into a custom Docker image.

## Project Structure

```text
task-06-python-dockerfile/
├── app.py
├── Dockerfile
└── README.md
```

## Dockerfile

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

## Build the Image

```bash
docker build -t super30-python-app .
```

## Run the Container

```bash
docker run --name docker-task-06 super30-python-app
```

## Expected Output

```text
Hello from my first Python Docker application!
Task 6: Custom Docker image built successfully.
```

## Verification

- Docker image built successfully.
- Python application executed successfully.
- Container exited with status 0.
- Image verified using `docker images super30-python-app`.