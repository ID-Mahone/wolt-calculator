<img src="./logo-wolt.png" />


# Delivery Fee Calculator

## Overview

This Flask-based API application calculates the delivery fee based on input parameters such as cart value, 
delivery distance, number of items, and order time.

It is part of the [Wolt Summer 2024 Engineering Internships](https://github.com/woltapp/engineering-internship-2024).

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- dateutil

### Installation

1. Clone the repository:

```bash
git clone <https://github.com/ID-Mahone/wolt-calculator>
```

### Install dependencies

```bash
pip install flask python-dateutil
```

### Run the application

```bash
python app.py
```

The API will be accessible via `http://127.0.0.1:5000`

### API Endpoint

#### Request

- POST /
- Content-Type: application/json
- Request Body
```json
{
    "cart_value": 0,
    "delivery_distance": 0,
    "number_items": 0,
    "order_time": "0000-00-00T00:00:00Z"
}
```

#### Response
- Content-Type: application/json
- Response JSON
```json
{
    "delivery_fee": 00.00
}
```

### Delivery Fee Calculation 

The `calculate_delivery_fee` function in app.py performs the delivery fee calculation based on the provided input parameters.

#### Input Parameters

- cart_value (float): The total value of the items in the shopping cart.
- delivery_distance (float): The distance (in meters) to the delivery location.
- number_items (int): The total number of items in the shopping cart.
- order_time (str): The timestamp of the order in ISO 8601 format (e.g., "2024-01-19T16:30:00Z").

#### Output

The function returns the calculated delivery fee as a decimal rounded to two decimal places.

### Test

The `CalculatorTest` class in [test_delivery_fee.py](./test_delivery_fee.py) contains unit tests to verify the correctness 
of the delivery fee calculation function.

#### Test Cases

- Small value, short distance, few items (Expected: 7.00).
- Large value, long distance, many items, Friday rush (Expected: 12.20).
- Cart value >= 200 (Expected: 0.00 - Free delivery).
- Order value exactly 10 euro (Expected: 2.00 - Surcharge check).
- Order value exactly 12 euro (Expected: 10.50 - Bulk fee check).

#### Running Test

```bash
python -m unittest test_delivery_fee.py
```

### Error Handling

The API handles potential errors such as invalid input values or missing parameters. If an error occurs during the calculation, an error response with a relevant message is returned.

### Conclusion

This delivery fee calculator API provides a simple and flexible solution for calculating the delivery fee based on various factors. It is important to ensure that valid input parameters are provided for accurate results.

## Author

David Manning

## License

MIT