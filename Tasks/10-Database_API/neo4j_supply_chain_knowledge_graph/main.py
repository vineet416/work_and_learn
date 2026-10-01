from database import driver, close_connection


# CREATE DATASET
def create_dataset():
    query = """
    CREATE
        // Suppliers
        (s1:Supplier {
            name: 'TechParts India'
        }),
        (s2:Supplier {
            name: 'Global Components'
        }),
        (s3:Supplier {
            name: 'AutoParts Japan'
        }),
        (s4:Supplier {
            name: 'ElectroSupply Germany'
        }),

        // Components
        (c1:Component {
            name: 'Battery Cell'
        }),
        (c2:Component {
            name: 'Microcontroller'
        }),
        (c3:Component {
            name: 'Brake Sensor'
        }),
        (c4:Component {
            name: 'Display Module'
        }),

        // Products
        (p1:Product {
            name: 'Electric Car'
        }),
        (p2:Product {
            name: 'Smart Dashboard'
        }),

        // Plants
        (pl1:Plant {
            name: 'Pune Plant'
        }),
        (pl2:Plant {
            name: 'Bangalore Plant'
        }),

        // Shipments
        (sh1:Shipment {
            id: 'Shipment-101'
        }),
        (sh2:Shipment {
            id: 'Shipment-102'
        }),
        (sh3:Shipment {
            id: 'Shipment-103'
        }),
        (sh4:Shipment {
            id: 'Shipment-104'
        }),

        // Countries
        (co1:Country {
            name: 'India'
        }),
        (co2:Country {
            name: 'USA'
        }),
        (co3:Country {
            name: 'Japan'
        }),
        (co4:Country {
            name: 'Germany'
        })

    CREATE
        // Supplier -> Component
        (s1)-[:SUPPLIES]->(c1),
        (s1)-[:SUPPLIES]->(c2),
        (s2)-[:SUPPLIES]->(c1),
        (s2)-[:SUPPLIES]->(c4),
        (s3)-[:SUPPLIES]->(c3),
        (s4)-[:SUPPLIES]->(c2),
        (s4)-[:SUPPLIES]->(c4),

        // Component -> Product
        (c1)-[:USED_IN]->(p1),
        (c2)-[:USED_IN]->(p1),
        (c3)-[:USED_IN]->(p1),
        (c4)-[:USED_IN]->(p2),
        (c2)-[:USED_IN]->(p2),

        // Product -> Plant
        (p1)-[:MANUFACTURED_AT]->(pl1),
        (p1)-[:MANUFACTURED_AT]->(pl2),
        (p2)-[:MANUFACTURED_AT]->(pl2),

        // Supplier -> Country
        (s1)-[:LOCATED_IN]->(co1),
        (s2)-[:LOCATED_IN]->(co2),
        (s3)-[:LOCATED_IN]->(co3),
        (s4)-[:LOCATED_IN]->(co4),

        // Shipment -> Component
        (sh1)-[:CONTAINS]->(c1),
        (sh2)-[:CONTAINS]->(c2),
        (sh3)-[:CONTAINS]->(c3),
        (sh4)-[:CONTAINS]->(c4),

        // Shipment -> Plant
        (sh1)-[:DESTINED_FOR]->(pl1),
        (sh2)-[:DESTINED_FOR]->(pl2),
        (sh3)-[:DESTINED_FOR]->(pl1),
        (sh4)-[:DESTINED_FOR]->(pl2),

        // Tier-2 Supplier Relationship
        (s2)-[:SUPPLIES]->(s1)
    """
    with driver.session() as session:
        session.run(query)
    print("Supply-chain graph created successfully.")


# QUERY 1
# Which products depend on Supplier A?
def products_depending_on_supplier():
    query = """
    MATCH
        (s:Supplier {name: 'TechParts India'})
        -[:SUPPLIES]->
        (c:Component)
        -[:USED_IN]->
        (p:Product)
    RETURN DISTINCT
        s.name AS supplier,
        c.name AS component,
        p.name AS product
    ORDER BY product
    """
    with driver.session() as session:
        result = session.run(query)
        print("\n# PRODUCTS DEPENDING ON SUPPLIER A")
        for record in result:
            print(
                f"Supplier: {record['supplier']} | "
                f"Component: {record['component']} | "
                f"Product: {record['product']}"
            )


# QUERY 2
# Which plants could be affected if Component X becomes unavailable?
def plants_affected_by_component():
    query = """
    MATCH
        (c:Component {name: 'Battery Cell'})
        -[:USED_IN]->
        (p:Product)
        -[:MANUFACTURED_AT]->
        (plant:Plant)
    RETURN DISTINCT
        c.name AS component,
        p.name AS product,
        plant.name AS plant
    ORDER BY plant
    """
    with driver.session() as session:
        result = session.run(query)
        print("\n# PLANTS AFFECTED BY BATTERY CELL")
        for record in result:
            print(
                f"Component: {record['component']} | "
                f"Product: {record['product']} | "
                f"Plant: {record['plant']}"
            )


# QUERY 3
# Find all suppliers connected to Product Y
def suppliers_connected_to_product():
    query = """
    MATCH
        (s:Supplier)
        -[:SUPPLIES]->
        (c:Component)
        -[:USED_IN]->
        (p:Product {name: 'Electric Car'})
    RETURN DISTINCT
        s.name AS supplier,
        c.name AS component,
        p.name AS product
    ORDER BY supplier
    """
    with driver.session() as session:
        result = session.run(query)
        print("\n# SUPPLIERS CONNECTED TO ELECTRIC CAR")
        for record in result:
            print(
                f"Supplier: {record['supplier']} | "
                f"Component: {record['component']} | "
                f"Product: {record['product']}"
            )


# QUERY 4
# Find dependency path between a Tier-2 supplier and a plant
def tier2_dependency_path():
    query = """
    MATCH path =
        (tier2:Supplier {name: 'Global Components'})
        -[:SUPPLIES*1..3]->
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
    with driver.session() as session:
        result = session.run(query)
        print("\n# TIER-2 SUPPLIER DEPENDENCY PATH")
        for record in result:
            print(" -> ".join(record["dependency_path"]))


# QUERY 5
# Which components supplied by suppliers from a particular country are used in which products?
def components_from_country():
    query = """
    MATCH
        (s:Supplier)
        -[:LOCATED_IN]->
        (country:Country {name: 'India'}),
        (s)-[:SUPPLIES]->
        (c:Component)
        -[:USED_IN]->
        (p:Product)
    RETURN DISTINCT
        country.name AS country,
        s.name AS supplier,
        c.name AS component,
        p.name AS product
    ORDER BY component
    """
    with driver.session() as session:
        result = session.run(query)
        print("\n# COMPONENTS FROM INDIAN SUPPLIERS")
        for record in result:
            print(
                f"Country: {record['country']} | "
                f"Supplier: {record['supplier']} | "
                f"Component: {record['component']} | "
                f"Product: {record['product']}"
            )


# MAIN
def main():
    print("\n# SUPPLY CHAIN KNOWLEDGE GRAPH")
    # Create dataset
    create_dataset()
    # Required business queries
    products_depending_on_supplier()
    plants_affected_by_component()
    suppliers_connected_to_product()
    tier2_dependency_path()
    components_from_country()
    close_connection()


if __name__ == "__main__":
    main()