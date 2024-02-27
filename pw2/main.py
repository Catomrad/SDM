import Classes.client
import Repositories.ClientRepository
from Classes import material, category, order, product, client
from Repositories import ClientRepository, OrderRepository, ProductRepository

client1 = client.Client(name="Name1", email="mail1@mail.com",
                               password="***", addr="Pushkin street 1")
client2 = client.Client(name="Name2", email="mail2@mail.com",
                               password="****", addr="Pushkin street 2")

Client_rep = ClientRepository.ClientRepository()

oak = material.Material(name="Дуб")

tables = category.Category(name="Столы")

prod_1 = product.Product(id=0, name="Дубовый стол",
                                 category=tables, material=oak, price=1000)
