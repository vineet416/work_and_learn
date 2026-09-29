# Project Management API

FastAPI project-management APIs with two database implementations:

- `mongodb_version`: MongoDB with PyMongo
- `postgres_version`: PostgreSQL with SQLAlchemy

Both versions provide the same project and task endpoints.

## Setup

Create a virtual environment and install the requirements for the version you want to run:

```powershell
cd mongodb_version
pip install -r requirements.txt
```

or:

```powershell
cd postgres_version
pip install -r requirements.txt
```

Create a `.env` file in the selected version directory:

```env
# mongodb_version
MONGO_DB_URL=your-mongodb-connection-string

# postgres_version
DATABASE_URL=your-postgresql-connection-string
```

For PostgreSQL, run `schema.sql` before starting the API.

## Run

From the selected version directory:

```powershell
uvicorn main:app --reload
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/projects` | List projects |
| POST | `/projects` | Create a project |
| GET | `/projects/{project_id}` | Get one project |
| GET | `/projects/{project_id}/tasks` | List tasks for a project |
| POST | `/tasks` | Create a task |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/filter?status=pending&project_id=1` | Filter tasks |
| PUT | `/tasks/{task_id}/assign` | Assign a task |
| PUT | `/tasks/{task_id}/status` | Update task status |
| DELETE | `/tasks/{task_id}` | Delete a task |

Request bodies are validated with Pydantic. The API returns `404` when a requested project or task does not exist.
