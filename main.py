from sdk.petstore_sdk import PetStoreSDK
from sdk.orders_sdk import OrderSDK

# Initialize the SDKs with the path to the JSON file
pet_sdk = PetStoreSDK('petstore_db.json')
order_sdk = OrderSDK('petstore_db.json')

# Get all pets
all_pets = pet_sdk.get_pets()
print("All Pets:", all_pets)

# Get a pet by ID
pet = pet_sdk.get_pet_by_id(1)
print("Pet with ID 1:", pet)

# Add a new pet
new_pet = {
    "id": 3,
    "name": "Bella",
    "category": {"id": 101, "name": "Dog"},
    "photoUrls": ["https://example.com/photos/bella1.jpg"],
    "tags": [{"id": 205, "name": "energetic"}],
    "status": "available"
}
pet_sdk.add_pet(new_pet)

# Add a new order
new_order = {
    "id": 303,
    "petId": 1,
    "quantity": 1,
    "shipDate": "2024-10-05T16:00:00Z",
    "status": "pending",
    "complete": False
}
order_sdk.add_order(new_order)

# Print updated data
print("Updated Pets:", pet_sdk.get_pets())
print("Updated Orders:", order_sdk.get_orders())
