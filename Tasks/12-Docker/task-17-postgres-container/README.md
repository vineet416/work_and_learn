# Task 17: Run PostgreSQL in a Docker Container

## Objective

Run PostgreSQL in a separate Docker container and configure the database name, username, and password using environment variables.

## Configuration

| Variable | Value |
|---|---|
| `POSTGRES_DB` | `super30db` |
| `POSTGRES_USER` | `super30user` |
| `POSTGRES_PASSWORD` | Demonstration password |

## Start the PostgreSQL Container

```powershell
docker run -d `
  --name super30-postgres `
  -e POSTGRES_DB=super30db `
  -e POSTGRES_USER=super30user `
  -e POSTGRES_PASSWORD=demo-password-123 `
  -p 5432:5432 `
  postgres:17
```

## Verify the Container

```powershell
docker ps
docker logs super30-postgres
```

Wait for PostgreSQL to report that it is ready to accept connections.

## Check Database Readiness

```powershell
docker exec super30-postgres pg_isready -U super30user -d super30db
```

Expected output:

```text
/var/run/postgresql:5432 - accepting connections
```

## Verify the Database and User

Connect to PostgreSQL:

```powershell
docker exec -it super30-postgres psql -U super30user -d super30db
```

Execute:

```sql
SELECT current_database(), current_user;
```

Expected result:

```text
 current_database | current_user
------------------+-------------
 super30db        | super30user
```

Exit the PostgreSQL shell:

```text
\q
```

## Key Concepts

- PostgreSQL runs inside a Docker container.
- Environment variables configure the initial database and user.
- Port `5432` is PostgreSQL's default port.
- `pg_isready` checks whether PostgreSQL is accepting connections.

## Security Note

The password used here is for demonstration only. Real credentials should be stored outside source control.