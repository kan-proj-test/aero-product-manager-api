# product_service.py

from src.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all_products(self):
        return self.product_repository.get_all()

    def create_product(self, data):
        return self.product_repository.create(data)