import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в виде кортежа

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Читаем файл и переводим в нижний регистр
                    # Убираем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation + ' -'))
                    words = text.split()  # Разбиваем текст на слова
                    all_words[file_name] = words  # Записываем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()  # Игнорируем регистр
        result = {}
        all_words = self.get_all_words()  # Получаем все слова

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1  # Позиция первого вхождения (считаем с 1)
                result[file_name] = position

        return result

    def count(self, word):
        word = word.lower()  # Игнорируем регистр
        result = {}
        all_words = self.get_all_words()  # Получаем все слова

        for file_name, words in all_words.items():
            count = words.count(word)  # Считаем количество вхождений
            if count > 0:
                result[file_name] = count

        return result


# Пример использования класса
finder2 = WordsFinder('test_file.txt')

# Получаем все слова из файлов
print(finder2.get_all_words())

# Находим позицию первого вхождения слова 'TEXT'
print(finder2.find('TEXT'))

# Считаем количество вхождений слова 'teXT'
print(finder2.count('teXT'))
