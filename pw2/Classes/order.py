from client import Client
from product import Product


class Order:

    def __init__(self, id, product: Product, product_count, date, client: Client, discount):
        self.id = id
        self.client = client
        self.date = date
        self.product_count = product_count
        self.product = product
        self.discount = discount


