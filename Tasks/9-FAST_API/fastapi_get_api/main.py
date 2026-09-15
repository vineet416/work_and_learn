from fastapi import FastAPI

app = FastAPI()


# 1. Home API
@app.get("/")
def home():
    return {"message": "Welcome to Super30 FastAPI"}


# 2. Student API
@app.get("/student")
def student():
    return {
        "name": "Vineet Patel",
        "batch": "Super30",
        "role": "Student"
    }


# 3. Course API
@app.get("/course")
def course():
    return {
        "course_name": "Backend Development with FastAPI",
        "mentor": "Sudhanshu",
        "duration": "8 Weeks",
        "topics": ["Python","FastAPI","REST API","Database","Deployment"]
    }


# 4. Skills API
@app.get("/skills")
def skills():
    return {"skills": ["Python","FastAPI","SQL","Docker","AWS"]}


# 5. Addition API
@app.get("/add/{num1}/{num2}")
def add_numbers(num1: int, num2: int):
    return {"result": num1 + num2}


# 6. Multiplication API
@app.get("/multiply/{num1}/{num2}")
def multiply_numbers(num1: int, num2: int):
    return {"result": num1 * num2}


# 7. Square API
@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number ** 2}


# 8. Even/Odd API
@app.get("/check/{number}")
def check_even_odd(number: int):
    if number % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"
    return {"number": number, "type": number_type}


# 9. Age API
@app.get("/age/{age}")
def check_age(age: int):
    if age < 13:
        message = "You are a child."
    elif age < 20:
        message = "You are a teenager."
    elif age < 60:
        message = "You are an adult."
    else:
        message = "You are a senior citizen."
    return {"age": age, "message": message}


# 10. Table API
@app.get("/table/{number}")
def multiplication_table(number: int):
    table = [ f"{number} x {i} = {number * i}" for i in range(1, 11)]
    return {"number": number, "table": table}


# 11. Profile API
@app.get("/profile/{name}/{age}")
def profile(name: str, age: int):
    return {"name": name, "age": age}


# 12. Number Analysis API
@app.get("/number/{number}")
def number_analysis(number: int):
    return {
        "number": number,
        "square": number ** 2,
        "cube": number ** 3,
        "even": number % 2 == 0
    }