import threading
import time


class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов
    lock = threading.Lock()  # Блокировка для синхронизации

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while True:
            with Knight.lock:  # Блокируем доступ к общему количеству врагов
                if Knight.total_enemies <= 0:
                    break

                # Увеличиваем количество дней сражения
                self.days += 1
                # Уменьшаем количество врагов на силу рыцаря
                Knight.total_enemies -= self.power

                # Выводим информацию о сражении
                remaining_enemies = max(Knight.total_enemies, 0)
                day_word = "дней" if self.days > 1 else "день"
                print(f"{self.name}, сражается {self.days} {day_word}..., осталось {remaining_enemies} воинов.")

            time.sleep(1)  # Задержка в 1 секунду

        # Победа
        day_word = "дней" if self.days > 1 else "день"
        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битв
print("Все битвы закончились!")
