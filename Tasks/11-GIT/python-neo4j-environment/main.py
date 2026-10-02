import os
from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()


URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")


driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


try:
    driver.verify_connectivity()
    print("Successfully connected to Neo4j Aura!")
except Exception as e:
    print("Neo4j connection failed.")
    print(e)
finally:
    driver.close()