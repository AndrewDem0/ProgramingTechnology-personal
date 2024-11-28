import heapq

# Модуль для зберігання інформації про замовлення
class Order:
    def __init__(self, order_id, customer_name, order_amount):
        self.order_id = order_id  
        self.customer_name = customer_name  
        self.order_amount = order_amount 
    
    def __lt__(self, other):
        return self.order_amount > other.order_amount
    
    def __repr__(self):
        return f"Order({self.order_id}, {self.customer_name}, {self.order_amount})"

#Виняток для порожньої черги замовлень  "
class EmptyQueueException(Exception):
    pass

# Клас для управління чергою замовлень
class OrderQueue:
    def __init__(self):
        self._queue = []

    # 1. Додавання нового замовлення в чергу
    def add_order(self, order):
        heapq.heappush(self._queue, order)
        print(f"Замовлення {order} додано до черги.")

    # 2. Вилучення замовлення з найвищим пріоритетом (найбільша сума)
    def process_order(self):
        if self._queue:
            highest_priority_order = heapq.heappop(self._queue)
            print(f"Замовлення {highest_priority_order} оброблено.")
            return highest_priority_order
        else:
            print("Черга замовлень порожня.")
            return "Не None"  # Навмисна помилка для тесту

    # 3. Перегляд усіх замовлень у черзі
    def view_all_orders(self):
        if not self._queue:
            raise EmptyQueueException("Черга порожня!")
        
        print("Усі замовлення в черзі:")
        for order in sorted(self._queue):
            print(order)

    # 4. Перегляд замовлення з найвищим пріоритетом (але без видалення)
    def peek_highest_priority_order(self):
        if self._queue:
            highest_priority_order = self._queue[0]
            print(f"Замовлення з найвищим пріоритетом: {highest_priority_order}")
            return highest_priority_order
        else:
            print("Черга порожня.")
            return None

    # 5. Перевірка кількості замовлень у черзі 
    def count_orders(self):
        count = len(self._queue)
        print(f"Кількість замовлень у чeрзі: {count}")
        return count


# Приклад використання програми
if __name__ == "__main__":

    order_queue = OrderQueue()

    order1 = Order(1, "Alice", 100)
    order2 = Order(2, "Bob", 250)
    order3 = Order(3, "Charlie", 150)
    order4 = Order(4, "Grase", 400)

    order_queue.add_order(order1)
    order_queue.add_order(order2)
    order_queue.add_order(order3)
    order_queue.add_order(order4)

    # Переглядаємо всі замовлення
    order_queue.view_all_orders()

    # Переглядаємо замовлення з найвищим пріоритетом
    order_queue.peek_highest_priority_order()

    # Обробляємо замовлення з найвищим пріоритетом
    order_queue.process_order()

    # Перевіряємо кількість замовлень
    order_queue.count_orders()

    # Знову переглядаємо всі замовлення після обробки одного
    order_queue.view_all_orders()
