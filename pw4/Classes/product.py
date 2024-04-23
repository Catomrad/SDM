from Classes.material import Material
from Classes.category import Category


class Product:

    def __init__(self, id:int, name, price):
        self.id = id
        self.name = name
        #self.category = category
        #self.material = material
        self.price = price
    
    def __eq__(self, other):
        return self.id == other.id


