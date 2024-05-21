# # run.py
# from flask import Flask, jsonify, request
# from routes.search import search_query
# from routes.weaviateSetUp import weaviate_add_data,weaviate_create_schema
# from utils.jsonValidator import validate_json
# from flask_cors 


from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from middleware.pasql_mid import SessionLocal, engine, Base
from routes.search import router as search_router
from routes.auth import router as auth_router
from routes.weaviateSetUp import router as weaviate_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(search_router)
app.include_router(auth_router)
app.include_router(weaviate_router)























# # Create the application instance
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})



# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'message': 'Welcome to the search engine'}), 200


# @app.route('/search', methods=['POST'])
# @validate_json(['query','className'])
# def search():
#     try:
#         search_result = search_query(request)
#         return jsonify(search_result) , 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400
    
# @app.route("/weaviate/schema",methods=['POST'])
# @validate_json(['className','properties'])
# def weaviate_schema():
#     try:
#         creation_result = weaviate_create_schema(request)
#         return creation_result
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400    
    
    
# @app.route("/add/data",methods=['POST'])
# def add_data():
#     try:
#         add_result = weaviate_add_data(request)
#         return add_result
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400


# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run(host='0.0.0.0',port=5000)  
