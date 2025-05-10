from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)