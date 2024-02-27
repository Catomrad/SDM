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
            print(f"{o.id}; {o.client.name}; "
                  f"{o.product.name};{o.product_count}; "
                  f"{o.date}; {o.discount}")
