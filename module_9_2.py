first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, где длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список пар (кортежей) слов одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь с парой ключ-значение: строка-длина строки, только с чётной длиной
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример вывода программы
print(first_result)   # Вывод: [10, 8, 8]
print(second_result)  # Вывод: [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)   # Вывод: {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
