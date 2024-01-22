# app/services/user_service.py
from app.models.demo_model import User
from app import db

def get_all_users():
    users = User.query.all()
    return users

def create_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user
