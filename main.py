from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Simple Calculator API"}

@app.get("/add")
def add(num1: float, num2: float):
    return {"Result": num1 + num2}

@app.get("/subtract")
def subtract(num1:float, num2:float):
    return {"Result": num1 - num2}

@app.get("/multiply")
def multiply(num1:float, num2:float):
    return {"Result": num1 * num2}

@app.get("/divide")
def divide(num1:float, num2:float):
    return {"Result": num1 / num2}