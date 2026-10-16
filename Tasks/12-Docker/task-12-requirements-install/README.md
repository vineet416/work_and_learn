# Task 12: Install Dependencies Using requirements.txt

## Objective
Install FastAPI and Uvicorn during Docker image construction using a requirements file.

## Dependencies

```text
fastapi
uvicorn[standard]
```

## Build

```powershell
docker build -t super30-task-12 .
```

## Run

```powershell
docker run -d --name docker-task-12 -p 8012:8000 super30-task-12
```

## Verification

- Dependencies installed during image build.
- FastAPI container started successfully.
- API accessible on host port 8012.
- Root endpoint returned the expected JSON response.