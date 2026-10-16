# Task 16: Communication Between Docker Containers

## Objective
Connect two containers through a custom Docker network and verify communication using container-name resolution.

## Create the Network

```powershell
docker network create super30-network
```

## Start the Web Container

```powershell
docker run -d --name super30-web --network super30-network nginx:alpine
```

## Start the Client Container

```powershell
docker run --rm --name super30-client --network super30-network alpine sh -c "apk add --no-cache curl && curl -I --max-time 5 http://super30-web"
```

## Verify the Network

```powershell
docker network inspect super30-network
```

## Result

The client receives an HTTP response from the Nginx container, normally `HTTP/1.1 200 OK`.

## Key Concept

Containers connected to the same user-defined Docker network can communicate using container names through Docker's embedded DNS.