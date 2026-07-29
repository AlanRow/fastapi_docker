from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello_docker():
    return { "message": "It's Dockerized app"}