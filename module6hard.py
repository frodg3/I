import math


class Figure:
    def __init__(self, color, *sides):
        self._sides = []
        self._color = list(color)
        self.filled = False
        self.sides_count = len(sides)  # Инициализируем количество сторон

        if self.is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            self.set_sides(*[1] * self.sides_count)  # Если некорректные стороны, задаем единичные

    def get_color(self):
        return self._color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = [r, g, b]

    def is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(
            isinstance(side, (int, float)) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def perimeter(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides):
            self._sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, circumference):
        self.sides_count = 1
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    def __init__(self, color, a, b, c):
        self.sides_count = 3
        super().__init__(color, a, b, c)

    def get_square(self):
        s = sum(self._sides) / 2
        return math.sqrt(s * (s - self._sides[0]) * (s - self._sides[1]) * (s - self._sides[2]))


class Cube(Figure):
    def __init__(self, color, side_length):
        self.sides_count = 12
        super().__init__(color, *[side_length] * self.sides_count)

    def get_volume(self):
        return self._sides[0] ** 3


# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(circle1.perimeter())

# Проверка объёма (куба):
print(cube1.get_volume())
