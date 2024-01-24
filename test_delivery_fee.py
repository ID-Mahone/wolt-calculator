import unittest
from datetime import datetime
from app import calculate_delivery_fee

class CalculatorTest(unittest.TestCase):

    def test_delivery_fee(self):
        # Test1: Small value, short distance, few items
        result = calculate_delivery_fee(500.0, 800, 3, "2024-01-15T12:00:00Z")
        self.assertEqual(result, 0)  # Expected delivery fee: 0 Euro

        # Test2: Large value, long distance, many items, Friday rush
        result = calculate_delivery_fee(2500.0, 3000, 15, "2024-01-17T16:30:00Z")
        self.assertEqual(result, 1080)  # Expected delivery fee: 10.80 Euro

        # Test3: High order value == free delivery
        result = calculate_delivery_fee(25000.0, 1200, 8, "2024-01-18T10:00:00Z")
        self.assertEqual(result, 0)  # Expected delivery fee: 0 Euro
if __name__ == '__main__':
    unittest.main()
