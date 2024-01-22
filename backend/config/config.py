# config/config.py
from flask_sqlalchemy import SQLAlchemy

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
