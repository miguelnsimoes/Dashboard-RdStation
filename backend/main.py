from fastapi import FastAPI
from backend.routers import newsletter

app = FastAPI()

app.include_router(newsletter.router)

@app.get("/")
def hello_world():
    return {"Hello" : "World"}