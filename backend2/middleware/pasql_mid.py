from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define your database models here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    # Add other fields as needed

class WeavaiteClassData(Base):
    __tablename__ = "weavaite_class_data"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, unique=True, index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    # Add other fields as needed


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:aryangp@127.0.0.1:5432/weavaiteuserdata"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)