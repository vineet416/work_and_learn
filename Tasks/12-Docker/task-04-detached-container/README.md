# Task 04: Detached Container Lifecycle

## Objective
Run an Ubuntu container in detached mode and practise listing, stopping, restarting, and removing it.

## Commands Executed

### Start in detached mode

```bash
docker run -dit --name docker-task-04 ubuntu:latest
```

### Check running containers

```bash
docker ps
```

### Stop the container

```bash
docker stop docker-task-04
docker ps -a
```

### Restart the container

```bash
docker start docker-task-04
docker ps
```

### Remove the container

```bash
docker stop docker-task-04
docker rm docker-task-04
docker ps -a
```