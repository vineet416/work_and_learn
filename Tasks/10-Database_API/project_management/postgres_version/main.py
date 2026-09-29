from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from database import SessionLocal
from models import ProjectCreate, TaskCreate, TaskAssign, TaskStatusUpdate


app = FastAPI()


# 1. CREATE PROJECT
@app.post("/projects")
def create_project(project: ProjectCreate):
    db = SessionLocal()
    try:
        result = db.execute(
            text("""
                INSERT INTO projects
                (
                    name,
                    description
                )
                VALUES
                (
                    :name,
                    :description
                )
                RETURNING id, name, description
            """),
            {
                "name": project.name,
                "description": project.description
            }
        )
        new_project = result.fetchone()
        db.commit()
        return {
            "id": new_project.id,
            "name": new_project.name,
            "description": new_project.description
        }
    finally:
        db.close()


# 2. CREATE TASK
@app.post("/tasks")
def create_task(task: TaskCreate):
    db = SessionLocal()
    try:
        # Check project
        project = db.execute(
            text("""
                SELECT id
                FROM projects
                WHERE id = :project_id
            """),
            {
                "project_id": task.project_id
            }
        ).fetchone()
        if not project:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )
        result = db.execute(
            text("""
                INSERT INTO tasks
                (
                    project_id,
                    title,
                    description,
                    status
                )
                VALUES
                (
                    :project_id,
                    :title,
                    :description,
                    'pending'
                )
                RETURNING
                    id,
                    project_id,
                    title,
                    description,
                    assigned_to,
                    status
            """),
            {
                "project_id": task.project_id,
                "title": task.title,
                "description": task.description
            }
        )
        new_task = result.fetchone()
        db.commit()
        return {
            "id": new_task.id,
            "project_id": new_task.project_id,
            "title": new_task.title,
            "description": new_task.description,
            "assigned_to": new_task.assigned_to,
            "status": new_task.status
        }
    finally:
        db.close()


# 3. ASSIGN TASK
@app.put("/tasks/{task_id}/assign")
def assign_task(task_id: int, assignment: TaskAssign):
    db = SessionLocal()
    try:
        # Check task
        task = db.execute(
            text("""
                SELECT id
                FROM tasks
                WHERE id = :task_id
            """),
            {
                "task_id": task_id
            }
        ).fetchone()
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        db.execute(
            text("""
                UPDATE tasks
                SET assigned_to = :assigned_to
                WHERE id = :task_id
            """),
            {
                "assigned_to": assignment.assigned_to,
                "task_id": task_id
            }
        )
        db.commit()
        return {
            "message": "Task assigned successfully",
            "task_id": task_id,
            "assigned_to": assignment.assigned_to
        }
    finally:
        db.close()


# 4. UPDATE TASK STATUS
@app.put("/tasks/{task_id}/status")
def update_task_status(task_id: int, status_data: TaskStatusUpdate):
    db = SessionLocal()
    try:
        task = db.execute(
            text("""
                SELECT id
                FROM tasks
                WHERE id = :task_id
            """),
            {
                "task_id": task_id
            }
        ).fetchone()
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        db.execute(
            text("""
                UPDATE tasks
                SET status = :status
                WHERE id = :task_id
            """),
            {
                "status": status_data.status,
                "task_id": task_id
            }
        )
        db.commit()
        return {
            "message": "Task status updated successfully",
            "task_id": task_id,
            "status": status_data.status
        }
    finally:
        db.close()


# 5. RETRIEVE TASKS
@app.get("/tasks")
def retrieve_tasks():
    db = SessionLocal()
    try:
        result = db.execute(
            text("""
                SELECT
                    t.id,
                    t.project_id,
                    p.name AS project_name,
                    t.title,
                    t.description,
                    t.assigned_to,
                    t.status
                FROM tasks t
                JOIN projects p
                    ON t.project_id = p.id
                ORDER BY t.id
            """)
        )
        tasks = result.fetchall()
        return [
            {
                "id": task.id,
                "project_id": task.project_id,
                "project_name": task.project_name,
                "title": task.title,
                "description": task.description,
                "assigned_to": task.assigned_to,
                "status": task.status
            }
            for task in tasks
        ]
    finally:
        db.close()


# 6. FILTER TASKS
@app.get("/tasks/filter")
def filter_tasks(status: str | None = None, project_id: int | None = None):
    db = SessionLocal()
    try:
        query = """
            SELECT
                t.id,
                t.project_id,
                p.name AS project_name,
                t.title,
                t.description,
                t.assigned_to,
                t.status
            FROM tasks t
            JOIN projects p
                ON t.project_id = p.id
            WHERE 1 = 1
        """
        parameters = {}
        if status is not None:
            query += " AND t.status = :status"
            parameters["status"] = status
        if project_id is not None:
            query += " AND t.project_id = :project_id"
            parameters["project_id"] = project_id
        query += " ORDER BY t.id"
        result = db.execute(text(query), parameters)
        tasks = result.fetchall()
        return [
            {
                "id": task.id,
                "project_id": task.project_id,
                "project_name": task.project_name,
                "title": task.title,
                "description": task.description,
                "assigned_to": task.assigned_to,
                "status": task.status
            }
            for task in tasks
        ]
    finally:
        db.close()


# 7. DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.execute(
            text("""
                SELECT id
                FROM tasks
                WHERE id = :task_id
            """),
            {
                "task_id": task_id
            }
        ).fetchone()
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        db.execute(
            text("""
                DELETE FROM tasks
                WHERE id = :task_id
            """),
            {
                "task_id": task_id
            }
        )
        db.commit()
        return {
            "message": "Task deleted successfully",
            "task_id": task_id
        }
    finally:
        db.close()