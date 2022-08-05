def summary(a, b, c):
    numbers = a, b, c
    print(f"Сумма двух наибольших чисел из введенных равна: ", sum(numbers) - min(a, b, c))


try:
    d, e, f = map(int, input('Введите 3 любых числа: ').split())
    summary(d, e, f)
except:
    print('Вы вводите какую то дич')
