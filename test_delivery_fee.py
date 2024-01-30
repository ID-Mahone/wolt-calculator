import unittest
from app import calculate_delivery_fee
from decimal import Decimal


class CalculatorTest(unittest.TestCase):
    def test_delivery_fee(self):
        # Test1: Small value, short distance, few items (7€ expected)
        # cart_value, delivery_distance, number_items, order_time
        result = calculate_delivery_fee(5, 800, 3, "2024-01-15T12:00:00Z")
        self.assertEqual(result, Decimal('7.00'))

        # Test2: Large value, long distance, many items, friday_rush (12.20€ expected)
        result = calculate_delivery_fee(80, 3000, 15, "2024-01-19T16:30:00Z")
        self.assertEqual(result, Decimal('12.20'))

        # Test3: >= 200 == free delivery (0€ expected)
        result = calculate_delivery_fee(250000, 800, 3, "2024-01-15T12:00:00Z")
        self.assertEqual(result, Decimal('0.00'))

        # Test4:Order value exactly 10 euro / surcharge check (2.00€ expected)
        result = calculate_delivery_fee(10, 800, 3, "2024-01-15T12:00:00Z")
        self.assertEqual(result, Decimal('2.00'))

        # Test5:Exactly 12 euro / bulkfee check (10.50€ expected)
        result = calculate_delivery_fee(5, 800, 12, "2024-01-15T12:00:00Z")
        self.assertEqual(result, Decimal('10.50'))


if __name__ == '__main__':
    unittest.main()
