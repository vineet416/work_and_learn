# Neon E-commerce API

A simple FastAPI e-commerce backend using PostgreSQL on Neon.

## Setup

1. Create a Neon PostgreSQL database.
2. Run [`schema.sql`](schema.sql) in the Neon SQL editor.
3. Run [`sample_data.sql`](sample_data.sql) to add sample users and products.
4. Create a `.env` file in this folder:

```env
DATABASE_URL=your_neon_database_url
```

5. Install the dependencies and start the API:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will run at `http://127.0.0.1:8000`.

Interactive API documentation is available at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/users` | Create a user |
| `GET` | `/products` | View all products |
| `POST` | `/orders` | Place an order |
| `GET` | `/users/{user_id}/orders` | View a user's orders |
| `PUT` | `/products/{product_id}/inventory` | Update product inventory |
| `PUT` | `/orders/{order_id}/cancel` | Cancel an order |

## Example Request Bodies

### Create User

```json
{
	"name": "Jane Doe",
	"email": "jane@example.com"
}
```

### Place Order

```json
{
	"user_id": 1,
	"items": [
		{
			"product_id": 1,
			"quantity": 2
		}
	]
}
```

### Update Inventory

```json
{
	"inventory": 25
}
```

## Main Files

- [`main.py`](main.py) - FastAPI routes
- [`database.py`](database.py) - PostgreSQL connection
- [`models.py`](models.py) - Request and response models
- [`schema.sql`](schema.sql) - Database tables
- [`sample_data.sql`](sample_data.sql) - Sample users and products
