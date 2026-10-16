# Task 07: Build and Run a Docker Image

## Objective
Build a Docker image for a Python application, run a container, and verify its output.

## Build the Image

```powershell
docker build -t super30-python-app ./task-06-python-dockerfile
```

## Run the Container

```powershell
docker run --name docker-task-07 super30-python-app
```

## Output

```text
Hello from my first Python Docker application!
Task 6: Custom Docker image built successfully.
```

## Verification

- Image built successfully with the required name `super30-python-app`.
- Python application ran successfully.
- Container `docker-task-07` exited with status 0.
- Image verified with `docker images super30-python-app`.