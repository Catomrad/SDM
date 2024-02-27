from material import Material
from category import Category


class Product:

    def __init__(self, id, name, category: Category, material: Material, price):
        self.id = id
        self.name = name
        self.category = category
        self.material = material
        self.price = price


