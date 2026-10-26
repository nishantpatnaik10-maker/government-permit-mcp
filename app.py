from fastapi import FastAPI
import json

app = FastAPI()

with open("permit_data.json") as f:
    permits = json.load(f)

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/permit/{permit_id}")
def get_permit(permit_id: str):
    return permits.get(permit_id, {"status": "Not Found"})
