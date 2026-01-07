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

def serialize_customer(c):
    return {
        "_id": str(c["_id"]),
        "id": c.get("id"),
        "fullName": c.get("fullName"),
        "email": c.get("email"),
        "type": c.get("type"),
        "discount": c.get("discount"),
        "totalSale": c.get("totalSale"),
    }

@app.get("/customers")
async def get_customers():
    result = []
    async for c in customers.find():
        result.append(serialize_customer(c))
    return result