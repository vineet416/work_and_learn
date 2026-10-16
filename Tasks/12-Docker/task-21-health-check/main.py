from fastapi import FastAPI

app = FastAPI(title="Task 21 - Health Check")


@app.get("/")
def home():
    return {
        "message": "FastAPI health-check application",
        "task": 21,
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }