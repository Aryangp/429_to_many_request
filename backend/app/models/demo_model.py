# app/models/user_model.py
import weaviate
from sqlalchemy import Column, Integer, String
from app import app, db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


def create_weaviate_client():
    auth_config = weaviate.AuthApiKey(api_key="6jxVgqxJGKOEYjZKNn7YZ5FryuZITj6mSNzJ")

    client = weaviate.Client(
        url="https://catalog-indexing-158090jd.weaviate.network",
        auth_client_secret=auth_config,
        
    )

    return client


def create_schema(client):
    class_obj = {
        "class": "Question",
        "vectorizer": "text2vec-openai",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
        "moduleConfig": {
            "text2vec-openai": {},
            "generative-openai": {}  # Ensure the `generative-openai` module is used for generative queries
        }
    }

    client.schema.create_class(class_obj)