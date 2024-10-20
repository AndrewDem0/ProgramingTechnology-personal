import os
import unittest
import xmlrunner
from lab2 import Order, OrderQueue, EmptyQueueException

class TestOrderQueue(unittest.TestCase):

    # 1. Тест на додавання замовлень
    def test_add_order(self):
        queue = OrderQueue()
        order = Order(1, "Alice", 100)
        queue.add_order(order)
        
        self.assertEqual(queue.count_orders(), 1)
    
    # 2. Тест на обробку замовлення з найвищим пріоритетом
    def test_process_order(self):
        queue = OrderQueue()
        order1 = Order(1, "Alice", 100)
        order2 = Order(2, "Bob", 250)
        queue.add_order(order1)
        queue.add_order(order2)
        
        highest_priority_order = queue.process_order()
        self.assertEqual(highest_priority_order.order_id, 2)
        self.assertEqual(queue.count_orders(), 1)

    # 3. Тест на перегляд усіх замовлень з порожньої черги (виняток)
    def test_view_all_orders_empty_queue(self):
        queue = OrderQueue()
        
        with self.assertRaises(EmptyQueueException):
            queue.view_all_orders()

    # 4. Тест на перегляд усіх замовлень з заповненої черги
    def test_view_all_orders_with_orders(self):
        queue = OrderQueue()
        order1 = Order(1, "Alice", 100)
        order2 = Order(2, "Bob", 250)
        queue.add_order(order1)
        queue.add_order(order2)


    # 5. Тест на перегляд замовлення з найвищим пріоритетом (без видалення)
    def test_peek_highest_priority_order(self):
        queue = OrderQueue()
        order1 = Order(1, "Alice", 100)
        order2 = Order(2, "Bob", 250)
        queue.add_order(order1)
        queue.add_order(order2)

        highest_order = queue.peek_highest_priority_order()
        self.assertEqual(highest_order.order_id, 2)

    # 6. Тест на кількість замовлень
    def test_count_orders(self):
        queue = OrderQueue()
        order1 = Order(1, "Alice", 100)
        order2 = Order(2, "Bob", 250)
        queue.add_order(order1)
        queue.add_order(order2)

        self.assertEqual(queue.count_orders(), 2)

    # Негативний тест на обробку порожньої черги (повинен повернути None)
    @unittest.expectedFailure
    def test_process_order_empty_queue(self):
        queue = OrderQueue()
        
        # Обробка порожньої черги має повернути None
        processed_order = queue.process_order()
        self.assertIsNone(processed_order)

if __name__ == '__main__':
    # Отримуємо директорію для збереження звіту
    results_dir = 'lab4_jenkins'  # Змінюємо шлях до test-results
    os.makedirs(results_dir, exist_ok=True)  # Створюємо папку, якщо вона не існує

    # Використовуємо xmlrunner для виводу в вказану директорію
    with open(os.path.join(results_dir, 'test-results.xml'), 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), verbosity=2)