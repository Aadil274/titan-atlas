from fastapi import FastAPI

from app.api.atlas import router as atlas_router
from app.api import titan
from app.api import reports

app = FastAPI(
    title="TITAN-ATLAS"
)

app.include_router(atlas_router)
app.include_router(titan.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {
        "status": "running"
    }