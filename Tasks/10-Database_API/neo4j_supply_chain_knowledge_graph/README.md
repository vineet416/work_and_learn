# Supply Chain Knowledge Graph

This project demonstrates how a supply chain can be modeled and queried using a Neo4j graph database. It creates a sample network of suppliers, components, products, plants, shipments, and countries, then runs business queries to analyze supplier dependencies and product impact.

## Features

- Creates a supply-chain dataset in Neo4j
- Maps relationships such as:
  - Supplier -> Component
  - Component -> Product
  - Product -> Plant
  - Shipment -> Destination
- Answers common business questions such as:
  - Which products depend on a supplier?
  - Which plants are affected if a component is unavailable?
  - Which suppliers are connected to a product?
  - What is the dependency path from a tier-2 supplier?

## Project Files

- `main.py` - creates the graph and runs the example queries
- `database.py` - establishes the Neo4j database connection
- `requirements.txt` - Python dependencies
- `.env.example` - sample environment variables

## Setup

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file from the example and add your Neo4j credentials:
   ```bash
   copy .env.example .env
   ```

   Then update the values:
   ```env
   NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=your_password
   ```

## Run the Project

```bash
python main.py
```

This will create the sample dataset and print the query results for the supply-chain analysis.

## Notes

- Make sure your Neo4j database is running and accessible.
- If you are using Neo4j Aura or a remote instance, use the correct URI and credentials in `.env`.
