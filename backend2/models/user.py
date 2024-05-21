from middleware.pasql_mid import Base
from sqlalchemy import Column,String,Integer, ForeignKey

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


class WeaviateData(Base):
    __tablename__="weaviate_data"

    id = Column(Integer, primary_key=True, index=True)
    className = Column(String)
    user_id=Column(ForeignKey("users.id"))
