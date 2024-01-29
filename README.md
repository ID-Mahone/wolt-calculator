# wolt-calculator

Introduction
This documentation provides an overview and explanation of the code implementing a delivery fee calculator using Flask, a micro web framework for Python. The calculator considers various factors such as cart value, delivery distance, number of items, and order time to determine the delivery fee.

Dependencies
Flask: A micro web framework for Python.
Decimal: Provides support for decimal floating-point arithmetic.
dateutil.parser: A module for parsing date strings into datetime objects.
logging: A standard module for logging messages from the application.
Function: calculate_delivery_fee
Purpose
Calculates the delivery fee based on input parameters.

Parameters
cart_value (float): Total value of items in the shopping cart.
delivery_distance (float): Distance in meters for delivery.
number_items (int): Number of items in the shopping cart.
order_time (str): Order time in string format.
Returns
calculated_fee (float): Rounded delivery fee in euros.
Fee Calculation
Small Order Charge: Fee applied for orders less than 10€.
Base Fee: A simple base fee of 2€.
Extra Fee: Additional fee for every 500 meters above 1000 meters in delivery distance.
Bulk Fee: A 20% surcharge for orders with more than 12 items.
Item Surcharge: Additional fee for orders with more than 5 items.
Friday Rush Fee: An extra fee for orders placed between 3 PM and 7 PM on Fridays.
Free Delivery: If the cart value is equal to or exceeds 200€, the delivery fee is set to zero.
Flask API: calculate_delivery_fee_api
Purpose
Exposes the delivery fee calculation functionality as a RESTful API using Flask.

Endpoints
GET /: Returns a message indicating that the endpoint only accepts POST requests.
POST /: Expects a JSON payload with the following parameters: cart_value, delivery_distance, number_items, and order_time. Returns the calculated delivery fee.
Input Validation
Ensures that input values (cart_value, delivery_distance, number_items) are non-negative.
Handles potential errors such as missing or incorrectly formatted input values.
Running the Application
If the script is executed directly (__name__ == '__main__'), the Flask application is run, and the API becomes accessible.

Conclusion
This code provides a flexible and customizable delivery fee calculation mechanism through a simple RESTful API. It considers various factors to determine the appropriate fee, providing a foundation for further customization and integration into larger systems.
