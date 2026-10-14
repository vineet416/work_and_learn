def run_demo_queries(db):
    """Run 12 graph queries for CareerGraph."""

    candidate_id = "C001"
    job_id = "J002"

    # Q1: Retrieve a candidate's skills.
    print("\nQ1. Candidate skills")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
              -[:HAS_SKILL]->(s:Skill)
        RETURN c.name AS candidate,
               collect(s.name) AS skills
    """, {"candidate_id": candidate_id}))

    # Q2: Find jobs matching existing skills.
    print("\nQ2. Jobs matching existing skills")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
              -[:HAS_SKILL]->(s:Skill)
              <-[:REQUIRES_SKILL]-(j:Job)
        WITH j, collect(DISTINCT s.name) AS matching_skills
        RETURN j.title AS job, matching_skills
        ORDER BY size(matching_skills) DESC
    """, {"candidate_id": candidate_id}))

    # Q3: Identify missing skills for a selected job.
    print("\nQ3. Missing skills")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
        MATCH (j:Job {job_id: $job_id})
              -[:REQUIRES_SKILL]->(s:Skill)
        WHERE NOT (c)-[:HAS_SKILL]->(s)
        RETURN j.title AS job,
               s.name AS missing_skill
    """, {
        "candidate_id": candidate_id,
        "job_id": job_id,
    }))

    # Q4: Find courses that teach missing skills.
    print("\nQ4. Courses for missing skills")

    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
        MATCH (j:Job {job_id: $job_id})
            -[:REQUIRES_SKILL]->(s:Skill)
        WHERE NOT (c)-[:HAS_SKILL]->(s)
        MATCH (course:Course)-[:TEACHES]->(s)
        RETURN DISTINCT course.title AS course,
                        s.name AS skill
        ORDER BY course
    """, {
        "candidate_id": candidate_id,
        "job_id": job_id,
    }))

    # Q5: Find jobs offered by a company.
    print("\nQ5. Jobs offered by a company")
    print(db.run_query("""
        MATCH (co:Company {company_id: $company_id})
              -[:OFFERS]->(j:Job)
        RETURN co.name AS company,
               collect(j.title) AS jobs
    """, {"company_id": "CO001"}))

    # Q6: Rank jobs by matching skill percentage.
    print("\nQ6. Job match percentages")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
              -[:HAS_SKILL]->(s:Skill)
              <-[:REQUIRES_SKILL]-(j:Job)
        WITH j, count(DISTINCT s) AS matched_skills
        MATCH (j)-[:REQUIRES_SKILL]->(required:Skill)
        WITH j, matched_skills,
             count(DISTINCT required) AS total_skills
        RETURN j.title AS job,
               matched_skills,
               total_skills,
               round(
                   100.0 * matched_skills / total_skills,
                   2
               ) AS match_percentage
        ORDER BY match_percentage DESC
    """, {"candidate_id": candidate_id}))

    # Q7: Find candidates matching a particular job.
    print("\nQ7. Candidates matching a job")
    print(db.run_query("""
        MATCH (j:Job {job_id: $job_id})
              -[:REQUIRES_SKILL]->(s:Skill)
              <-[:HAS_SKILL]-(c:Candidate)
        WITH c, count(DISTINCT s) AS matched_skills
        RETURN c.name AS candidate, matched_skills
        ORDER BY matched_skills DESC
    """, {"job_id": job_id}))

    # Q8: Multi-hop traversal:
    # Candidate -> Skill <- Job <- Company
    print("\nQ8. Candidate-skill-job-company paths")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
              -[:HAS_SKILL]->(s:Skill)
              <-[:REQUIRES_SKILL]-(j:Job)
              <-[:OFFERS]-(co:Company)
        RETURN DISTINCT c.name AS candidate,
                        s.name AS skill,
                        j.title AS job,
                        co.name AS company
        ORDER BY job
        LIMIT $limit
    """, {
        "candidate_id": candidate_id,
        "limit": 20,
    }))

    # Q9: Find projects that build missing skills.
    print("\nQ9. Projects for missing skills")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
        MATCH (j:Job {job_id: $job_id})
              -[:REQUIRES_SKILL]->(s:Skill)
        WHERE NOT (c)-[:HAS_SKILL]->(s)
        MATCH (p:Project)-[:BUILDS_SKILL]->(s)
        RETURN DISTINCT p.title AS project,
                        s.name AS skill,
                        p.difficulty AS difficulty
        ORDER BY project
    """, {
        "candidate_id": candidate_id,
        "job_id": job_id,
    }))

    # Q10: Find the most frequently required skills.
    print("\nQ10. Most demanded skills")
    print(db.run_query("""
        MATCH (j:Job)-[:REQUIRES_SKILL]->(s:Skill)
        WITH s, count(DISTINCT j) AS demand
        RETURN s.name AS skill, demand
        ORDER BY demand DESC, skill
        LIMIT $limit
    """, {"limit": 10}))

    # Q11: Find candidates with shared skills.
    print("\nQ11. Similar candidates")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
              -[:HAS_SKILL]->(s:Skill)
              <-[:HAS_SKILL]-(other:Candidate)
        WHERE other.candidate_id <> $candidate_id
        RETURN other.name AS candidate,
               count(DISTINCT s) AS shared_skills
        ORDER BY shared_skills DESC
        LIMIT $limit
    """, {
        "candidate_id": candidate_id,
        "limit": 5,
    }))

    # Q12: Retrieve completed courses and the skills they teach.
    print("\nQ12. Candidate learning history")
    print(db.run_query("""
        MATCH (c:Candidate {candidate_id: $candidate_id})
              -[:COMPLETED]->(course:Course)
        OPTIONAL MATCH (course)-[:TEACHES]->(s:Skill)
        RETURN course.title AS course,
               collect(s.name) AS skills_taught
    """, {"candidate_id": candidate_id}))