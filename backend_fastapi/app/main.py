from fastapi import FastAPI

app = FastAPI(title="FastAPI Backend Experiments")

@app.get("/")
def root():
    return {"status": "FastAPI running"}