import sys
sys.path.append('..')
import datetime
from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.String(200), primary_key=False)
    product = db.Column(db.String(200), unique=False, nullable=False)
    ques = db.Column(db.String(200), unique=False, nullable=False)
    optiona = db.Column(db.String(200), unique=False, nullable=False)
    optionb = db.Column(db.String(200), unique=False, nullable=False)
    optionc = db.Column(db.String(200), unique=False, nullable=False)
    optiond = db.Column(db.String(200), unique=False, nullable=False)
    rightans = db.Column(db.String(200), unique=False, nullable=False)

    def __init__(self, productId, product, ques, optiona, optionb, optionc, optiond, rightans):
        self.productId = productId
        self.product = product
        self.ques = ques
        self.optiona = optiona
        self.optionb = optionb
        self.optionc = optionc
        self.optiond = optiond
        self.rightans = rightans

