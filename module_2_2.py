first = int(input('Введите 1 число: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 число: '))
if first == second and first == third and third == second:
    print(3)

elif first == second or first == third or third == second:

    print(2)

else:

    print(0)