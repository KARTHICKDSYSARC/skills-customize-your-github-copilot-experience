from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mergington FastAPI Assignment")


class Item(BaseModel):
    name: str
    price: float


items = [
    {"id": 1, "name": "Notebook", "price": 3.5},
    {"id": 2, "name": "Pen", "price": 1.25},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API!"}


@app.get("/items")
def get_items(limit: int | None = None):
    if limit is not None:
        return items[:limit]
    return items


@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price,
    }
    items.append(new_item)
    return new_item
