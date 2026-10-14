from database import Neo4jConnection
from graph_setup import (
    create_constraints,
    seed_data,
    verify_graph,
)
from crud import demonstrate_crud
from queries import run_demo_queries


def main():
    db = Neo4jConnection()

    try:
        db.verify_connection()

        create_constraints(db)
        seed_data(db)
        verify_graph(db)

        demonstrate_crud(db)
        run_demo_queries(db)

        print("\nCareerGraph execution completed.")

    except Exception as error:
        print("\nAn error occurred:", error)
        raise

    finally:
        db.close()
        print("Neo4j connection closed.")


if __name__ == "__main__":
    main()