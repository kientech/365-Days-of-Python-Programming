# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 13

# Building a REST API with FastAPI
# This requires FastAPI and an ASGI server like uvicorn.
# pip install "fastapi[all]"

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# In-memory "database"
db = []

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return db

# To run this server:
# 1. Save the file as main.py
# 2. Open your terminal in the same directory.
# 3. Run the command: uvicorn main:app --reload
#
# You can then access the API documentation at http://127.0.0.1:8000/docs 