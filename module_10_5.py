filenames = [f'./data/file {number}.txt' for number in range(1, 5)]
import time
from multiprocessing import Pool

for i in range(1, 5):
    with open(f'file {i}.txt', 'w', encoding='utf-8') as f:
        f.write(f'Содержимое файла {i}\n')
        f.write('Еще одна строка.\n')


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line.strip())
    # Здесь можно добавить вывод для проверки, но в задании это не требуется
    # print(f"Файл {name} прочитан.")


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time_linear = time.time()
    for filename in filenames:
        read_info(filename)
    end_time_linear = time.time()
    print(f"Линейный вызов: {end_time_linear - start_time_linear:.6f} секунд")

    # Многопроцессный вызов
    start_time_multiprocessing = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time_multiprocessing = time.time()
    print(f"Многопроцессный вызов: {end_time_multiprocessing - start_time_multiprocessing:.6f} секунд")
