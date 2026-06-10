from fastapi import FastAPI

app = FastAPI(
    title="TITAN-ATLAS",
    version="0.1"
)

@app.get("/")
def root():
    return {
        "message": "TITAN-ATLAS API Running"
    }