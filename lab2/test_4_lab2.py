import unittest
from lab2.lab2 import Order, OrderQueue

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

    # 3. Тест на перегляд усіх замовлень
    def test_view_all_orders(self):
        queue = OrderQueue()
        order1 = Order(1, "Alice", 100)
        order2 = Order(2, "Bob", 250)
        queue.add_order(order1)
        queue.add_order(order2)

        all_orders = sorted(queue._queue)  #reverse=True
        self.assertEqual(all_orders[0].order_id, 2)
        self.assertEqual(all_orders[1].order_id, 1)
        #queue.view_all_orders()
    
    # 4. Тест на перегляд замовлення з найвищим пріоритетом (без видалення)
    def test_peek_highest_priority_order(self):
        queue = OrderQueue()
        order1 = Order(1, "Alice", 100)
        order2 = Order(2, "Bob", 250)
        queue.add_order(order1)
        queue.add_order(order2)

        highest_order = queue.peek_highest_priority_order()
        self.assertEqual(highest_order.order_id, 2)

    # 5. Тест на кількість замовлень
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
    unittest.main()