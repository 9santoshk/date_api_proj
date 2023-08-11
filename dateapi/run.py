# run.py

from app import create_app
from app import db

if __name__ == '__main__':
    app = create_app('development')  # Change 'development' to the desired configuration

    with app.app_context():
        db.drop_all()
        db.create_all()
        
        from utils.insert_sample_data import create_user_data, create_product_data, create_question_data
        create_user_data()
        create_product_data()
        create_question_data()

        app.run(debug=True)
        
