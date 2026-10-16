import os

import psycopg
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task 19 - Docker Compose Demo")

DATABASE_URL = os.getenv("DATABASE_URL", "")


@app.get("/")
def home():
    return {
        "message": "FastAPI and PostgreSQL are managed by Docker Compose",
        "task": 19,
    }


@app.get("/db-check")
def check_database():
    try:
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT current_database(), current_user")
                database, user = cursor.fetchone()

        return {
            "status": "connected",
            "database": database,
            "user": user,
        }

    except psycopg.Error as error:
        raise HTTPException(
            status_code=503,
            detail="PostgreSQL connection failed. Check the service and configuration.",
        ) from error