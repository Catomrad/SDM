from Classes.client import Client
from Classes.product import Product
import datetime

class Order:

    def __init__(self, id, product_id, product_count, delivery_date:datetime.date, client_id):
        self.id = id
        self.client_id = client_id
        self.delivery_date = delivery_date
        self.product_count = product_count
        self.product_id = product_id
    
    def __eq__(self, other):
        return self.id == other.id


