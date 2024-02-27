from Classes.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def del_product(self, product: Product):
        self.products.remove(product)

    def find_product(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def show_products(self):
        for p in self.products:
            print(f"{p.name}; {p.category.name}; "
                  f"{p.material.name}; {p.price}")
