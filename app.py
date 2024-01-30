from flask import Flask, request, jsonify
from decimal import Decimal
from dateutil import parser
import logging

app = Flask(__name__)


def calculate_delivery_fee(cart_value, delivery_distance, number_items, order_time):
    order_time = parser.parse(order_time)

    # Fee for orders less than 10€
    small_order_charge = max(0, 10 - cart_value) if cart_value < 10 else 0

    # Simple Base fee.
    base_fee = 2

    # Additional Fee every 500 meters above base_fee distance.
    extra_fee = max(0, ((delivery_distance - 1000) // 500))

    # Bulk fee calculation and surcharge fee.
    bulk_fee = 1.2 if number_items > 12 else 0
    item_surcharge = max(0, (number_items - 5) * 0.5)

    # Friday rush fee
    rush_fee = 0
    if 15 <= order_time.hour <= 19 and order_time.weekday() == 3:
        rush_fee = min(15, (base_fee + extra_fee +
                       item_surcharge + bulk_fee) * 1.2)

    # Free delivery for cart values >= 200 EUR.
    total_fee = Decimal(base_fee) + Decimal(extra_fee) + \
        Decimal(item_surcharge) + Decimal(bulk_fee)
    if cart_value >= 200:
        total_fee = Decimal(0)

    calculated_fee = total_fee + \
        Decimal(small_order_charge) + Decimal(rush_fee)

    # Return fee in EUR, rounded to two decimal places.
    return round(calculated_fee, 2)


@app.route('/', methods=['GET', 'POST'])
def calculate_delivery_fee_api():
    try:
        if request.method == 'POST':
            data = request.get_json()

            # Ensure correct input values
            cart_value = float(data.get('cart_value', 0))
            delivery_distance = float(data.get('delivery_distance', 0))
            number_items = int(data.get('number_items', 0))
            order_time = data.get('order_time')

            if cart_value < 0 or delivery_distance < 0 or number_items < 0:
                return jsonify({'error': 'Only positive input values'})

            delivery_fee = calculate_delivery_fee(
                cart_value, delivery_distance, number_items, order_time)

            return jsonify({'delivery_fee': delivery_fee})
        else:
            return jsonify({'message': 'This is a GET request. Use POST to calculate delivery fee.'})
    except (ValueError, KeyError) as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()

#   .--.
#  |o_o |
#  |    |
# //   \ \
# (|     | )
# \ /^\ /
#  \\|_|
#  /____\
# "I hope you had a good time reviewing my code, sir"

