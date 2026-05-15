from fastapi import FastAPI

app=FastAPI()

@app.get("/employees")
def get_employees():
    return {
        "name":"giri",
        "age":21,
        "salary":45000
    }