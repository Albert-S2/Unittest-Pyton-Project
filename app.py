from flask import Flask, jsonify, request
from sdk.petstore_sdk import PetStoreSDK
from sdk.orders_sdk import OrderSDK

app = Flask(__name__)

# Initialize the SDKs
pet_sdk = PetStoreSDK('petstore_db.json')
order_sdk = OrderSDK('petstore_db.json')

# Pet routes
@app.route('/pets', methods=['GET'])
def get_pets():
    """Get all pets"""
    pets = pet_sdk.get_pets()
    return jsonify(pets), 200

@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """Get a pet by ID"""
    pet = pet_sdk.get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({"error": "Pet not found"}), 404

@app.route('/pets', methods=['POST'])
def add_pet():
    """Add a new pet"""
    new_pet = request.json
    pet_sdk.add_pet(new_pet)
    return jsonify(new_pet), 201

@app.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    """Update a pet"""
    new_data = request.json
    pet_sdk.update_pet(pet_id, new_data)
    return jsonify(new_data), 200

@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    """Delete a pet"""
    pet_sdk.delete_pet(pet_id)
    return jsonify({"message": "Pet deleted"}), 204

# Order routes
@app.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders"""
    orders = order_sdk.get_orders()
    return jsonify(orders), 200

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get an order by ID"""
    order = order_sdk.get_order_by_id(order_id)
    if order:
        return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404

@app.route('/orders', methods=['POST'])
def add_order():
    """Add a new order"""
    new_order = request.json
    order_sdk.add_order(new_order)
    return jsonify(new_order), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an order"""
    new_data = request.json
    order_sdk.update_order(order_id, new_data)
    return jsonify(new_data), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order"""
    order_sdk.delete_order(order_id)
    return jsonify({"message": "Order deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
