# Task 16: Communication Between Docker Containers

## Objective

Connect two containers through a custom Docker network and verify communication using container-name resolution.

## Step 1: Create the Network

```powershell
docker network create super30-network
docker network ls
```

## Step 2: Start the Nginx Container

```powershell
docker run -d `
  --name super30-web `
  --network super30-network `
  nginx:alpine
```

## Step 3: Start the Client Container

```powershell
docker run --rm `
  --name super30-client `
  --network super30-network `
  alpine `
  sh -c "apk add --no-cache curl && curl -I --max-time 5 http://super30-web"
```

## Step 4: Verify the Network

```powershell
docker network inspect super30-network
```

## Verification Output

The client received:

```text
HTTP/1.1 200 OK
Server: nginx/1.31.7
```

The network inspection confirmed that `super30-web` was connected to `super30-network`.

## Key Concept

Containers connected to the same user-defined Docker bridge network can communicate using container names through Docker's embedded DNS.