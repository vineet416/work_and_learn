# Task 15: Docker Named Volume Persistence

## Objective

Demonstrate that data survives container removal by storing it in a named Docker volume.

## Build the Image

```powershell
docker build -t super30-task-15 .
```

## Create the Volume

```powershell
docker volume create super30-data
```

## Run the First Container

```powershell
docker run --name docker-task-15-a -v super30-data:/data super30-task-15
```

## Remove the First Container

```powershell
docker rm docker-task-15-a
```

## Run a Second Container with the Same Volume

```powershell
docker run --name docker-task-15-b -v super30-data:/data super30-task-15
```

## Expected Result

The second container displays both messages, proving that data persisted after the first container was removed.

## Key Concept

A named Docker volume stores data independently of a container's lifecycle. Reusing the same volume allows another container to access that data.