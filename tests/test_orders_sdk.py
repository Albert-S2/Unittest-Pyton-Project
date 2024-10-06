import unittest
import json
from sdk.orders_sdk import OrderSDK

class TestOrderSDK(unittest.TestCase):
    

# SAMPLE DATA


# Example data for my test database (Orders)
    @classmethod
    def setUpClass(cls):
        cls.db_file = 'test_orders_db.json'
        sample_data = {
            "orders": [
                {"id": 1, "petId": 1, "quantity": 1, "shipDate": "2024-10-05T16:00:00Z", "status": "pending", "complete": False},
                {"id": 2, "petId": 2, "quantity": 1, "shipDate": "2024-10-05T16:00:00Z", "status": "shipped", "complete": True}
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
        sdk = OrderSDK(self.db_file, auth_key="special-key")
        orders = sdk.get_orders()
# Test should provide 2 positions as per sample data         
        self.assertEqual(len(orders), 2)

# In this test we will receive error if wrong key has been used
    def test_authentication_failure(self):
        sdk = OrderSDK(self.db_file, auth_key="wrong-key")
        with self.assertRaises(PermissionError):
            sdk.get_orders()



# GET ORDERS TEST


# In this test we will check if we can get all the orders from database
    def test_get_orders(self):
        sdk = OrderSDK(self.db_file, auth_key="special-key")
        orders = sdk.get_orders()
        self.assertEqual(len(orders), 2)




# ADD ORDER TEST


# In this test we will check if we can add new order
    def test_add_order(self):
        sdk = OrderSDK(self.db_file, auth_key="special-key")
        new_order = {"id": 3, "petId": 1, "quantity": 1, "shipDate": "2024-10-05T16:00:00Z", "status": "pending", "complete": False}
        sdk.add_order(new_order)
        
# When we add new order, we should have 3 orders in total
        orders = sdk.get_orders()
        self.assertEqual(len(orders), 3)

# New order has to be deleted immediately as it may affect following tests
        sdk.delete_order(3)

# After deleting, we check if it's back to 2 orders
        orders_after_deletion = sdk.get_orders()
        self.assertEqual(len(orders_after_deletion), 2)  # Should be back to 2 orders




# UPDATE ORDER TEST


# In this test we will check if we can update an order
    def test_update_order(self):
        sdk = OrderSDK(self.db_file, auth_key="special-key")
        
# First I will add new order to update
        new_order = {"id": 3, "petId": 1, "quantity": 1, "shipDate": "2024-10-05T16:00:00Z", "status": "pending", "complete": False}
        sdk.add_order(new_order)

#  Update the order's details
        updated_order = {"id": 3, "petId": 1, "quantity": 2, "shipDate": "2024-10-05T16:00:00Z", "status": "pending", "complete": False}
        sdk.update_order(updated_order)

# Get updated order's name to check if it is correct
        orders = sdk.get_orders()
        updated_order_from_db = next(order for order in orders if order["id"] == 3)
        self.assertEqual(updated_order_from_db["quantity"], 2)




# DELETE ORDER TEST


# In this test we will check if we can delete an order
    def test_delete_order(self):
        sdk = OrderSDK(self.db_file, auth_key="special-key")
        
# First I will add a new order to delete
        new_order = {"id": 3, "petId": 1, "quantity": 1, "shipDate": "2024-10-05T16:00:00Z", "status": "pending", "complete": False}
        sdk.add_order(new_order)

# Then, let's delete new order from the database
        sdk.delete_order(3)

# Check if the order is deleted (back to 2 orders)
        orders = sdk.get_orders()
        self.assertEqual(len(orders), 2)


# Now tests have to executed when the script is run from the terminal:
# >>> python3 -m unittest discover <<<

if __name__ == '__main__':
    unittest.main()
