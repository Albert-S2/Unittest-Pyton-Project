import json

class OrderSDK:
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

    def get_orders(self):
        self.check_auth()
        return self.data.get("orders", [])

    def add_order(self, order):
        self.check_auth()
        # Add order implementation...
        self.data['orders'].append(order)
        self.save_data()

    def update_order(self, updated_order):
        self.check_auth()
        # Find and update the order
        for index, order in enumerate(self.data["orders"]):
            if order["id"] == updated_order["id"]:
                self.data["orders"][index] = updated_order
                self.save_data()
                return
        raise ValueError("Order with id {} not found.".format(updated_order["id"]))

    def delete_order(self, order_id):
        self.check_auth()
        # Find and delete the order
        for index, order in enumerate(self.data["orders"]):
            if order["id"] == order_id:
                del self.data["orders"][index]
                self.save_data()
                return
        raise ValueError("Order with id {} not found.".format(order_id))


    def save_data(self):
        # Save data back to the JSON file
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file)
