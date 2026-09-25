# Course Management API

A simple FastAPI project for managing course records.

## Overview
This API allows you to create, view, update, replace, and delete course information.

## Run the project

```bash
uvicorn main:app --reload
```

Then open: http://127.0.0.1:8000

## API Endpoints

### Root
- GET /
  - Returns a welcome message

### Course operations
- POST /create_course
  - Create a new course
- GET /courses/
  - Get all courses
- GET /courses
  - Get courses with optional filters:
    - category
    - min_price
    - max_price
    - active
- PUT /replace_courses/{course_id}
  - Replace a course by ID
- PATCH /update_courses/{course_id}
  - Partially update a course
- DELETE /delete_courses/{course_id}
  - Delete a course by ID

## Example course payload

```json
{
  "title": "Python Programming",
  "description": "Learn Python from basics to advanced concepts.",
  "price": 999,
  "duration": "8 weeks",
  "instructor": "Vineet Patel",
  "category": "python",
  "rating": 4.5,
  "active": true
}
```

## Notes
- The app uses in-memory data storage.
- Data resets when the server restarts.
