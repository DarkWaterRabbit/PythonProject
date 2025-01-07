

def test_function():        # 1
    def inner_function():   # 2
        print("Я в области видимости функции test_function")

    inner_function()        # 3

#inner_function()  # не работает! (ошибка)

test_function()     # Работет