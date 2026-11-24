from sqlalchemy import *
from fileex import db


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)
    price = db.Column(Integer, nullable=False)
    active = Column(Integer, nullable=False, index=True)
