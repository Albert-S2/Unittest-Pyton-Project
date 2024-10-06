# Petstore API Unittest/Python Project
A Python project for testing the Petstore API using SDKs and `Unittest` framework.

## Overview
This project is about creating unit tests for the Petstore API using Python SDKs and the `unittest` framework. Instead of sending live API requests, it uses a JSON file to mimic the API responses. This approach helps create consistent and controlled testing situations.

## Features
- Unit tests for CRUD operations on the Petstore API
- Uses Python's `unittest` framework
- Automated testing of API responses, status codes, and data validation

## Technologies
- Python 3.9
- `unittest` for unit testing
- Python SDK for Petstore API
- JSON file to simulate API requests

## Tests
Tests are organized to cover the following **CRUD** operations:

- **Create**: Testing POST requests to create new **pets/order**.
- **Read**: Testing GET requests to retrieve **pet/order details**.
- **Update**: Testing PUT requests to modify **pet/order** data.
- **Delete**: Testing DELETE requests to remove **pets/order** from the database.

## Installation & usage:
1. Clone the repository:
```bash
git clone https://github.com/yourusername/petstore-api-unittest.git
```
2. Navigate to the project directory
```plaintext
Unittest-Python-Project/
├── tests/
│   ├── test_orders_sdk.py
│   └── test_petstore_sdk.py
```
3. To run all the tests, use the following command:
```bash
python -m unittest discover
```
