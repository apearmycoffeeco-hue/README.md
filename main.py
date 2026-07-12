from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PoolPro AI")

@app.get("/")
def home():
    return {"message": "PoolPro AI is running! 🚀"}

@app.get("/quote")
def get_quote(job_type: str):
    return {"quote": f"Quote for {job_type} job
