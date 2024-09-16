import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль объекта
    module = obj.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info


# Пример класса для демонстрации
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2


# Создаем объект класса
my_obj = MyClass(10)

# Проводим интроспекцию объекта
info = introspection_info(my_obj)
print(info)
