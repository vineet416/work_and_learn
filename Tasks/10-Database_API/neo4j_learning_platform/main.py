from database import driver, close_connection


# CREATE NODES
def create_nodes():
    query = """
    CREATE
        (s1:Student {name: 'Rahul', age: 21, city: 'Pune'}),
        (s2:Student {name: 'Amit', age: 22, city: 'Mumbai'}),
        (s3:Student {name: 'Priya', age: 20, city: 'Delhi'}),
        (s4:Student {name: 'Neha', age: 21, city: 'Bangalore'}),
        (s5:Student {name: 'Arjun', age: 23, city: 'Hyderabad'}),
        (s6:Student {name: 'Sneha', age: 20, city: 'Chennai'}),

        (c1:Course {name: 'Python Programming', duration: '8 weeks'}),
        (c2:Course {name: 'Data Analytics', duration: '10 weeks'}),
        (c3:Course {name: 'Machine Learning', duration: '12 weeks'}),
        (c4:Course {name: 'Agentic AI', duration: '10 weeks'}),

        (m1:Mentor {name: 'Vineet', experience: 5}),
        (m2:Mentor {name: 'Rohit', experience: 7}),
        (m3:Mentor {name: 'Anjali', experience: 6}),

        (sk1:Skill {name: 'Python'}),
        (sk2:Skill {name: 'Pandas'}),
        (sk3:Skill {name: 'Machine Learning'}),
        (sk4:Skill {name: 'AI Agents'}),

        (p1:Project {name: 'Student Analytics System', type: 'Data Analytics'}),
        (p2:Project {name: 'AI Research Assistant', type: 'Agentic AI'}),

        (co1:Company {name: 'TechNova', industry: 'Software'}),
        (co2:Company {name: 'DataWorks', industry: 'Analytics'})
    """
    with driver.session() as session:
        session.run(query)
    print("21 nodes created.")


# CREATE RELATIONSHIPS
def create_relationships():
    query = """
    MATCH
        (s1:Student {name: 'Rahul'}),
        (s2:Student {name: 'Amit'}),
        (s3:Student {name: 'Priya'}),
        (s4:Student {name: 'Neha'}),
        (s5:Student {name: 'Arjun'}),
        (s6:Student {name: 'Sneha'}),

        (c1:Course {name: 'Python Programming'}),
        (c2:Course {name: 'Data Analytics'}),
        (c3:Course {name: 'Machine Learning'}),
        (c4:Course {name: 'Agentic AI'}),

        (m1:Mentor {name: 'Vineet'}),
        (m2:Mentor {name: 'Rohit'}),
        (m3:Mentor {name: 'Anjali'}),

        (sk1:Skill {name: 'Python'}),
        (sk2:Skill {name: 'Pandas'}),
        (sk3:Skill {name: 'Machine Learning'}),
        (sk4:Skill {name: 'AI Agents'}),

        (p1:Project {name: 'Student Analytics System'}),
        (p2:Project {name: 'AI Research Assistant'}),

        (co1:Company {name: 'TechNova'}),
        (co2:Company {name: 'DataWorks'})

    CREATE

        // Student -> Course
        (s1)-[:ENROLLED_IN]->(c1),
        (s2)-[:ENROLLED_IN]->(c1),
        (s3)-[:ENROLLED_IN]->(c2),
        (s4)-[:ENROLLED_IN]->(c3),
        (s5)-[:ENROLLED_IN]->(c4),
        (s6)-[:ENROLLED_IN]->(c4),

        // Mentor -> Course
        (m1)-[:TEACHES]->(c1),
        (m1)-[:TEACHES]->(c4),
        (m2)-[:TEACHES]->(c2),
        (m3)-[:TEACHES]->(c3),

        // Course -> Skill
        (c1)-[:TEACHES_SKILL]->(sk1),
        (c2)-[:TEACHES_SKILL]->(sk2),
        (c3)-[:TEACHES_SKILL]->(sk3),
        (c4)-[:TEACHES_SKILL]->(sk4),

        // Student -> Project
        (s1)-[:BUILT]->(p1),
        (s3)-[:BUILT]->(p1),
        (s5)-[:BUILT]->(p2),

        // Project -> Skill
        (p1)-[:USES]->(sk1),
        (p1)-[:USES]->(sk2),
        (p2)-[:USES]->(sk1),
        (p2)-[:USES]->(sk4),

        // Student -> Company
        (s1)-[:INTERESTED_IN]->(co1),
        (s2)-[:INTERESTED_IN]->(co1),
        (s3)-[:INTERESTED_IN]->(co2),
        (s5)-[:INTERESTED_IN]->(co2)
    """
    with driver.session() as session:
        session.run(query)
    print("25 relationships created.")


