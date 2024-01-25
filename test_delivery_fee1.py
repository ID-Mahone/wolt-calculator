import unittest
from flask import Flask, current_app
from app import app,calculate_delivery_fee_api

class TestDeliveryFeeCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_request(self):
        data = {
            'cart_value': 50,
            'delivery_distance': 1500,
            'number_items': 8,
            'time': '2024-01-25T12:30:00'
        }
        response = self.app.post('/', json=data)
        self.assertEqual(response.status_code, 200)
        result = response.get_json()
        self.assertIn('delivery_fee', result)

    def test_invalid_value_in_request(self):
        data = {
            'cart_value': 'invalid_value',
            'delivery_distance': 1500,
            'number_items': 8,
            'time': '2024-01-25T12:30:00'
        }
        response = self.app.post('/', json=data)
        self.assertEqual(response.status_code, 200)  # Assuming a generic error response for simplicity
        result = response.get_json()
        self.assertIn('error', result)

    def test_missing_key_in_request(self):
        data = {
            'cart_value': 50,
            'delivery_distance': 1500,
            'time': '2024-01-25T12:30:00'
        }
        response = self.app.post('/', json=data)
        self.assertEqual(response.status_code, 200)

        # Check for the absence of 'delivery_fee' key
        result = response.get_json()
        self.assertNotIn('error', result)

    def test_get_request(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        result = response.get_json()
        self.assertIn('message', result)
if __name__ == '__main__':
    unittest.main()
