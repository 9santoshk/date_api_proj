from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

# app.py
CLIENT_API_KEYS = {
    'client_app_1': 'api_key_for_client_app_1',
    'client_app_2': 'api_key_for_client_app_2'
}

def create_app(config_name):
    app = Flask(__name__)

    # Load configuration based on config_name (e.g., 'development', 'production', etc.)
    app.config.from_object(configurations[config_name])

    # Initialize extensions with the app instance
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    from models.user import User
    from models.product import Product
    from models.question import Question 
    # with app.app_context():
    
    # cors.init_app(app)
    # CORS_ALLOW_ORIGIN="127.0.0.1:19006, localhost:19006"
    # CORS_EXPOSE_HEADERS="*,*"
    # CORS_ALLOW_HEADERS="content-type,*"
    # CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , 
    #             expose_headers= CORS_EXPOSE_HEADERS.split(","),   supports_credentials = True)


# app.py
    def before_request():
        # API Key validation before each request
        print(request.headers)
        api_key = request.headers.get('Authorization')
        print(api_key)
        if not api_key or api_key not in CLIENT_API_KEYS.values():
            return jsonify({"message": "Invalid API key"}), 401, {"Access-Control-Allow-Origin": "localhost:19006"}
        
    # app.before_request(before_request)

    # Import and register blueprints/routes here
    from routes.user import users_bp
    app.register_blueprint(users_bp)

    from routes.product import products_bp
    app.register_blueprint(products_bp)

    from routes.question import questions_bp
    app.register_blueprint(questions_bp)
    # @app.after_request
    # def after_request(response):
    #     print(response.headers)
    #     # response.headers.add('Access-Control-Allow-Origin', 'localhost:19006')
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    #     # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        # return response
    # app.after_request(after_request)

    return app


class BaseConfig:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = "postgresql://sk:sk@localhost/letsdate"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    CORS_SUPPORTS_CREDENTIALS=True
    supports_credentials=True
    CORS_HEADERS = 'Content-Type'
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

# app.py

configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    # Add more configurations as needed
}

from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()  # Verify that a valid JWT is in the request
        identity = get_jwt_identity()
        if identity.get('user_type') != 'admin':
            return jsonify(message='Admins only!'), 403
        return fn(*args, **kwargs)
    return wrapper