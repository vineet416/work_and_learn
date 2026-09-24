# Student Course API

Simple FastAPI CRUD API for managing students, courses, and enrollments with Neon PostgreSQL.

## Setup

1. Create a Neon PostgreSQL database and copy full content of [`database_schema.txt`](database_schema.txt) and paste it into the SQL editor of your Neon database to create the necessary tables and insert sample data.
2. Create and activate a virtual environment, then install dependencies:

	```bash
	pip install -r requirements.txt
	```

3. Copy `.env.example` to `.env` and set the database connection:

	```env
	DATABASE_URL=postgresql://username:password@host/database_name
	```

4. Start the API:

	```bash
	uvicorn main:app --reload
	```

API URL: `http://127.0.0.1:8000`  
Interactive docs: `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/students` | List students |
| GET | `/students/{student_id}` | Get a student |
| POST | `/create_student` | Create a student |
| PATCH | `/update_student/{student_id}` | Update a student |
| DELETE | `/delete_student/{student_id}` | Delete a student |
| GET | `/courses` | List courses |
| GET | `/courses/{course_id}` | Get a course |
| POST | `/create_course` | Create a course |
| PATCH | `/update_course/{course_id}` | Update a course |
| DELETE | `/delete_course/{course_id}` | Delete a course |
| GET | `/enrollments` | List enrollments |
| GET | `/enrollments/{enrollment_id}` | Get an enrollment |
| POST | `/enroll_student` | Enroll a student in a course |
| PATCH | `/update_enrollment/{enrollment_id}` | Update an enrollment |
| DELETE | `/delete_enrollment/{enrollment_id}` | Delete an enrollment |

## Request Examples

```json
// POST /create_student
{"name": "Asha Patel", "email": "asha@example.com", "age": 21}
```

```json
// POST /enroll_student
{"student_id": 1, "course_id": 1, "status": "active"}
```
