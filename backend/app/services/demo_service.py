# app/controllers/user_controller.py
from flask import jsonify, request
from app import app, controllers
from app.models.demo_model import User
from app.utils.common_utils import validate_json

@app.route('/users', methods=['GET'])
def get_users():
    users = controllers.get_all_users()
    return jsonify([user.__dict__ for user in users])

@app.route('/users', methods=['POST'])
@validate_json(['name', 'email'])
def create_user():
    data = request.get_json()
    user = controllers.create_user(data['name'], data['email'])
    return jsonify(user.__dict__), 201
