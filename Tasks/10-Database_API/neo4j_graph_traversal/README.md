# Graph Traversal and Multi-Hop Queries

This project demonstrates graph traversal and multi-hop Cypher queries using the Supply Chain Knowledge Graph.

## Technologies

- Python
- Neo4j
- Cypher
- Neo4j Python Driver

## Graph Structure

The graph represents a supply chain containing:

- Supplier
- Component
- Product
- Plant
- Shipment
- Country

Main relationships:

- Supplier -> SUPPLIES -> Component
- Component -> USED_IN -> Product
- Product -> MANUFACTURED_AT -> Plant
- Supplier -> LOCATED_IN -> Country
- Shipment -> CONTAINS -> Component
- Shipment -> DESTINED_FOR -> Plant

A Tier-2 supplier relationship is also included.

## Project Structure

```text
neo4j_graph_traversal/
│
├── main.py
├── database.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md