-- ==========================================
-- PROJECTS TABLE
-- ==========================================

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);


-- ==========================================
-- TASKS TABLE
-- ==========================================

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,

    project_id INTEGER NOT NULL,

    title VARCHAR(150) NOT NULL,

    description TEXT,

    assigned_to VARCHAR(100),

    status VARCHAR(30) NOT NULL DEFAULT 'pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_task_project
        FOREIGN KEY (project_id)
        REFERENCES projects(id)
        ON DELETE CASCADE
);