# READ DATA
def read_graph():
    query = """
    MATCH (n)
    RETURN labels(n) AS labels, n
    ORDER BY labels(n)
    """
    with driver.session() as session:
        result = session.run(query)
        print("\n===== GRAPH NODES =====")
        for record in result:
            print(record["labels"], dict(record["n"]))


# READ RELATIONSHIPS
def read_relationships():
    query = """
    MATCH (a)-[r]->(b)
    RETURN
        a.name AS from_node,
        type(r) AS relationship,
        b.name AS to_node
    """
    with driver.session() as session:
        result = session.run(query)
        print("\n===== GRAPH RELATIONSHIPS =====")
        for record in result:
            print(
                f"{record['from_node']} "
                f"-[:{record['relationship']}]-> "
                f"{record['to_node']}"
            )


# UPDATE DATA
def update_student():
    query = """
    MATCH (s:Student {name: 'Rahul'})
    SET s.city = 'Bangalore'
    RETURN s
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()
        if record:
            print("\nUpdated Student:")
            print(dict(record["s"]))


# DELETE RELATIONSHIP
def delete_relationship():
    query = """
    MATCH
        (s:Student {name: 'Rahul'})
        -[r:INTERESTED_IN]->
        (c:Company {name: 'TechNova'})
    DELETE r
    """
    with driver.session() as session:
        session.run(query)
    print("\nRelationship deleted.")


# CREATE THE DELETED RELATIONSHIP AGAIN
def recreate_relationship():
    query = """
    MATCH
        (s:Student {name: 'Rahul'}),
        (c:Company {name: 'TechNova'})
    CREATE (s)-[:INTERESTED_IN]->(c)
    """
    with driver.session() as session:
        session.run(query)
    print("Relationship recreated for the final graph.")


# DELETE NODE
def delete_node():
    query = """
    MATCH (s:Student {name: 'Sneha'})
    DETACH DELETE s
    """
    with driver.session() as session:
        session.run(query)
    print("\nStudent node deleted.")


# CREATE THE DELETED NODE AGAIN
def recreate_node():
    query = """
    CREATE (s:Student {
        name: 'Sneha',
        age: 20,
        city: 'Chennai'
    })
    """
    with driver.session() as session:
        session.run(query)
    print("Student node recreated for the final graph.")


# COUNT NODES AND RELATIONSHIPS
def count_graph():
    node_query = """
    MATCH (n)
    RETURN count(n) AS total_nodes
    """
    relationship_query = """
    MATCH ()-[r]->()
    RETURN count(r) AS total_relationships
    """
    with driver.session() as session:
        node_result = session.run(node_query)
        node_record = node_result.single()
        relationship_result = session.run(relationship_query)
        relationship_record = relationship_result.single()
        print("\n===== GRAPH COUNT =====")
        print("Total Nodes:", node_record["total_nodes"])
        print("Total Relationships:", relationship_record["total_relationships"])



# MAIN
def main():
    print("===== NEO4J LEARNING PLATFORM GRAPH =====")
    # Create graph
    create_nodes()
    create_relationships()
    # Read graph
    read_graph()
    read_relationships()
    # Count graph
    count_graph()
    # Update
    update_student()
    # Delete relationship
    delete_relationship()
    # Recreate relationship so final graph remains complete
    recreate_relationship()
    # Delete node
    delete_node()
    # Recreate node so final graph remains complete
    recreate_node()
    # Final count
    count_graph()
    # Close connection
    close_connection()


if __name__ == "__main__":
    main()