import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс
        self.lock = threading.Lock()  # Объект блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()  # Разблокируем, если баланс >= 500
            time.sleep(0.001)  # Имитация времени пополнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокируем поток при недостатке средств
            time.sleep(0.001)  # Имитация времени снятия

# Создание объекта банка
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
