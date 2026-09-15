# Super30 FastAPI GET API Task

## Project Objective

This project is a beginner-level FastAPI application created as part of the Super30 assignment.

The objective is to understand:

* FastAPI application creation
* GET API endpoints
* Static routes
* Dynamic URL path parameters
* Type hints
* Returning Python dictionaries as JSON
* Running FastAPI using Uvicorn
* Testing APIs using Swagger UI
* FastAPI automatic API documentation

## Technologies Used

* Python
* FastAPI
* Uvicorn

## Project Structure

```text
super30-fastapi-get-api-task/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and open the project folder.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI application using:

```bash
uvicorn main:app --reload
```

The application will normally be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Available GET APIs

| Method | Endpoint                  | Description                   |
| ------ | ------------------------- | ----------------------------- |
| GET    | `/`                       | Home API                      |
| GET    | `/student`                | Student information           |
| GET    | `/course`                 | Course information            |
| GET    | `/skills`                 | Technical skills              |
| GET    | `/add/{num1}/{num2}`      | Add two numbers               |
| GET    | `/multiply/{num1}/{num2}` | Multiply two numbers          |
| GET    | `/square/{number}`        | Calculate square              |
| GET    | `/check/{number}`         | Check even or odd             |
| GET    | `/age/{age}`              | Classify age                  |
| GET    | `/table/{number}`         | Generate multiplication table |
| GET    | `/profile/{name}/{age}`   | Display profile               |
| GET    | `/number/{number}`        | Analyze a number              |

## Example URLs

```text
http://127.0.0.1:8000/

http://127.0.0.1:8000/student

http://127.0.0.1:8000/course

http://127.0.0.1:8000/skills

http://127.0.0.1:8000/add/10/20

http://127.0.0.1:8000/multiply/5/8

http://127.0.0.1:8000/square/9

http://127.0.0.1:8000/check/17

http://127.0.0.1:8000/age/25

http://127.0.0.1:8000/table/7

http://127.0.0.1:8000/profile/Vineet/25

http://127.0.0.1:8000/number/25
```

## Dynamic API Example

The addition API accepts dynamic numbers.

For example:

```text
/add/10/20
```

returns:

```json
{
    "result": 30
}
```

While:

```text
/add/50/25
```

returns:

```json
{
    "result": 75
}
```

## Author

Vineet Patel