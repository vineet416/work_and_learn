# Task 10: Custom Host Port Mapping

## Objective
Run the same FastAPI Docker image on host port 5000 while keeping the container port at 8000.

## Run the Container

```powershell id="2vm7bs"
docker run -d --name docker-task-10 -p 5000:8000 super30-fastapi-app
```

## Port Mapping

- Host port: `5000`
- Container port: `8000`

## Verification

The following URLs successfully displayed FastAPI Swagger UI:

- Task 9: `http://localhost:8000/docs`
- Task 10: `http://localhost:5000/docs`

Both containers were running simultaneously and exposed the same API endpoints.

## Explanation

Docker's `-p HOST_PORT:CONTAINER_PORT` syntax forwards traffic from the selected host port to the application port inside the container.