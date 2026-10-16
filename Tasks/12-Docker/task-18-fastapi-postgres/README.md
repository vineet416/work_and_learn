# Task 18: Connect FastAPI to PostgreSQL Using Docker

## Objective

Run FastAPI and PostgreSQL in separate Docker containers and connect them using a custom Docker network.

## Architecture

- FastAPI container: `super30-fastapi`
- PostgreSQL container: `super30-postgres`
- Docker network: `task-18-network`
- Host API port: `8018`
- PostgreSQL port inside the network: `5432`

## Build the FastAPI Image

```powershell
docker build -t super30-task-18 .
```

## Connect PostgreSQL to the Network

```powershell
docker network create task-18-network
docker network connect task-18-network super30-postgres
```

If the network already exists, reuse it instead of creating it again.

## Run FastAPI

```powershell
docker run -d `
  --name super30-fastapi `
  --network task-18-network `
  -e DATABASE_URL="postgresql://super30user:demo-password-123@super30-postgres:5432/super30db" `
  -p 8018:8000 `
  super30-task-18
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check FastAPI |
| GET | `/db-check` | Verify the PostgreSQL connection |

## Verification

```powershell
docker ps
docker logs super30-fastapi
docker network inspect task-18-network
```

Open `http://localhost:8018/db-check` and verify that the database connection succeeds.

## Key Concepts

- Each service runs in its own container.
- Containers on the same user-defined network can communicate using container names.
- `DATABASE_URL` configures the database connection.
- The host port mapping makes the API accessible from the browser.

## Security Note

The credentials in this exercise are for local demonstration only. Do not commit real passwords or credentials to Git.