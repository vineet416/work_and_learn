import os

import psycopg
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task 18 - FastAPI and PostgreSQL")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://super30user:demo-password-123@super30-postgres:5432/super30db",
)


@app.get("/")
def home():
    return {"message": "FastAPI is running inside Docker!", "task": 18}


@app.get("/db-check")
def check_database():
    try:
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT current_database(), current_user"
                )
                database, user = cursor.fetchone()

        return {
            "status": "connected",
            "database": database,
            "user": user,
        }

    except psycopg.Error as error:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to PostgreSQL. Check the database container and configuration.",
        ) from error