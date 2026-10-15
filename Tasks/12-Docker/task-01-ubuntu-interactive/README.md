# Task 01: Ubuntu Interactive Container

## Objective
Pull the latest Ubuntu Docker image, run an interactive container, and execute five Linux commands.

## Commands Executed

```bash
docker pull ubuntu:latest
docker run -it --name docker-task-01 ubuntu:latest
```

Inside the container:

```bash
whoami
pwd
ls
cat /etc/os-release
echo "Hello from my Ubuntu Docker container!"
```

Exit the container:

```bash
exit
```

Verify the container:

```bash
docker ps -a
```

## Verification

- Successfully pulled `ubuntu:latest`.
- `whoami` displayed `root`.
- `pwd` displayed `/`.
- `ls` displayed the Ubuntu root directories.
- `/etc/os-release` confirmed Ubuntu 26.04.1 LTS.
- The `echo` command displayed the expected message.
- The container exited with status `0`.