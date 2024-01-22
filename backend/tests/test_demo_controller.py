import unittest
from flask import Flask, jsonify
from app import app, db
from app.controllers.user_controller import get_users, create_user
from app.models.user_model import User

class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_users(self):
        # Test the /users endpoint for retrieving users
        response = self.app.get('/users')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data)

    def test_create_user(self):
        # Test the /users endpoint for creating a new user
        user_data = {'name': 'Test User', 'email': 'test@example.com'}
        response = self.app.post('/users', json=user_data)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data)
        self.assertEqual(data['name'], user_data['name'])
        self.assertEqual(data['email'], user_data['email'])

        # Verify that the user is stored in the database
        user = User.query.filter_by(email=user_data['email']).first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, user_data['name'])

if __name__ == '__main__':
    unittest.main()
