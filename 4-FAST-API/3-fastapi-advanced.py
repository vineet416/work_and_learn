from fastapi import FastAPI, Depends, HTTPException, Header, status
from fastapi.security import APIKeyHeader

# Create FastAPI app
app = FastAPI()

# Security key for token verification
SECRET_KEY = "test123"

# Token verification dependency
def verify_token(x_token: str = Header()):
    if x_token != SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid X-Token header",
        )
    return True


# API to test token verification
@app.get("/test")
def test(verified: bool = Depends(verify_token)):
    return {"message": "Token verified successfully"}





# API key verification dependency
api_key_header = APIKeyHeader(name="X-API-Key")

# API to test API key verification
@app.get("/test1")
def test1(api_key: str = Depends(api_key_header)):
    if api_key != SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return {"message": "API Key verified successfully"}







# Rate limiting implementation
import time
from fastapi import Request

# Dictionary to store request history for rate limiting
request_history = {}

# Rate limiting 
@app.get("/rate-limiting")
def rate_limiting(request: Request):
    client_ip = request.client.host
    current_time = time.time()

    # Check if the client IP is already in the request history, if not, initialize it
    if client_ip not in request_history:
        request_history[client_ip] = []

    # Remove timestamps older than 60 seconds from the request history
    request_history[client_ip] = [timestamp for timestamp in request_history[client_ip] if current_time - timestamp < 60]

    # Check if the number of requests in the last 60 seconds exceeds the limit (5 requests)
    if len(request_history[client_ip]) >= 5:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Try again later.",
        )

    # Add the current timestamp to the request history
    request_history[client_ip].append(current_time)

    # Return a success message along with the client IP and the number of requests made in the last 60 seconds
    return {
        "message": "Request successful", 
        "client_ip": client_ip, 
        "request_count": len(request_history[client_ip])
        }







# Define a Pydantic model for the book data
from pydantic import BaseModel

class books(BaseModel):
    title: str
    author: str
    year: int


# API to create a book with API key verification
@app.post("/create_book")
def create_book(book: books, api_key: str = Depends(api_key_header)):
    if api_key != SECRET_KEY:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API Key",
            )
    return {"message": "Book added successfully", "book": book.dict()}