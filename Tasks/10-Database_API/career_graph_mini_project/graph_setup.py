from data import (
    CANDIDATES,
    SKILLS,
    COMPANIES,
    JOBS,
    COURSES,
    PROJECTS,
)


def create_constraints(db):
    """Ensure each node has a unique ID."""

    constraints = [
        (
            "candidate_id_unique",
            "Candidate",
            "candidate_id",
        ),
        ("skill_id_unique", "Skill", "skill_id"),
        ("job_id_unique", "Job", "job_id"),
        ("company_id_unique", "Company", "company_id"),
        ("course_id_unique", "Course", "course_id"),
        ("project_id_unique", "Project", "project_id"),
    ]

    for name, label, property_name in constraints:
        query = (
            f"CREATE CONSTRAINT {name} IF NOT EXISTS "
            f"FOR (n:{label}) "
            f"REQUIRE n.{property_name} IS UNIQUE"
        )
        db.run_query(query)

    print("Uniqueness constraints created.")


def create_nodes(db):
    """Insert all six node types."""

    node_groups = [
        ("Candidate", "candidate_id", CANDIDATES),
        ("Skill", "skill_id", SKILLS),
        ("Company", "company_id", COMPANIES),
        ("Job", "job_id", JOBS),
        ("Course", "course_id", COURSES),
        ("Project", "project_id", PROJECTS),
    ]

    for label, id_field, records in node_groups:
        query = f"""
        UNWIND $records AS item
        MERGE (n:{label} {{{id_field}: item.{id_field}}})
        SET n += item
        """

        db.run_query(query, {"records": records})

    print("All node types created.")


def create_relationships(db):
    """Create the seven relationship types."""

    # Candidate -> Skill
    edges = []
    for i, candidate in enumerate(CANDIDATES):
        for offset in range(3):
            skill = SKILLS[(i + offset) % len(SKILLS)]
            edges.append({
                "candidate_id": candidate["candidate_id"],
                "skill_id": skill["skill_id"],
            })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (c:Candidate {candidate_id: edge.candidate_id})
        MATCH (s:Skill {skill_id: edge.skill_id})
        MERGE (c)-[:HAS_SKILL]->(s)
    """, {"edges": edges})

    # Job -> Skill
    edges = []
    for i, job in enumerate(JOBS):
        for offset in range(3):
            skill = SKILLS[(2 * i + offset) % len(SKILLS)]
            edges.append({
                "job_id": job["job_id"],
                "skill_id": skill["skill_id"],
            })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (j:Job {job_id: edge.job_id})
        MATCH (s:Skill {skill_id: edge.skill_id})
        MERGE (j)-[:REQUIRES_SKILL]->(s)
    """, {"edges": edges})

    # Company -> Job
    edges = []
    for i, job in enumerate(JOBS):
        company = COMPANIES[i % len(COMPANIES)]
        edges.append({
            "company_id": company["company_id"],
            "job_id": job["job_id"],
        })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (co:Company {company_id: edge.company_id})
        MATCH (j:Job {job_id: edge.job_id})
        MERGE (co)-[:OFFERS]->(j)
    """, {"edges": edges})

    # Course -> Skill
    edges = []
    for i, course in enumerate(COURSES):
        for offset in range(2):
            skill = SKILLS[(i + offset) % len(SKILLS)]
            edges.append({
                "course_id": course["course_id"],
                "skill_id": skill["skill_id"],
            })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (course:Course {course_id: edge.course_id})
        MATCH (s:Skill {skill_id: edge.skill_id})
        MERGE (course)-[:TEACHES]->(s)
    """, {"edges": edges})

    # Project -> Skill
    edges = []
    for i, project in enumerate(PROJECTS):
        for offset in range(2):
            skill = SKILLS[(i + 3 + offset) % len(SKILLS)]
            edges.append({
                "project_id": project["project_id"],
                "skill_id": skill["skill_id"],
            })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (p:Project {project_id: edge.project_id})
        MATCH (s:Skill {skill_id: edge.skill_id})
        MERGE (p)-[:BUILDS_SKILL]->(s)
    """, {"edges": edges})

    # Candidate -> Job
    edges = []
    for i, candidate in enumerate(CANDIDATES):
        edges.append({
            "candidate_id": candidate["candidate_id"],
            "job_id": JOBS[(i + 1) % len(JOBS)]["job_id"],
        })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (c:Candidate {candidate_id: edge.candidate_id})
        MATCH (j:Job {job_id: edge.job_id})
        MERGE (c)-[:INTERESTED_IN]->(j)
    """, {"edges": edges})

    # Candidate -> Course
    edges = []
    for i, candidate in enumerate(CANDIDATES):
        edges.append({
            "candidate_id": candidate["candidate_id"],
            "course_id": COURSES[i]["course_id"],
        })

    db.run_query("""
        UNWIND $edges AS edge
        MATCH (c:Candidate {candidate_id: edge.candidate_id})
        MATCH (course:Course {course_id: edge.course_id})
        MERGE (c)-[:COMPLETED]->(course)
    """, {"edges": edges})

    print("All seven relationship types created.")


def seed_data(db):
    """Create nodes first, then their relationships."""
    create_nodes(db)
    create_relationships(db)
    print("Graph seed completed.")


def verify_graph(db):
    """Check the actual graph size and relationship types."""

    node_result = db.run_query("""
        MATCH (n)
        RETURN count(n) AS total_nodes
    """)

    relationship_result = db.run_query("""
        MATCH ()-[r]->()
        RETURN count(r) AS total_relationships
    """)

    node_count = node_result[0]["total_nodes"]
    relationship_count = relationship_result[0]["total_relationships"]

    print("\n========== GRAPH VERIFICATION ==========")
    print("Total nodes:", node_count)
    print("Total relationships:", relationship_count)

    print("\nNode counts by type:")
    for record in db.run_query("""
        MATCH (n)
        UNWIND labels(n) AS label
        RETURN label, count(*) AS total
        ORDER BY label
    """):
        print(record)

    print("\nRelationship counts by type:")
    for record in db.run_query("""
        MATCH ()-[r]->()
        RETURN type(r) AS relationship_type, count(r) AS total
        ORDER BY relationship_type
    """):
        print(record)

    if node_count < 50 or relationship_count < 75:
        raise RuntimeError(
            "Graph does not meet the minimum assignment requirements."
        )

    print("\nGraph size requirements satisfied.")