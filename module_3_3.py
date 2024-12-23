def print_params(a = 1, b = 'строка', c = True): #1 Функция с параметрами по умолчанию:
    print(a,b,c) #2 Функция должна выводить эти параметры.

#3 Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(3456, 'Енот')
print_params( 3465,None, False)
print_params(23562365)
print_params()

#4 Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c = [1,2,3])
print('Функция print_params(c = [1,2,3]) работает')

#5 Создайте список values_list с тремя элементами разных типов
values_list = [2145565, None, 'Енот']
#6 Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a':3245232.242357, 'b':"Енот", 'c':False}
#7 Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

print_params(*values_list)
print_params(**values_dict)
#8 Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print('Функция print_params(*values_list_2, 42) работает')