import unittest
from app import calculate_delivery_fee

class CalculatorTest(unittest.TestCase):

#cart_value, delivery_distance, numb_items, order_time
    def test_delivery_fee(self):
        #Test1: Small value, short distance, few items
        result = calculate_delivery_fee(5, 800, 3,"2024-01-15T12:00:00Z")
        self.assertEqual(result, 7.00) 

if __name__ == '__main__':
    unittest.main()
