# Task 19: Docker Compose — FastAPI and PostgreSQL

## Objective

Run FastAPI and PostgreSQL as separate containers using Docker Compose.

## Project Structure

```text
task-19-docker-compose/
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

## Services

| Service | Purpose | Port |
|---|---|---|
| `api` | FastAPI application | Host `8019` → Container `8000` |
| `db` | PostgreSQL database | Container `5432` |

## Configuration

The `.env` file provides the database name, username, and password. It is excluded from Git.

The `.env.example` file documents the required variables without containing real credentials.

## Start the Application

Run from this directory:

```powershell
docker compose up --build -d
```

## Verify the Containers

```powershell
docker compose ps
docker compose logs api
docker compose logs db
```

The PostgreSQL service should become healthy, and the API should start successfully.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Verify the API is running |
| GET | `/db-check` | Verify the PostgreSQL connection |
| GET | `/docs` | Open Swagger UI |

Base URL: `http://localhost:8019`

## Verify the Database Connection

Open:

`http://localhost:8019/db-check`

Expected response:

```json
{
  "status": "connected",
  "database": "super30compose",
  "user": "super30user"
}
```

## Docker Compose Features Demonstrated

- Building the FastAPI image from a Dockerfile.
- Running FastAPI and PostgreSQL as separate services.
- Creating a shared Docker network.
- Using a named volume for PostgreSQL data.
- Configuring services through environment variables.
- Waiting for PostgreSQL's health check before starting the API.

## Stop the Services

```powershell
docker compose down
```

The named volume is preserved. To remove it as well, use `docker compose down -v` only when you intentionally want to delete the database data.