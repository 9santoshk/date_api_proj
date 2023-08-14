import sys
sys.path.append('..')
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import CheckConstraint

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
    gender = db.Column(db.String(120), unique=False, nullable=True, default=None)
    education = db.Column(db.String(120), unique=False, nullable=True, default=None)
    income = db.Column(db.String(120), unique=False, nullable=True, default=None)
    occupation = db.Column(db.String(120), unique=False, nullable=True, default=None)
    dob = db.Column(db.Date, unique=False, nullable=True, default=None)
    age = db.Column(db.Integer, unique=False, nullable=True, default=None)

    def __init__(self, fullname,given_name,family_name, email, password, 
                 user_type, registered_on, picture, is_active, gender, education,
                 income, occupation, age, dob):
        self.fullname = fullname
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        self.set_password(password)
        self.user_type = user_type
        self.registered_on = registered_on
        self.picture = picture
        self.is_active = is_active
        self.gender = gender
        self.education  = education 
        self.income = income
        self.occupation = occupation
        self.age = age
        self.dob = dob 

    def set_password(self, password):
        # You can use a secure password hashing mechanism like bcrypt or Werkzeug's security helpers
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    __table_args__ = (
        CheckConstraint(gender.in_([None, "Male", "Female", "Other"])),
    )
    __table_args__ = (
        CheckConstraint(occupation.in_([None, "Employed", "Unemployed", "Housewife", "Student"])),
    )
    
    __table_args__ = (
        CheckConstraint(education.in_([None, "Illiterate", "High School", "Graduate",
                                       "Post graduate", "Doctorate"])),
    )

    __table_args__ = (
        CheckConstraint(income.in_([None,"< 1L", "1-3 L", "3-5 L",
                                       "5-10 L", "10-20 L", "20 - 50 L", "> 50 L"])),
    )
    
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
            'education': self.education,
            'occupation': self.occupation,
            'age': self.age,
            'gender': self.gender,
            'dob': self.dob,
            # Include other fields as needed
        }

# code to inset sample users 
