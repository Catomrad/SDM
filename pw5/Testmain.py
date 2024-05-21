import unittest
import main
from main import auth, register, make_order, show_orders_to_client



class TestFunctions(unittest.TestCase):

    def test_auth(self):
        # Тест на успешную авторизацию
        self.assertEqual(auth(1), True)

        # Тест на неудачную авторизацию
        self.assertEqual(auth(9), False)

    def test_register(self):
        # Тест на успешную регистрацию
        self.assertEqual(register(main.c3), True)

        # Тест на попытку зарегистрировать уже существующего пользователя
        self.assertEqual(register(main.c2), False)

    def test_make_order(self):
        # Тест на успешное создание заказа
        self.assertEqual(make_order(main.o4), True)

    def test_show_orders_to_client(self):
        # Создаем несколько заказов для пользователя
        make_order(main.o1)
        make_order(main.o2)
        make_order(main.o3)

        # Получаем список заказов для пользователя
        orders = show_orders_to_client(main.o1.client_id)

        # Проверяем, что список заказов содержит созданные ранее заказы
        self.assertIn(main.o1, orders)
        self.assertIn(main.o3, orders)

if __name__ == '__main__':
    unittest.main()