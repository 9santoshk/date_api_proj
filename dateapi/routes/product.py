import sys, os
sys.path.append('..')
from flask import Blueprint, jsonify, request
import datetime
from app import db
import logging
from models.product import Product
from services.product import ProductService
# from app import api_key_required
# from app import CLIENT_API_KEYS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin 
from flask import send_from_directory
from models.question import Question

products_bp = Blueprint('products', __name__)
product_service = ProductService()


@products_bp.route('/products', methods=['GET'])
@cross_origin(supports_credentials=True)
# @jwt_required  
def products():    
    products = Product.query.all()
    product_list = []
    
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'image': product.image,
            'isActive': product.isActive
        }
        product_list.append(product_data)
    
    return jsonify({'products': product_list})

@products_bp.route('/assets/products/<filename>')
@cross_origin(supports_credentials=True)
def product_image(filename):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    return send_from_directory(os.path.join(base_dir, '../assets/products/'), filename)



