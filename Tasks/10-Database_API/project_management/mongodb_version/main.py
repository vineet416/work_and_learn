from fastapi import FastAPI, HTTPException
from database import projects_collection, tasks_collection
from models import ProjectCreate, TaskCreate, TaskAssign, TaskStatusUpdate


app = FastAPI()


# 1. CREATE PROJECT
@app.post("/projects")
def create_project(project: ProjectCreate):
    project_id = projects_collection.count_documents({}) + 1
    project_data = {"_id": project_id, "name": project.name, "description": project.description}
    result = projects_collection.insert_one(project_data)
    return {
        "id": str(result.inserted_id),
        "name": project.name,
        "description": project.description
    }


# 2. CREATE TASK
@app.post("/tasks")
def create_task(task: TaskCreate):
    task_id = tasks_collection.count_documents({}) + 1
    project = projects_collection.find_one(
        {
            "_id": task.project_id
        }
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    task_data = {
        "_id": task_id,
        "project_id": task.project_id,
        "title": task.title,
        "description": task.description,
        "assigned_to": None,
        "status": "pending"
    }
    result = tasks_collection.insert_one(task_data)
    return {
        "id": str(result.inserted_id),
        "project_id": task.project_id,
        "title": task.title,
        "description": task.description,
        "assigned_to": None,
        "status": "pending"
    }


# 3. ASSIGN TASK
@app.put("/tasks/{task_id}/assign")
def assign_task(task_id: int,assignment: TaskAssign):
    result = tasks_collection.update_one(
        {
            "_id": task_id
        },
        {
            "$set": {
                "assigned_to": assignment.assigned_to
            }
        }
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
        "message": "Task assigned successfully",
        "task_id": task_id,
        "assigned_to": assignment.assigned_to
    }


# 4. UPDATE TASK STATUS
@app.put("/tasks/{task_id}/status")
def update_task_status(task_id: int, status_data: TaskStatusUpdate):
    result = tasks_collection.update_one(
        {
            "_id": task_id
        },
        {
            "$set": {
                "status": status_data.status
            }
        }
    )
    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {
        "message": "Task status updated successfully",
        "task_id": task_id,
        "status": status_data.status
    }


# 5. RETRIEVE TASKS
@app.get("/tasks")
def retrieve_tasks():
    tasks = tasks_collection.find()
    result = []
    for task in tasks:
        result.append(
            {
                "id": str(task["_id"]),
                "project_id": task["project_id"],
                "title": task["title"],
                "description": task["description"],
                "assigned_to": task["assigned_to"],
                "status": task["status"]
            }
        )
    return result


# 6. FILTER TASKS
@app.get("/tasks/filter")
def filter_tasks(status: str | None = None, project_id: int | None = None):
    filter_query = {}
    if status is not None:
        filter_query["status"] = status
    if project_id is not None:
        filter_query["project_id"] = project_id
    tasks = tasks_collection.find(filter_query)
    result = []
    for task in tasks:
        result.append(
            {
                "id": str(task["_id"]),
                "project_id": task["project_id"],
                "title": task["title"],
                "description": task["description"],
                "assigned_to": task["assigned_to"],
                "status": task["status"]
            }
        )
    return result


# 7. DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    result = tasks_collection.delete_one(
        {
            "_id": task_id
        }
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully", "task_id": task_id}