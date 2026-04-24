from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detector import scan_email

app = FastAPI(title="Gmail Phishing Detector")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailInput(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/scan")
def scan(data: EmailInput):
    return scan_email(data.content)