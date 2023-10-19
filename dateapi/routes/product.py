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
from app import admin_required

products_bp = Blueprint('products', __name__)
product_service = ProductService()


@products_bp.route('/products', methods=['GET'])
@cross_origin(supports_credentials=True)
# @jwt_required()
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


@products_bp.route('/edit_product/<int:product_id>', methods=['PUT'])
# @jwt_required  # Require JWT authentication
@admin_required
@cross_origin(supports_credentials=True)
def edit_product(product_id):
    current_user = get_jwt_identity()
    if current_user.get('user_type') != 'admin':
        return jsonify({'message': 'You do not have permission to edit products'}), 403

    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.description = data.get('description', product.description)
    product.image = data.get('image', product.image)
    product.isActive = data.get('isActive', product.isActive)

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'}), 200



