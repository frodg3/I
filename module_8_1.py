def add_everything_up(a, b):
    # Проверяем типы a и b
    if isinstance(a, str) and isinstance(b, (int, float)):
        return f"{a}{b}"
    elif isinstance(b, str) and isinstance(a, (int, float)):
        return f"{a}{b}"
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError("Unsupported types")

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))      # яблоко4215
print(add_everything_up(123.456, 7))           # 130.456
