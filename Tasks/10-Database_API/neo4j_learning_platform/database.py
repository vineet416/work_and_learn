import os
from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

try:
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
    driver.verify_connectivity()
except Exception as e:
    print(f"Error connecting to Neo4j: {e}")

def close_connection():
    driver.close()