import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()


class Neo4jConnection:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")

        self.database = os.getenv("NEO4J_DATABASE", "neo4j")

        if not uri or not username or not password:
            raise ValueError(
                "Neo4j configuration is missing. "
                "Check your .env file."
            )

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def verify_connection(self):
        """Check the database connection."""
        self.driver.verify_connectivity()
        print("Connected to Neo4j successfully.")

    def run_query(self, query, parameters=None):
        """Execute Cypher and return records as dictionaries."""
        with self.driver.session(
            database=self.database
        ) as session:
            result = session.run(query, parameters or {})
            return [record.data() for record in result]

    def close(self):
        """Close the database driver."""
        self.driver.close()