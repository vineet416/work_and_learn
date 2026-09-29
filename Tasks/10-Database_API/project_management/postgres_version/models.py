from pydantic import BaseModel, Field


# PROJECT
class ProjectCreate(BaseModel):
    name: str
    description: str


# TASK
class TaskCreate(BaseModel):
    project_id: int
    title: str
    description: str


# ASSIGN TASK
class TaskAssign(BaseModel):
    assigned_to: str


# UPDATE STATUS
class TaskStatusUpdate(BaseModel):
    status: str


# FILTER TASKS
class TaskFilter(BaseModel):
    status: str | None = None
    project_id: int | None = None