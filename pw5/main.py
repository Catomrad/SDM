from Classes.client import Client
from Classes.product import Product
from Classes.order import Order
from Repositories.XMLrepository import XMLRepository
import datetime
from Repositories.SQLRepository import SQLAlchemyRepository
from businessRules import BusinessRules
from setup_db import ClientModel, OrderModel, ProductModel, session
import os


def main():
    user_repo = SQLAlchemyRepository(session)

    # Создаем экземпляры
    client = ClientModel(id=1, name="Ivan", age=20)
    product = ProductModel(id=1, name="Wooden Table", price=1200, category = "Table", material = "Wood")
    order = OrderModel(id=1, date=datetime.date.fromisoformat('2024-12-04'), clients = 1, products = 1)

    user_repo.save(client)
    user_repo.save(order)
    user_repo.save(product)

    bus = BusinessRules(session)
    result = bus.Make_order(order_id = 1, client_id = 1, product_id = 1)
    print(result)  # Вывод: 1 если успешно


if __name__ == "__main__":
    main()