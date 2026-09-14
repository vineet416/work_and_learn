from fastapi import FastAPI
import numpy as np

# Create a FastAPI instance
app = FastAPI()

# Define a NumPy array of numbers
numbers = np.array([12, 7, 25, 4, 18, 31, 10, 6, 22, 15])


@app.get("/numbers")
def get_numbers():
    return {"numbers": numbers.tolist()}


@app.get("/mean")
def get_mean():
    return {"mean": float(np.mean(numbers))}


@app.get("/median")
def get_median():
    return {"median": float(np.median(numbers))}


@app.get("/std")
def get_standard_deviation():
    return {"standard_deviation": float(np.std(numbers))}


@app.get("/variance")
def get_variance():
    return {"variance": float(np.var(numbers))}


@app.get("/maximum")
def get_maximum():
    return {"maximum": int(np.max(numbers))}


@app.get("/minimum")
def get_minimum():
    return {"minimum": int(np.min(numbers))}


@app.get("/sum")
def get_sum():
    return {"sum": int(np.sum(numbers))}


@app.get("/even")
def get_even_numbers():
    return {"even": numbers[numbers % 2 == 0].tolist()}


@app.get("/odd")
def get_odd_numbers():
    return {"odd": numbers[numbers % 2 != 0].tolist()}


@app.get("/stats")
def get_stats():
    return {
        "mean": float(np.mean(numbers)),
        "median": float(np.median(numbers)),
        "standard_deviation": float(np.std(numbers)),
        "variance": float(np.var(numbers)),
        "maximum": int(np.max(numbers)),
        "minimum": int(np.min(numbers)),
    }


@app.get("/table/{number}")
def multiplication_table(number):
    table = [{"multiplier": i, "result": int(number) * i} for i in range(1, 11)]
    return {"number": int(number), "table": table}

