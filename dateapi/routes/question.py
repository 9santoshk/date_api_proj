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
from services.question import QuestionService

questions_bp = Blueprint('questions', __name__)
question_service = QuestionService()

@questions_bp.route('/questions', methods=['GET'])
@cross_origin(supports_credentials=True)
# @jwt_required  
def productsQues():
    productId = request.args.get('productId')
    print(productId)
    prodques = Question.query.filter_by(productId=productId).all()
    ques_list = []
    
    for ques in prodques:
        ques_data = {
            'id': ques.id,
            'productId': ques.productId,
            'product': ques.product,
            'ques': ques.ques,
            'optiona': ques.optiona,
            'optionb': ques.optionb,
            'optionc': ques.optionc,
            'optiond': ques.optiond,
            'rightans': ques.optiona,
        }
        ques_list.append(ques_data)
    
    return jsonify({'questions': ques_list})
