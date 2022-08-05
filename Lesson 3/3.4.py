def stepen(x, y):
    print(f"Число {x} в степени {y} равно {x ** y}")


def stepen_while(x, y):
    i = 0
    proizv = 1
    while i > y:
        proizv /= x
        i -= 1
    print(f"Число {x} в степени {y} равно {proizv}")


try:
    x = int(input('Введите число которое нужно ввозвести в степень (положительное целое число): '))
    y = int(input('Введите степень, в которую нужно ввозвести число (отрицательное целое число): '))
    if x > 0 and y < 0:
        stepen(x, y)
        stepen_while(x, y)
    else:
        print('Вводите нормальные числа')
except:
    print('Вводите нормальные числа')
