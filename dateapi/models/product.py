import sys
sys.path.append('..')
import datetime
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    category = db.Column(db.String(200), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=False)
    image = db.Column(db.String(200), unique=False, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, name, category, description, image, isActive):
        self.name = name
        self.category = category
        self.description = description
        self.image = image
        self.isActive = isActive

