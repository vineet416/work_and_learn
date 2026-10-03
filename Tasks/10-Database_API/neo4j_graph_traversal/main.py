from database import driver, close_connection


def run_query(title, query):
    print("\n" + "-" * 60)
    print("# " + title)
    print("-" * 60)
    with driver.session() as session:
        result = session.run(query)
        for record in result:
            print(dict(record))


# QUERY 1
# Single-hop relationship
# Supplier -> Component
query_1 = """
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)
RETURN
    s.name AS supplier,
    c.name AS component
ORDER BY supplier
"""


# QUERY 2
# Single-hop relationship
# Component -> Product
query_2 = """
MATCH (c:Component)-[:USED_IN]->(p:Product)
RETURN
    c.name AS component,
    p.name AS product
ORDER BY component
"""


# QUERY 3
# Multi-hop relationship
# Supplier -> Component -> Product
query_3 = """
MATCH
    (s:Supplier)-[:SUPPLIES]->(c:Component)
    -[:USED_IN]->(p:Product)
RETURN DISTINCT
    s.name AS supplier,
    c.name AS component,
    p.name AS product
ORDER BY supplier, product
"""


# QUERY 4
# Multi-hop relationship
# Supplier -> Component -> Product -> Plant
query_4 = """
MATCH
    (s:Supplier)-[:SUPPLIES]->(c:Component)
    -[:USED_IN]->(p:Product)
    -[:MANUFACTURED_AT]->(plant:Plant)
RETURN DISTINCT
    s.name AS supplier,
    c.name AS component,
    p.name AS product,
    plant.name AS plant
ORDER BY supplier, product, plant
"""


# QUERY 5
# Filtering by properties
# Suppliers from India
query_5 = """
MATCH
    (s:Supplier)-[:LOCATED_IN]->
    (country:Country)
WHERE country.name = 'India'
RETURN
    s.name AS supplier,
    country.name AS country
ORDER BY supplier
"""


# QUERY 6
# Relationship direction
# Product <- USED_IN - Component
# Starting from Product and moving backwards
query_6 = """
MATCH
    (p:Product {name: 'Electric Car'})
    <-[:USED_IN]-(c:Component)
RETURN
    p.name AS product,
    c.name AS component
ORDER BY component
"""


# QUERY 7
# Aggregation / Counting
# Number of components supplied by each supplier
query_7 = """
MATCH
    (s:Supplier)-[:SUPPLIES]->(c:Component)
RETURN
    s.name AS supplier,
    COUNT(c) AS component_count
ORDER BY component_count DESC
"""


# QUERY 8
# Aggregation / Counting
# Number of suppliers connected to each product
query_8 = """
MATCH
    (s:Supplier)-[:SUPPLIES]->(c:Component)
    -[:USED_IN]->(p:Product)
RETURN
    p.name AS product,
    COUNT(DISTINCT s) AS supplier_count
ORDER BY supplier_count DESC
"""


# QUERY 9
# Path query
# Find a complete dependency path from a supplier to a plant
query_9 = """
MATCH path =
    (s:Supplier {name: 'TechParts India'})
    -[:SUPPLIES]->
    (c:Component)
    -[:USED_IN]->
    (p:Product)
    -[:MANUFACTURED_AT]->
    (plant:Plant)
RETURN
    [node IN nodes(path) |
        coalesce(node.name, node.id)
    ] AS dependency_path
"""


# QUERY 10
# Variable-length traversal
# Tier-2 supplier -> Supplier -> Component
# SUPPLIES*1..3 allows traversal through one or more SUPPLIES relationships.
query_10 = """
MATCH path =
    (s:Supplier {name: 'Global Components'})
    -[:SUPPLIES*1..3]->
    (c:Component)
RETURN
    [node IN nodes(path) |
        coalesce(node.name, node.id)
    ] AS supply_chain_path
"""


# QUERY 11
# Multi-hop traversal using Shipment
# Shipment -> Component -> Product -> Plant
query_11 = """
MATCH
    (shipment:Shipment)-[:CONTAINS]->(c:Component)
    -[:USED_IN]->(p:Product)
    -[:MANUFACTURED_AT]->(plant:Plant)
RETURN DISTINCT
    shipment.id AS shipment,
    c.name AS component,
    p.name AS product,
    plant.name AS plant
ORDER BY shipment
"""


# EXECUTE ALL QUERIES
def main():
    print("\n# GRAPH TRAVERSAL AND MULTI-HOP QUERIES")
    run_query("QUERY 1: Supplier -> Component", query_1)
    run_query("QUERY 2: Component -> Product", query_2)
    run_query("QUERY 3: Supplier -> Component -> Product", query_3)
    run_query("QUERY 4: Supplier -> Component -> Product -> Plant", query_4)
    run_query("QUERY 5: Suppliers from India", query_5)
    run_query("QUERY 6: Product -> Component using reverse direction", query_6)
    run_query("QUERY 7: Count components per supplier", query_7)
    run_query("QUERY 8: Count suppliers per product", query_8)
    run_query("QUERY 9: Dependency path", query_9)
    run_query("QUERY 10: Variable-length Tier-2 traversal", query_10)
    run_query("QUERY 11: Shipment -> Component -> Product -> Plant", query_11)
    close_connection()


if __name__ == "__main__":
    main()