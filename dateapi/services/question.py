import sys
sys.path.append('..')
from models.question import Question
from app import db

class QuestionService:
    # def create_product(self, fullname, given_name, family_name, email, password, user_type, registered_on, picture, is_active):
    #     user = User(fullname=fullname,given_name=given_name,family_name=family_name
    #                 , email=email, password=password, user_type=user_type
    #                 , registered_on=registered_on, picture=picture, is_active=is_active)
    #     db.session.add(user)
    #     db.session.commit()
    #     return user

    def get_question_by_id(self, qid):
        return Question.query.get(qid)

    # def get_user_by_username(self, username):
    #     return User.query.filter_by(username=username).first()

    # def get_user_by_email(self, email):
    #     return User.query.filter_by(email=email).first()
