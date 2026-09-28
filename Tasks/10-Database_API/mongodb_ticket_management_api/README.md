# MongoDB Ticket Management API

A simple ticket management API built with FastAPI and MongoDB.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in this project directory:

```env
MONGO_DB_URL=your_mongodb_connection_string
```

Start the API:

```bash
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

Interactive documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/tickets` | Create a ticket |
| `GET` | `/tickets` | Get all tickets |
| `GET` | `/tickets/{ticket_id}` | Get a ticket by ID |
| `GET` | `/tickets/filter?status=Open` | Filter tickets by status |
| `GET` | `/tickets/filter?status=Open&priority=High` | Filter by status and priority |
| `PATCH` | `/tickets/{ticket_id}` | Update ticket details |
| `PATCH` | `/tickets/{ticket_id}/status` | Update ticket status |
| `POST` | `/tickets/{ticket_id}/comments` | Add a comment |
| `DELETE` | `/tickets/{ticket_id}` | Delete a ticket |

Ticket IDs are integers. Request and response schemas are available in the Swagger UI.
