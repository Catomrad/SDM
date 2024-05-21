import sys
sys.path.append('D:\Important_files\Study\Sem_6\Методологии разработки программного обеспечения\pw3')
from Classes.product import Product

class ProductRepository:

    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if not product in self.products:
            self.products.append(product)

    def del_product(self, product: Product):
        self.products.remove(product)

    def find_product(self, product_id):
        for p in self.products:
            if p.id== product_id:
                return p

    def show_products(self):
        for p in self.products:
            print(f"{p.name}; {p.category.name}; "
                  f"{p.material.name}; {p.price}")
            
    def sort_products_material(self, material):
        result=[]
        for p in self.products:
            if p.material.name == material:
                result.append(p)
        return result
    
    def sort_products_category(self, category):
        result=[]
        for p in self.products:
            if p.category.name == category:
                result.append(p)
        return result
