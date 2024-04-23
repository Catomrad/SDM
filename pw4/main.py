from Classes.client import Client
from Classes.product import Product
from Classes.order import Order
from Repositories.XMLrepository import XMLRepository

def save_to_xml(client_data):
    repository = XMLRepository("base.xml")
    repository.save(client_data)


def find_client_by_name(name):
    client_repository = XMLRepository("base.xml")
    query = f"//item[name='{name}']"
    clients = client_repository.find()
    return clients

if __name__ == "__main__":
    client_data = {
        'id': 1,
        'name': "Ivan",
        'age': 20,
        'email': "mail@mail.ru",
        'addr': "Paper street 1"
    }
    client = Client(**client_data)  
    save_to_xml(client)
    client_data = {
        'id': 2,
        'name': "Pavel Nikolaev",
        'age': 20,
        'email': 'gmail@gmail.com',
        'addr': "Paper street 2"
    }
    client = Client(**client_data)  
    save_to_xml(client)
    client = Client(3, 'Denis Belavin', 21, 'yandex@yandex.ru', 'Paper street 3')
    save_to_xml(client)

    product_data = {
        'id': 2,
        'name': 'Chair',
        'price': 2000
    }
    product = Product(**product_data)
    save_to_xml(product)
    product_data = {
        'id': 1,
        'name': 'Table',
        'price': 1000
    }
    product = Product(**product_data)
    save_to_xml(product)

    print(find_client_by_name('Ivan'))

    