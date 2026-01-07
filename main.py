from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://695eae376cc9c2339af850dc--jade-heliotrope-6abf2c.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/customers")
async def get_customers():
    customers = []
    async for c in db["Customers"].find({}, {"_id": 0}):
        customers.append(c)
    return customers
