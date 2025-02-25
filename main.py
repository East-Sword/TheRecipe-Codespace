from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "East gold its rising the proyect The recepy its growing ia will be implemented in 2 weeks  "}
