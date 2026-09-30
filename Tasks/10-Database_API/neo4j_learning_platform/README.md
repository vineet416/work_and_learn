# Neo4j Learning Platform

This project is a simple Python-based example for learning Neo4j graph database operations. It demonstrates how to connect to a Neo4j database, create nodes and relationships, read graph data, update records, and delete nodes or relationships.

## Project Structure

- `database.py` – Handles the Neo4j driver connection and environment variables.
- `main.py` – Contains the graph creation, reading, updating, and deletion examples.
- `.env.example` – Example environment file for Neo4j credentials.
- `requirements.txt` – Python dependencies for the project.

## Features

- Connect to Neo4j using environment variables
- Create student, course, skill, project, mentor, and company nodes
- Create relationships such as ENROLLED_IN, TEACHES, BUILT, and INTERESTED_IN
- Query and display graph data
- Update and delete records to practice CRUD operations on a graph database

## Requirements

- Python 3.x
- Neo4j database instance
- Internet access or local Neo4j setup

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example`:

   ```env
   NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=your_password
   ```

4. Run the project:

   ```bash
   python main.py
   ```

## Notes

This project is intended for learning and practicing graph database concepts in Python. You can expand it by adding additional queries, more nodes, or a small Flask/FastAPI application on top of the Neo4j data.

## License

This project is for educational purposes.
