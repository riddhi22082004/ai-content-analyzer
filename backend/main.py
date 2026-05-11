from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "running"}

@app.post("/analyze")
def analyze(data: dict):
    text = data.get("text", "").lower()

    if "good" in text:
        return {"result": "Positive"}
    elif "bad" in text:
        return {"result": "Negative"}
    else:
        return {"result": "Neutral"}