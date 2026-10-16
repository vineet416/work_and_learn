from fastapi import FastAPI

app = FastAPI(title="Task 12 - Requirements Demo")


@app.get("/")
def home():
    return {
        "message": "Dependencies installed from requirements.txt!",
        "task": 12
    }