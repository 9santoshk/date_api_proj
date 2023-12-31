import sys
sys.path.append('..')
from models.product import Product
from app import db

class ProductService:
    # def create_product(self, fullname, given_name, family_name, email, password, user_type, registered_on, picture, is_active):
    #     user = User(fullname=fullname,given_name=given_name,family_name=family_name
    #                 , email=email, password=password, user_type=user_type
    #                 , registered_on=registered_on, picture=picture, is_active=is_active)
    #     db.session.add(user)
    #     db.session.commit()
    #     return user

    def get_product_by_id(self, user_id):
        return Product.query.get(user_id)

    # def get_user_by_username(self, username):
    #     return User.query.filter_by(username=username).first()

    # def get_user_by_email(self, email):
    #     return User.query.filter_by(email=email).first()
