# app/utils/common_utils.py
from functools import wraps
from flask import request, jsonify

def validate_json(required_fields):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return jsonify({'error': 'Invalid JSON format'}), 400

            data = request.get_json()
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

            return func(*args, **kwargs)

        return wrapper

    return decorator
