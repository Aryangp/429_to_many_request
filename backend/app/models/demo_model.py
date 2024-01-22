# app/models/user_model.py
from sqlalchemy import Column, Integer, String
from app import app, db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
