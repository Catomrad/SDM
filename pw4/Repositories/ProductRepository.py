import sys
sys.path.append('D:\Important_files\Study\Sem_6\Методологии разработки программного обеспечения\pw3')
from Classes.product import Product
from Classes.material import Material
from Classes.category import Category

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

# pr1 = ProductRepository()
# c1 = Category("table")
# m1 = Material("wood")
# p1 = Product(1,"wooden table",  c1, m1, 1000)
# pr1.add_product(p1)
# pr1.show_products()