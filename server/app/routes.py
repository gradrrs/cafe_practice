from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import MenuItem, Order

app = FastAPI()

class OrderRequest(BaseModel):
    item_name: str
    quantity: int

@app.get("/menu")
def get_menu():
    db: Session = SessionLocal()
    items = db.query(MenuItem).all()
    return [{"name": i.name, "price": i.price} for i in items]

@app.post("/order")
def post_order(order_req: OrderRequest):
    db: Session = SessionLocal()
    order = Order(item_name=order_req.item_name, quantity=order_req.quantity)
    db.add(order)
    db.commit()
    return {"status": "success"}
