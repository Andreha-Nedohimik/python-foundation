def fact(n):
    summ = 1
    for el in range(1, n):
        summ *= el
        yield summ


number = int(input('Введите целое положительное число: '))
for el in fact(number):
    print(el, end=' ')
