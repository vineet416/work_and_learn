
# Student Management REST API

A Student Management REST API built using FastAPI.
This project performs CRUD operations using in-memory Python storage.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
uvicorn main:app --reload
```

### 3. Open API Documentation

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| POST | `/students` | Create a student |
| GET | `/students` | List all students |
| GET | `/students/{id}` | Get student by ID |
| PUT | `/students/{id}` | Replace student |
| PATCH | `/students/{id}` | Partially update student |
| DELETE | `/students/{id}` | Delete student |

## Features

- CRUD operations
- Request validation using Pydantic
- Path parameters
- Query parameters
- HTTP status codes
- Error handling for invalid IDs
- In-memory data storage

## Storage

Student data is stored in a Python dict.
Data will be lost when the application restarts.

## Author

Vineet Patel