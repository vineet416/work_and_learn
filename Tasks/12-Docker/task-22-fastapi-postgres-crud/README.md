# Task 22 — FastAPI + PostgreSQL CRUD with Docker Compose

## Overview

A Student Management REST API built using FastAPI and PostgreSQL. Docker Compose runs the API and database in separate containers, connected through a custom network.

A named Docker volume persists student records across container recreation.

## Technologies

- Python
- FastAPI
- PostgreSQL
- psycopg
- Docker
- Docker Compose

## Project Structure

```text
task-22-fastapi-postgres-crud/
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

## Configuration

Create `.env` from `.env.example` and configure the database name, user, and password. Do not commit `.env` to GitHub.

## Run the Application

Run from this project directory:

```powershell
docker compose up --build -d
```

Check the containers:

```powershell
docker compose ps
docker compose logs api
docker compose logs db
```

## API Documentation

Open http://localhost:8022/docs

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Check API and database connectivity |
| POST | `/students` | Create a student |
| GET | `/students` | List students |
| GET | `/students/{student_id}` | Get one student |
| PUT | `/students/{student_id}` | Update provided student fields |
| DELETE | `/students/{student_id}` | Delete a student |

Search students using `/students?search=python`.

## Example Student

```json
{
  "name": "Aarav Patel",
  "email": "aarav@example.com",
  "course": "Python"
}
```

Send this body to `POST /students`.

## Verify Persistence

1. Create a student through Swagger UI.
2. Stop and remove the containers without removing the volume:

```powershell
docker compose down
docker compose up --build -d
```

3. Open `/students` again and verify that the record still exists.

The named volume `student-data` stores PostgreSQL data.

**Warning:** `docker compose down -v` removes the named volume and deletes its stored database data.

## Stop the Application

```powershell
docker compose down
```

## What I Learned

- Implementing CRUD operations with FastAPI and PostgreSQL.
- Connecting containers using Docker Compose networking.
- Using environment variables for database configuration.
- Persisting database records with named Docker volumes.
- Testing API endpoints through Swagger UI.