# Task 03: Create a Container with a Custom Name

## Objective
Run an Ubuntu container with a user-defined name and verify its identity.

## Commands Executed

```bash
docker run -it --name docker-task-03 ubuntu:latest
```

Inside the container:

```bash
whoami
hostname
cat /etc/os-release
exit
```

Verify the container:

```bash
docker ps -a
```

## Verification

- Container name: `docker-task-03`
- User: `root`
- Operating system: Ubuntu 26.04.1 LTS
- Container exit status: `0`