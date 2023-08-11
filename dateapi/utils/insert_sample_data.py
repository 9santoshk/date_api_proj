import sys
sys.path.append('..')
from app import db
from models.user import User
from models.product import Product
from models.question import Question
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# users
def create_user_data():
    # print('Creating')
    db.session.add(User('admin k','admin','k', 'admin@example.com',generate_password_hash('123456')
                        ,'admin',datetime.datetime.now(),'../assets/profile_pics/csk.jpg',True))
    db.session.add(User('guest k','guest','k', 'guest@example.com',generate_password_hash('123456')
                        ,'normal',datetime.datetime.now(),'../assets/profile_pics/dsk.jpg',True))
    db.session.commit()

# products
def create_product_data():
    db.session.add(Product('Saving Bank Account','Saving', 'Saving from income','saving.jpg',True))
    db.session.add(Product('Stock Market','Investment', 'Share market investment','shares.jpg',True))
    db.session.add(Product('Health/vehicle insurance','Insurance', 'Insure family and weath','insurance.jpg',True))
    db.session.add(Product('Credit Cards','Credit Cards', 'For daily transactions','creditcard.jpg',True))
    db.session.add(Product('Car/House Loans','Loans', 'For buying assets','loans.jpg',True))
    db.session.commit()

# ques
def create_question_data():
    db.session.add(Question('1','Saving', 'what Saving from income','optiona','optionb','optionc','optiond','optiona'))
    db.session.add(Question('1','Saving', 'what do you save','optiona','optionb','optionc','optiond','optiona'))
    db.session.add(Question('2','Investment', 'how much wealth','optiona','optionb','optionc','optiond','optiona'))
    db.session.add(Question('2','Investment', 'how much investment','optiona','optionb','optionc','optiond','optiona'))
    db.session.add(Question('3','Insurance', 'do you have ins','optiona','optionb','optionc','optiond','optiona'))
    db.session.commit()

