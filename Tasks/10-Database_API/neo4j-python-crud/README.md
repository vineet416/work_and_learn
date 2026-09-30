# Neo4j Python CRUD API

A simple FastAPI project that connects to a Neo4j database and manages students, courses, and their relationships.

## Features
- Create a course
- Create a student
- Create a relationship between a student and a course
- Read all students
- Search students by city
- Update a student's city
- Delete a student relationship
- Delete a student

## Setup

1. Create a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Neo4j connection details:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

4. Start the API:

```bash
uvicorn main:app --reload
```

The app will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Courses
- `POST /courses/` - Create a course

Request body:
```json
{
  "name": "Python"
}
```

### Students
- `POST /students/` - Create a student
- `GET /students/` - Get all students
- `GET /students/search/{city}` - Search students by city
- `PUT /students/update_city/` - Update a student's city
- `DELETE /students/{name}` - Delete a student

Request body for creating a student:
```json
{
  "name": "Vineet",
  "age": 22,
  "city": "Mumbai"
}
```

Request body for updating city:
```json
{
  "name": "Vineet",
  "new_city": "Palghar"
}
```

### Relationships
- `POST /relationships/` - Create a student-course relationship
- `DELETE /relationships/` - Delete a student-course relationship

Request body:
```json
{
  "student_name": "Vineet",
  "course_name": "Python"
}
```

## Notes
- Make sure your Neo4j database is running before starting the app.
- You can view the interactive API docs at:

```text
http://127.0.0.1:8000/docs
```
