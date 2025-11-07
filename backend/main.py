from fastapi import FastAPI
from backend.routers import newsletter
from backend.routers import crm
from backend.routers import landing_pages

app = FastAPI()

app.include_router(newsletter.router)
app.include_router(crm.router)
app.include_router(landing_pages.router)

@app.get("/")
def hello_world():
    return {"Hello" : "World"}

