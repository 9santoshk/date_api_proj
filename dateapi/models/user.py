import sys
sys.path.append('..')
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(64), unique=False, nullable=False)
    given_name = db.Column(db.String(64), unique=False, nullable=False)
    family_name = db.Column(db.String(64), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.String(64), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    picture = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, nullable=False)

    def __init__(self, fullname,given_name,family_name, email, password, user_type, registered_on, picture, is_active):
        self.fullname = fullname
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        self.set_password(password)
        self.user_type = user_type
        self.registered_on = registered_on
        self.picture = picture
        self.is_active = is_active

    def set_password(self, password):
        # You can use a secure password hashing mechanism like bcrypt or Werkzeug's security helpers
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'given_name': self.given_name,
            'family_name': self.family_name,
            'email': self.email,
            'user_type': self.user_type,
            'registered_on': self.registered_on,
            'picture': self.picture,
            'is_active': self.is_active,
            # Include other fields as needed
        }

# code to inset sample users 
