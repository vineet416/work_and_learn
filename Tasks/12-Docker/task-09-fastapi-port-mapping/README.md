# Task 09: Run FastAPI in Docker

## Objective
Run a Dockerized FastAPI application on port 8000 and access it through a browser.

## Run the Container

```powershell
docker run -d --name docker-task-09 -p 8000:8000 super30-fastapi-app
```

## Port Mapping

- Host port: `8000`
- Container port: `8000`

## Verification

- `docker ps` confirmed that `docker-task-09` was running.
- The browser accessed the FastAPI Swagger UI.
- The root endpoint returned HTTP `200 OK`.

## URLs

- API root: `http://localhost:8000/`
- Swagger UI: `http://localhost:8000/docs`
- About endpoint: `http://localhost:8000/about`