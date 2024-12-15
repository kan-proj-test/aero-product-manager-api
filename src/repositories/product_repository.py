# product_repository.py

from src.models.product import Product
from src.repositories.base import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__(Product)

    def get_by_name(self, name):
        return self.model.query.filter_by(name=name).first()