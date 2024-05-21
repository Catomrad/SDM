from setup_db import ClientModel, OrderModel, ProductModel
import datetime
# Бизнес-правила:
# 1) Заказывать могут только люди, достигшие 18 лет
# 2) Заказывать можно только товары, присутствующие на складе(в репозитории)
# 3) Доставку может заказать только зарегестрированный пользователь
# 4) Дата доставки не может быть раньше чем дата заказа


class BusinessRules:
    def __init__(self, session):
        self.session = session
        self.orders = session.query(OrderModel).all()

    def Make_order(self, order_id, client_id, product_id):
        client = self.session.query(ClientModel).filter_by(id=client_id).one()
        product = self.session.query(ClientModel).filter_by(id=product_id).one()
        order = self.session.query(ProductModel).filter_by(id=order_id).one()

        if order in self.orders:
            if client.age >= 18:
                if order.date >= datetime.now():
                    return 1
                else: 
                    print("Дата доставки не может быть раньше чем дата заказа")
                    return -1
                
                return 1
            else:
                print("Заказывать могут только люди, достигшие 18 лет")
                return -1

