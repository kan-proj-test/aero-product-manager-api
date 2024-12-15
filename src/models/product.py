# product.py

from sqlalchemy import Column, Integer, String, Float
from src.models.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f'Product(id={self.id}, name={self.name})'