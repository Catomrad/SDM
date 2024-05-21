from Classes.client import Client
from Classes.material import Material
from Classes.category import Category
from Classes.order import Order
from Classes.product import Product
from Repositories.ClientRepository import ClientRepository
from Repositories.ProductRepository import ProductRepository
from Repositories.OrderRepository import OrderRepository
import datetime
# Бизнес-правила:
# 1) Заказывать могут только люди, достигшие 18 лет
# 2) Заказывать можно только товары, присутствующие на складе(в репозитории)
# 3) Доставку может заказать только зарегестрированный пользователь
# 4) Дата доставки не может быть раньше чем дата заказа


clientRepository = ClientRepository()
productRepository = ProductRepository()
orderRepository = OrderRepository()


c1 = Client(id=1, name="Ivan", age = 20, email="addr1@mail.com", password="123", addr="home1")
c2 = Client(id=2, name="Pavel", age = 17, email="addr2@mail.com", password="321", addr="home2")
c3 = Client(id=3, name="Oleg", age = 12, email="addr3@mail.com", password="132", addr="home3")
c4 = Client(id=4, name="Denis", age = 34, email="addr4@mail.com", password="312", addr="home4")
c5 = Client(id=5, name="Ivan", age = 77, email="addr5@mail.com", password="231", addr="home5")


def auth(client_id): #Проверяет, присутствует ли пользователь в репозитории клиентов
    if clientRepository.find_client(client_id):
        return True
    else: 
        return False

def register(client:Client): #Добавляет клиента в репозиторий, если его не было там ранее
    if not clientRepository.find_client(client.id):
        clientRepository.add_client(client)
        return True
    else: 
        return False

def make_order(order:Order): #Добавляет заказ в репозиторий заказов, если удовлетворяет всем бизнес-правилам
    if (productRepository.find_product(order.product_id) and 
    clientRepository.find_client(order.client_id).age >= 18 and 
    auth(order.client_id) and 
    order.delivery_date > datetime.date.today()):
        orderRepository.add_order(order) 
        return True
    else:
        return False

    # print(not productRepository.find_product(order.product_id) is None,  
    # clientRepository.find_client(order.client_id).age >= 18, 
    # auth(order.client_id),  
    # order.delivery_date > datetime.date.today())
    
def show_orders_to_client(client_id):
    result = []
    if (auth(client_id)):
        for i in orderRepository.orders:
            if i.client_id == client_id:
                result.append(i)
    return result




register(c1)
register(c2)
register(c5)

productRepository.add_product(Product(1, "Дубовый стол", Category("Стол"), Material("Дуб"), 3000))
productRepository.add_product(Product(2, "Березовый стул", Category("Стул"), Material("Береза"), 1000))
productRepository.add_product(Product(3, "Дубовый стул", Category("Стул"), Material("Дуб"), 2000))
productRepository.add_product(Product(4, "Березовый стол", Category("Стол"), Material("Береза"), 3000))
productRepository.add_product(Product(5, "Фанерный скворечник", Category("Скворечник"), Material("Фанера"), 500))

p1 = Product(6, "Ивовая подставка", Category("Подставка"), Material("Ива"), 600)

o1 = Order(1, 1, 4, datetime.date(2024, 4, 24), 1)
o2 = Order(2, 5, 4, datetime.date(2024, 7, 14), 2)
o3 = Order(3, 4, 4, datetime.date(2024, 4, 24), 1)
o4 = Order(4, 3, 5, datetime.date(2024, 4, 24), 5)

make_order(o1)
make_order(o2)

print(show_orders_to_client(1)[0].delivery_date)