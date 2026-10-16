import os

import psycopg
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task 20 - Three-Service Application")

DATABASE_URL = os.getenv("DATABASE_URL", "")


@app.get("/")
def home():
    return {
        "message": "FastAPI backend is running",
        "task": 20,
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
            detail="PostgreSQL connection failed",
        ) from error