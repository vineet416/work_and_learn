def create_candidate(db, candidate_id, name, experience, location):
    query = """
    CREATE (c:Candidate {
        candidate_id: $candidate_id,
        name: $name,
        experience: $experience,
        location: $location
    })
    RETURN c.candidate_id AS candidate_id,
           c.name AS name
    """

    return db.run_query(query, {
        "candidate_id": candidate_id,
        "name": name,
        "experience": experience,
        "location": location,
    })


def read_candidate(db, candidate_id):
    query = """
    MATCH (c:Candidate {candidate_id: $candidate_id})
    RETURN c.candidate_id AS candidate_id,
           c.name AS name,
           c.experience AS experience,
           c.location AS location
    """

    return db.run_query(query, {
        "candidate_id": candidate_id,
    })


def update_candidate(db, candidate_id, new_location):
    query = """
    MATCH (c:Candidate {candidate_id: $candidate_id})
    SET c.location = $new_location
    RETURN c.candidate_id AS candidate_id,
           c.name AS name,
           c.location AS location
    """

    return db.run_query(query, {
        "candidate_id": candidate_id,
        "new_location": new_location,
    })


def delete_candidate(db, candidate_id):
    query = """
    MATCH (c:Candidate {candidate_id: $candidate_id})
    DETACH DELETE c
    RETURN $candidate_id AS deleted_candidate_id
    """

    return db.run_query(query, {
        "candidate_id": candidate_id,
    })


def demonstrate_crud(db):
    """Demonstrate all four CRUD operations."""

    demo_id = "C_DEMO"

    # Clean up if a previous run was interrupted.
    db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
        DETACH DELETE c
    """, {"candidate_id": demo_id})

    print("\n========== CRUD DEMONSTRATION ==========")

    print("\n1. CREATE")
    print(create_candidate(
        db, demo_id, "Demo Candidate", 0, "Mumbai"
    ))

    print("\n2. READ")
    print(read_candidate(db, demo_id))

    print("\n3. UPDATE")
    print(update_candidate(db, demo_id, "Pune"))

    print("\n4. DELETE")
    print(delete_candidate(db, demo_id))