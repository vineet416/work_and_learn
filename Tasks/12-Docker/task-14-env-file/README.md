# Task 14: Environment Configuration with a .env File

## Objective
Load application configuration from a `.env` file and prevent local environment files from being committed to Git.

## Project Structure

```text
task-14-env-file/
├── main.py
├── Dockerfile
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Build the Image

```powershell
docker build -t super30-task-14 .
```

## Run with Environment Variables

```powershell
docker run --rm --env-file .env --name docker-task-14 super30-task-14
```

## Output

```text
Application: Super30 Docker Demo
Environment: testing
Database password configured: True
```

## Security Practices

- `.env` contains local configuration and must not be committed.
- `.env.example` documents the required variables using placeholder values.
- The `.gitignore` file excludes `.env`.
- The application never prints the password itself.
- Real credentials must not be placed in Docker images or source control.