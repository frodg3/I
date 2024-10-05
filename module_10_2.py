import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, enemies):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days = 0
        self.lock = threading.Lock()  # Замок для синхронизации

    def run(self):
        print(f"{self.name}, на нас напали!")

        while True:
            with self.lock:  # Блокируем доступ к количеству врагов
                if self.enemies <= 0:
                    break

                # Увеличиваем количество боевых дней
                self.days += 1

                # Уменьшаем количество врагов на силу рыцаря
                damage = min(self.power, self.enemies)
                self.enemies -= damage

                # Выводим информацию о битве
                remaining_enemies = max(self.enemies, 0)
                day_word = "день" if self.days == 1 else "дня" if self.days < 5 else "дней"
                print(f"{self.name} сражается {self.days} {day_word}..., осталось {remaining_enemies} воинов.")

            time.sleep(1)  # Задержка в 1 секунду

        # Победа
        day_word = "день" if self.days == 1 else "дня" if self.days < 5 else "дней"
        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")


# Создаем рыцарей с индивидуальным количеством врагов
first_knight = Knight('Sir Lancelot', 10, 100)  # 50 врагов для первого рыцаря
second_knight = Knight("Sir Galahad", 20, 100)  # 30 врагов для второго рыцаря

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ждем завершения обоих потоков
first_knight.join()
second_knight.join()

# Выводим строку, указывающую на то, что все битвы закончились
print("Все битвы закончились!")


# Вывод строки об окончании битв
print("Все битвы закончились!")

