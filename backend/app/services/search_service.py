# app/service/search_service.py
from flask import jsonify, request
from app import app, controllers
from app.utils.common_utils import validate_json


# Example request body:
# {
#     "query": "a black shoes with a white sole and sports shoes",
#     "filters":{
#         "category": "shoes",
#         "color": "black",
#         "style": "sports",
#         "sole": "white",
#         "brand": "nike"
#     }
# }


@app.route('/search/query', methods=['POST'])
@validate_json(['query', 'filters'])
def search_catalog():
    data = request.get_json()
    try:
        search_result = controllers.search_controller(data['query'], data['filters'])
    except Exception as e:
        return jsonify({'error': str(e)}), 400    
    
    return jsonify(search_result.__dict__), 201


# Example request body:
# data={
#   "unique_id": "user123",
#   "product_id": "P123",
#   "product_desc": "male running shoes comfortable soeul and nice design",
#   "category": "Shoes",
#   "sub_category": "running",
#   "product_type": "footware",
#   "color": "Black",
#   "usage": "Sports",
#   "product_title": "CR7 predator"
# }


@app.route('/add/querydata', methods=['POST'])
@validate_json(['unique_id', 'product_id', 'product_desc', 'category', 'sub_category', 'product_type', 'color', 'usage', 'product_title'])
def add_data_to_database():
    data = request.get_json()
    try:
        search_result = controllers.add_data_controller(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400    
    
    return "data added successfully ", 201
