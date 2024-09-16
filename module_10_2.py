import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, total_enemies):
        super().__init__()
        self.name = name
        self.power = power
        self.total_enemies = total_enemies  # Индивидуальное количество врагов
        self.days = 0
        self.lock = threading.Lock()  # Блокировка для синхронизации

    def run(self):
        print(f"{self.name}, на нас напали!")
        while True:
            with self.lock:  # Блокируем доступ к общему количеству врагов
                if self.total_enemies <= 0:
                    break

                # Увеличиваем количество дней сражения
                self.days += 1
                
                # Уменьшаем количество врагов на силу рыцаря
                damage = min(self.power, self.total_enemies)
                self.total_enemies -= damage

                # Выводим информацию о сражении
                remaining_enemies = max(self.total_enemies, 0)
                day_word = "дней" if self.days > 1 else "день"
                print(f"{self.name}, сражается {self.days} {day_word}..., осталось {remaining_enemies} воинов.")

            time.sleep(1)  # Задержка в 1 секунду

        # Победа
        day_word = "дней" if self.days > 1 else "день"
        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")


# Создание рыцарей с индивидуальным количеством врагов
first_knight = Knight('Sir Lancelot', 10, 100)
second_knight = Knight("Sir Galahad", 20, 80)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битв
print("Все битвы закончились!")

