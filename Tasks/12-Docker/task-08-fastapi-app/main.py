from fastapi import FastAPI

app = FastAPI(title="Super30 Docker API")


@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI inside Docker!",
        "task": 8
    }


@app.get("/about")
def about():
    return {
        "application": "Super30 FastAPI",
        "description": "A simple API running inside Docker."
    }