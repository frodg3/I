def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Вызов функции test_function
test_function()

# Попытка вызвать inner_function вне функции test_function
# inner_function()
