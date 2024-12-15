# routes.py

from flask import Blueprint
from src.api.controllers.product_controller import ProductController

api_bp = Blueprint('api', __name__)
product_controller = ProductController()

@api_bp.route('/products', methods=['GET'])
def get_products():
    return product_controller.get_all_products()

@api_bp.route('/products', methods=['POST'])
def create_product():
    return product_controller.create_product()