import json

class PetStoreSDK:
    def __init__(self, db_file, auth_key=None):
        self.db_file = db_file
        self.auth_key = auth_key
        self.data = self.load_data()

    def load_data(self):
        # Load data from the JSON file
        with open(self.db_file, 'r') as file:
            return json.load(file)

    def check_auth(self):
        if self.auth_key != "special-key":
            raise PermissionError("Invalid authentication key.")

    def get_pets(self):
        self.check_auth()
        return self.data.get("pets", [])

    def add_pet(self, pet):
        self.check_auth()
        self.data['pets'].append(pet)
        self.save_data()

    def update_pet(self, updated_pet):
        self.check_auth()
        # Find and update the pet
        for index, pet in enumerate(self.data["pets"]):
            if pet["id"] == updated_pet["id"]:
                self.data["pets"][index] = updated_pet
                self.save_data()
                return  # Exit once the pet is updated
        raise ValueError("Pet with id {} not found.".format(updated_pet["id"]))

    def delete_pet(self, pet_id):
        self.check_auth()
        # Find and delete the pet
        for index, pet in enumerate(self.data["pets"]):
            if pet["id"] == pet_id:
                del self.data["pets"][index]
                self.save_data()
                return  # Exit once the pet is deleted
        raise ValueError("Pet with id {} not found.".format(pet_id))

    def save_data(self):
        # Save data back to the JSON file
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file)
