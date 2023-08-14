import sys, os
sys.path.append('..')
from flask import Blueprint, jsonify, request
import datetime
from app import db
import logging
from services.user import UserService
# from app import api_key_required
# from app import CLIENT_API_KEYS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin 

users_bp = Blueprint('users', __name__)
user_service = UserService()

@users_bp.route('/')
def home():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    return f'Base Directory: {base_dir}'

# @users_bp.route('/users', methods=['GET'])
# def get_all_users():
#     users = user_service.get_all_users()
#     user_list = [user.to_dict() for user in users]
#     return jsonify(user_list)

# @users_bp.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = user_service.get_user_by_id(user_id)
#     if user:
#         return jsonify(user.to_dict())
#     return jsonify(error='User not found'), 404

@users_bp.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
# @jwt_required  
def login():    
    data = request.get_json()
    # print(request.data, file=sys.stderr)
    fullname = data.get('fullname')
    given_name = data.get('given_name')
    family_name = data.get('family_name')
    email = data.get('email')
    password = '123456'
    user_type = 'normal'
    registered_on = datetime.datetime.now()
    picture = data.get('picture')
    is_active = True
    print(request.data)
    if not email:
        return jsonify(error='Missing required fields'), 400

    existing_user = user_service.get_user_by_email(email)
    if existing_user:
        return jsonify(existing_user.to_dict()), 200

    new_user = user_service.create_user(fullname,given_name,family_name, email
                                        ,password, user_type, registered_on,picture, is_active
                                        ,None,None,None,None,None,datetime.date(1990, 5, 15))
    
    access_token = create_access_token(identity=email)
    response = jsonify({'logintoken': access_token})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response

    return response, 201

    # return jsonify(new_user.to_dict()), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
# @jwt_required
def update_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify(error='User not found'), 404

    data = request.get_json()
    fullname = data.get('fullname')
    given_name = data.get('given_name')
    family_name = data.get('family_name')
    email = data.get('email')
    password = data.get('password')
    user_type = data.get('user_type')
    registered_on = data.get('registered_on')
    picture = data.get('picture')
    is_active = data.get('is_active')
    gender = data.get('gender')
    education = data.get('education')
    income = data.get('income')
    occupation = data.get('occupation')
    age = data.get('age')
    dob = data.get('dob')

    if not email:
        return jsonify(error='Missing required fields'), 400
    
    user.fullname = fullname
    user.given_name = given_name
    user.family_name = family_name
    user.email = email
    user.set_password(password)
    user.user_type = user_type
    user.registered_on = registered_on
    user.picture = picture
    user.is_active = is_active
    user.gender = gender
    user.education  = education 
    user.income = income
    user.occupation = occupation
    user.age = age
    user.dob = dob 

    db.session.commit()

    return jsonify(user.to_dict())

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
# @jwt_required
def delete_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify(error='User not found'), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify(message='User deleted')
