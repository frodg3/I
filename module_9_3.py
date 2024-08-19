first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для разницы длин строк, если они не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример вывода программы
print(list(first_result))   # Вывод: [1, 2]
print(list(second_result))  # Вывод: [False, False, True]
