import sys
sys.path.append('D:\Important_files\Study\Sem_6\Методологии разработки программного обеспечения\pw3')
from Classes.order import Order


class OrderRepository:

    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def del_order(self, order: Order):
        self.orders.remove(order)

    def find_order(self, order_id):
        for o in self.orders:
            if o.id == order_id:
                return o

    def show_orders(self):
        for o in self.orders:
            print(f"{o.id}; {o.client_id}; "
                  f"{o.product_id}; {o.product_count}; "
                  f"{o.delivery_date}")

