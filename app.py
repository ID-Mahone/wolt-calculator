from flask import Flask, request, jsonify
from datetime import datetime
from decimal import Decimal
import unittest

app = Flask(__name__)

def calculate_delivery_fee(cart_value, delivery_distance, numb_items, order_time):
    order_time = datetime.fromisoformat(order_time)
    

    # Fee for orders less than 10€
    small_order_charge = max(0, 10 - cart_value) if cart_value < 10 else 0

    # Simple Base fee
    base_fee = 2

    # Additional Fee every 500 meters above base_fee distance
    extra_fee = max(1, ((delivery_distance - 1000) // 500))

    # Bulk fee calculation and surcharge fee
    bulk_fee = 1.2 if numb_items > 12 else 1  
    item_surcharge = max(0, (numb_items - 5) * 0.5)

    # Friday rush fee
    rush_fee = 0
    if 15 <= order_time.hour <= 19 and order_time.weekday() == 4:
        rush_fee = min(15, (base_fee + extra_fee + item_surcharge + bulk_fee) * 1.2)

    # Free delivery for cart values > 200 Euro
    total_fee = Decimal(base_fee) + Decimal(extra_fee) + Decimal(item_surcharge) + Decimal(bulk_fee)
    if cart_value > 200:
        total_fee = Decimal(0)

    calculated_fee = total_fee + Decimal(small_order_charge) + Decimal(rush_fee)

    return round(calculated_fee, 2)  # Return fee in Euros, rounded to two decimal places

@app.route('/', methods=['GET', 'POST'])
def calculate_delivery_fee_api():
    try:
        if request.method == 'POST':
            data = request.get_json() 

            cart_value = float(data.get('cart_value', 0))
            delivery_distance = float(data.get('delivery_distance', 0))
            number_items = int(data.get('number_items', 0))
            order_time = data.get('time')

            delivery_fee = calculate_delivery_fee(cart_value, delivery_distance, number_items, order_time)

            return jsonify({'delivery_fee': delivery_fee})
        else:
            return jsonify({'message': 'This is a GET request. Use POST to calculate delivery fee.'})
    except (ValueError, KeyError) as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    unittest.main()
