def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Проверяем, является ли объект экземпляром класса
    if hasattr(obj, '__dict__'):
        # Получаем атрибуты объекта
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
        # Получаем методы объекта
        methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    else:
        # Для встроенных типов, таких как int, str и т.д.
        attributes = []
        methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль объекта
    module = obj.__class__.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info


# Примеры использования
print(introspection_info(42))
print(introspection_info("Hello"))
print(introspection_info([1, 2, 3]))
