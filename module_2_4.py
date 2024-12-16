numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    Bolut = True

    k = numbers[i]

    if k < 2: #Простое число не может быть меньше 2, возврат в начало цикла

        continue
    else:

        f = k ** (1 / 2)
    for a in range(2, int(f + 1)): #Провека через цикл на простое или нет число
        if k % a == 0:
            Bolut = False
            break

    if not (Bolut):
        not_primes.append(k)
    else:
        primes.append(k)
Bolut = True

print('primes ', primes)
print('not_primes', not_primes)