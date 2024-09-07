#Requests
#Возможности:
# Выполнение HTTP-запросов (GET, POST и т.д.)
# Обработка ответов, включая JSON
# Управление сессиями
# Работа с заголовками и параметрами
import requests

# Выполняем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    data = response.json()
    print("Данные из запроса:")
    print(data[:5])  # Выводим первые 5 записей
else:
    print("Ошибка запроса:", response.status_code)

#Pandas
#Возможности:
# Чтение и запись данных в различных форматах (CSV, Excel и т.д.)
# Манипуляция данными (фильтрация, группировка)
# Анализ данных с использованием статистических функций
import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')  # Предполагается, что файл существует

# Анализ данных
print("Основные статистические характеристики:")
print(df.describe())

# Фильтрация данных
filtered_data = df[df['column_name'] > 100]  # Замените 'column_name' на имя колонки
print("Отфильтрованные данные:")
print(filtered_data.head())

#Matplotlib
#Возможности:
# Создание статических, анимационных и интерактивных графиков
# Настройка графиков (подписи, легенды, цвета)
# Поддержка различных форматов вывода (PNG, PDF и т.д.)
import matplotlib.pyplot as plt

# Данные для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y, marker='o')
plt.title('Пример графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.savefig('plot.png')  # Сохранение графика в файл
plt.show()


