import unittest
import json
from app import app

class CurrencyConverterTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        """Test if the index page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Currency Converter', response.data)

    def test_convert_valid_currency(self):
        """Test currency conversion with valid data."""
        data = {
            'base_currency': 'USD',
            'target_currency': 'EUR',
            'amount': 100
        }
        response = self.app.post('/convert', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('converted_amount', response.get_json())

    def test_convert_invalid_currency(self):
        """Test currency conversion with invalid data."""
        data = {
            'base_currency': 'USD',
            'target_currency': 'INVALID',
            'amount': 100
        }
        response = self.app.post('/convert', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()


