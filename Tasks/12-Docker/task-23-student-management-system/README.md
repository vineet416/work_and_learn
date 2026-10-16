# Task 23 — Student Management System with Docker

## Overview

A full-stack Student Management System built with HTML, CSS, JavaScript, FastAPI, and PostgreSQL.

The application runs as three separate Docker containers managed by Docker Compose.

## Architecture

```text
Browser
   |
   v
Frontend: Nginx + HTML/CSS/JavaScript
   |
   | /api/ requests
   v
Backend: FastAPI
   |
   v
Database: PostgreSQL
```

All services communicate through a custom Docker network. PostgreSQL data is stored in a named volume.

## Technologies Used

- Docker and Docker Compose
- Python and FastAPI
- PostgreSQL and psycopg
- HTML, CSS, and JavaScript
- Nginx
- Environment variables

## Project Structure

```text
task-23-student-management-system/
├── frontend/
│   ├── index.html
│   ├── nginx.conf
│   └── Dockerfile
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

Create a local `.env` file using `.env.example` as a template.

Configure the PostgreSQL database name, username, and password. Do not commit `.env` to GitHub.

## Run the Application

Run these commands from this project directory:

```powershell
docker compose up --build
```

The first build downloads the required base images and builds the frontend and backend images.

To run in detached mode:

```powershell
docker compose up --build -d
```

## Access the Application

- Frontend: http://localhost:8023/
- API documentation: available internally at `/docs` on the FastAPI service. The frontend exposes the application through Nginx.
- Health endpoint through the frontend: http://localhost:8023/api/health

## Student Management Features

- Add students.
- View all students.
- View a student by ID.
- Update student details.
- Delete students.
- Search by student name, email, or course.
- Check API and database health.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Check database connectivity |
| POST | `/students` | Create a student |
| GET | `/students` | List students |
| GET | `/students?search=Python` | Search students |
| GET | `/students/{student_id}` | Retrieve a student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

The endpoints are available through the frontend proxy by prefixing the paths with `/api`.

## Example Student

```json
{
  "name": "Aarav Patel",
  "email": "aarav@example.com",
  "course": "Python"
}
```

Submit this JSON body to `POST /api/students`.

## Verify the Services

Check the running containers:

```powershell
docker compose ps
```

View application logs:

```powershell
docker compose logs frontend
docker compose logs api
docker compose logs db
```

Check the API and database:

```powershell
Invoke-RestMethod http://localhost:8023/api/health
```

Expected response:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

## Verify Persistent Storage

1. Add a student through the frontend.
2. Stop and remove the containers:

```powershell
docker compose down
```

3. Rebuild and start them again:

```powershell
docker compose up --build -d
```

4. Reopen the frontend and verify that the student record still exists.

The named volume `student-data` retains the database files.

**Warning:** `docker compose down -v` deletes the named volume and the stored database data.

## Stop the Application

```powershell
docker compose down
```

## What I Learned

- Containerizing a frontend and backend separately.
- Connecting FastAPI to PostgreSQL.
- Using Docker Compose to manage multiple services.
- Configuring a custom Docker network.
- Managing environment variables.
- Persisting PostgreSQL data with a named volume.
- Implementing REST API CRUD operations.
- Using Nginx as a reverse proxy.
- Checking service health and application logs.