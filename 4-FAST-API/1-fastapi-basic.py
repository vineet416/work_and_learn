"""
To run this app, use the command: uvicorn 1-fastapi-basic:app --reload
"""

# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


# Define a route for the custom endpoint "/vineet/patel" that responds to GET requests
@app.get("/vineet/patel")   
def test():
    print("this is my first fastapi app")
    return {
        "message": "this is my first fastapi app"
    }


# Define a route for "/add" that takes two query parameters a and b, adds them, and returns the result
@app.get("/add")
def add(a, b):
    a,b = int(a), int(b)
    return {
        "a" : a,
        "b" : b,
        "result" : a+b
    }



# Define a route for "/calculator" that takes two float parameters a and b, and an operation string to perform basic arithmetic operations
@app.get("/calculator")
def calculator(a:float, b:float, operation:str):
    """
    This endpoint performs basic arithmetic operations (addition, subtraction, multiplication, division) based on the provided operation parameter. 
    The parameters a and b are expected to be floats, and the operation parameter should be one of the following strings: 'add', 'sub', 'mul', or 'div'.
    """
    if operation=='add':
        result = a+b
    elif operation =='sub':
        result = a-b
    elif operation =='mul':
        result = a*b
    elif operation == 'div':
        if b==0:
            return {"error ": "you cannot divide by zero"}
        result = a/b
    else:
        return {"error ": "you need to pass the valid input"}
    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result,
        }



# Import datetime module to get the current server time
from datetime import datetime

# Define a route for "/current_time" that returns the current server time in a formatted string
@app.get("/current_time")
def get_current_time():
    return {
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }




# Import socket, platform, and os modules to get system information
import socket
import platform
import os

# Define a route for "/system_info" that returns various system information 
# Such as hostname, local IP, OS details, architecture, machine type, processor, Python version, and current working directory of the server
@app.get("/system_info")
def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "current_working_directory": os.getcwd()
    }





# Import Request class from fastapi to access request information
from fastapi import Request

# Define a route for "/visitor_ip" that returns the visitor's IP address and port number
@app.get("/visitor_ip")
def visitor_ip(request: Request):
    return {
        "visitor_ip": request.client.host,
        "visitor_port": request.client.port
    }





# Define a route for "/visitor_info" that returns detailed information about the visitor
@app.get("/visitor_info")
def get_visitor_info(request: Request):
    visitor_ip = request.client.host
    visitor_port = request.client.port
    user_agent = request.headers.get("user-agent")
    referer = request.headers.get("referer")
    method = request.method
    url = str(request.url)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "visitor_ip": visitor_ip,
        "visitor_port": visitor_port,
        "user_agent": user_agent,
        "referer": referer,
        "method": method,
        "url": url,
        "timestamp": timestamp
    }




