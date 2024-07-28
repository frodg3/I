class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издаёт лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полёта на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация родительского класса Horse
        Eagle.__init__(self)  # Инициализация родительского класса Eagle

    def move(self, dx, dy):
        self.run(dx)  # Запускаем метод run из класса Horse
        self.fly(dy)  # Запускаем метод fly из класса Eagle

    def get_pos(self):
        return self.x_distance, self.y_distance  # Возвращаем текущее положение

    def voice(self):
        print(self.sound)  # Печатаем звук из экземпляра класса


# Пример использования классов
p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice()  # I train, eat, sleep, and repeat
