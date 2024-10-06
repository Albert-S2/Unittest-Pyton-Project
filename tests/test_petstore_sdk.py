import unittest
import json
from sdk.petstore_sdk import PetStoreSDK

class TestPetStoreSDK(unittest.TestCase):


# SAMPLE DATA


# Example data for my test database (Pets)
    @classmethod
    def setUpClass(cls):
        cls.db_file = 'test_petstore_db.json'
        sample_data = {
            "pets": [
                {"id": 1, "name": "Creed", "category": {"id": 1, "name": "Dog"}, "photoUrls": [], "tags": [], "status": "available"},
                {"id": 2, "name": "Rocky", "category": {"id": 2, "name": "Cat"}, "photoUrls": [], "tags": [], "status": "available"}
            ]
        }
        with open(cls.db_file, 'w') as f:
            json.dump(sample_data, f)

# Test database file to be deleted after test is completed
    @classmethod
    def tearDownClass(cls):
        import os
        os.remove(cls.db_file)




# AUTHENTICATION KEY TEST


# Authentication Key test (dummy key used)
    def test_authentication_success(self):
        sdk = PetStoreSDK(self.db_file, auth_key="special-key")
        pets = sdk.get_pets()
# Test should provide 2 positions as per sample data 
        self.assertEqual(len(pets), 2)  

# In this test we will receive error if wrong key has been used
    def test_authentication_failure(self):
        sdk = PetStoreSDK(self.db_file, auth_key="wrong-key")
        with self.assertRaises(PermissionError):
            sdk.get_pets()




# GET PETS TEST


# In this test we will check if we can get all the pets from database
    def test_get_pets(self):
        sdk = PetStoreSDK(self.db_file, auth_key="special-key")
        pets = sdk.get_pets()
        self.assertEqual(len(pets), 2)




# ADD NEW PET TEST


# In this test we will check if we can add new pet
    def test_add_pet(self):
        sdk = PetStoreSDK(self.db_file, auth_key="special-key")
        new_pet = {"id": 3, "name": "Cesar", "category": {"id": 1, "name": "Dog"}, "photoUrls": [], "tags": [], "status": "available"}
        sdk.add_pet(new_pet)
        
# When new pet added successfully, there should be now 3 pets in database
        pets = sdk.get_pets()
        self.assertEqual(len(pets), 3)

# New pet has to be deleted immediately as it may affect following tests
        sdk.delete_pet(3)

# After deleting, we check if it's back to 2 pets
        pets_after_deletion = sdk.get_pets()
        self.assertEqual(len(pets_after_deletion), 2)




# UPDATE PET TEST


# This test will check if we can update pet
    def test_update_pet(self):
        sdk = PetStoreSDK(self.db_file, auth_key="special-key")
        
# First I will add a new pet to update
        new_pet = {"id": 3, "name": "Cesar", "category": {"id": 1, "name": "Dog"}, "photoUrls": [], "tags": [], "status": "available"}
        sdk.add_pet(new_pet)

# Update pet's name
        updated_pet = {"id": 3, "name": "Julius Cesar", "category": {"id": 1, "name": "Dog"}, "photoUrls": [], "tags": [], "status": "available"}
        sdk.update_pet(updated_pet)

# Get updated pet's name to check if it is correct
        pets = sdk.get_pets()
        updated_pet_from_db = next(pet for pet in pets if pet["id"] == 3)
        self.assertEqual(updated_pet_from_db["name"], "Julius Cesar")




# DELETE PET TEST


# In this test we will add and the delete pet from database
    def test_delete_pet(self):
        sdk = PetStoreSDK(self.db_file, auth_key="special-key")
        
# First I will add a new pet to delete
        new_pet = {"id": 4, "name": "Wednesday", "category": {"id": 1, "name": "Dog"}, "photoUrls": [], "tags": [], "status": "available"}
        sdk.add_pet(new_pet)

# Then, let's delete new pet from the database
        sdk.delete_pet(4)

# Check if the pet is deleted (back to 2 pets)
        pets = sdk.get_pets()
        self.assertEqual(len(pets), 2)



# Now tests have to executed when the script is run from the terminal:
# >>> python3 -m unittest discover <<<

if __name__ == '__main__':
    unittest.main()
