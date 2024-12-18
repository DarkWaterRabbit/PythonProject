import random
from operator import contains


def get_cipher():  # Получение рандомного числа шифра
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 20))
    cipher = random.choice(numbers)
    return cipher

def get_passcod(n):
    passdict = {}  # Словарь с паролями
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    passdict.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    passdict.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    passdict.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passdict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passdict.update({20: 13141911923282183731746416515614713812911})
    passcod = passdict.get(n)
    return passcod

n = get_cipher()

print('Шифр :', n)

num1 = list(range(1, n))
num2 = list(range(1, n))
Parnum = []
result = ''

for i in num1:
    for j in num2:
        pn1 = i  #  num1[i]
        pn2 = j  # num2[j]
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                Parnum.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *Parnum)
print('Введите пароль', result, 'во вторую вставку')
if int(result) == get_passcod(n): #Проверка пароля
    print('Путь безопасен')