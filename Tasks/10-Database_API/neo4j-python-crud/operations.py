from database import driver


# 1. Create Node
def create_student(name, age, city):
    query = """
    CREATE (s:Student {
        name: $name,
        age: $age,
        city: $city
    })
    RETURN s
    """
    with driver.session() as session:
        result = session.run(query, name=name, age=age, city=city)
        record = result.single()
        if record:
            return {"message": "Student created:", "student": record["s"]}


# 2. Create Relationship
def create_relationship(student_name, course_name):
    query = """
    MATCH (s:Student {name: $student_name})
    MATCH (c:Course {name: $course_name})
    CREATE (s)-[:ENROLLED_IN]->(c)
    RETURN s, c
    """
    with driver.session() as session:
        result = session.run(query, student_name=student_name, course_name=course_name)
        record = result.single()
        if record:
            return {"message": "Relationship created between student and course:", "student": record["s"], "course": record["c"]}


# 3. Read Nodes
def read_students():
    query = """
    MATCH (s:Student)
    RETURN s
    ORDER BY s.name
    """
    with driver.session() as session:
        result = session.run(query)
        students = []        
        for record in result:
            students.append(record["s"])
        return {"message": "Students retrieved successfully.", "students": students}


# 4. Search / Filter
def search_students_by_city(city):
    query = """
    MATCH (s:Student)
    WHERE s.city = $city
    RETURN s
    """
    with driver.session() as session:
        result = session.run(query, city=city)
        students = []
        for record in result:
            students.append(record["s"])
        return {"message": f"Students in city '{city}':", "students": students}


# 5. Update Properties
def update_student_city(name, new_city):
    query = """
    MATCH (s:Student {name: $name})
    SET s.city = $new_city
    RETURN s
    """
    with driver.session() as session:
        result = session.run(query, name=name, new_city=new_city)
        record = result.single()
        if record:
            student = record["s"]
            return {"message": f"Student '{name}' city updated to '{new_city}'.", "student": student}


# 6. Delete Relationship
def delete_relationship(student_name, course_name):
    query = """
    MATCH (s:Student {name: $student_name})
          -[r:ENROLLED_IN]->
          (c:Course {name: $course_name})
    DELETE r
    """
    with driver.session() as session:
        session.run(query, student_name=student_name, course_name=course_name)
        return {"message": f"Relationship between student '{student_name}' and course '{course_name}' deleted."}


# 7. Delete Node
def delete_student(name):
    query = """
    MATCH (s:Student {name: $name})
    DETACH DELETE s
    """
    with driver.session() as session:
        session.run(query, name=name)
        return {"message": f"Student '{name}' deleted successfully."}