from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 설정
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터 저장을 위한 전역 변수
count_data = {"count": 0}

class CountData(BaseModel):
    count: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/get_count")
def get_count():
    return count_data

@app.get("/update_count")
def update_count(count: int):
    count_data["count"] = count
    return count_data
