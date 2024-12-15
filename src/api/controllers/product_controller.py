# product_controller.py

from flask import jsonify, request
from src.services.product_service import ProductService

class ProductController:
    def __init__(self):
        self.product_service = ProductService()

    def get_all_products(self):
        products = self.product_service.get_all_products()
        return jsonify(products), 200

    def create_product(self):
        data = request.get_json()
        new_product = self.product_service.create_product(data)
        return jsonify(new_product), 201