from fastapi import FastAPI

from app.api.atlas import router as atlas_router

app = FastAPI(
    title="TITAN-ATLAS"
)

app.include_router(atlas_router)

@app.get("/")
def root():
    return {
        "status": "running"
    }