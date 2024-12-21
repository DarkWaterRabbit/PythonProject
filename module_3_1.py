calls = 0
Sp2 = []

#Списки будут создоваться пользователем

def count_calls():
    global calls
    calls += 1
    return calls

def string_info (string):
    str1 = str(string)
    result = (len(str1), str1.upper(), str1.lower())
    count_calls()
    return result


def is_contains(string, list_to_search) :  # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)) :
        if str(list_to_search[i]).lower() == string :
            Bulitt = True
            break
        else :
            Bulitt = False
            continue
    return Bulitt
def Spisok (a):
    global Sp2
    for i in range(a) :

        Sp1 = input('Введите слово в список : ')
        Sp2.append(Sp1)

        print(string_info(Sp1))

    return Sp2

Sp3 = Spisok (int(input('Введите количество элементов первого списка: ')))

print(is_contains(input('Введите слово входящие в список: '), Sp3))

Sp3 = Spisok (int(input('Введите количество элементов второго списка: ')))

print(is_contains(input('Введите слово не взходящие в список: '), Sp3))

print('Количество вызова функций',calls)


