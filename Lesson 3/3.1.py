def deleniye(number_1, number_2):
    try:
        1 / number_1
        1 / number_2
    except :
        print('Деление на 0, ошибка')
        return
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
    print(f"{number_2} / {number_1} = {number_2 / number_1}")
    return
try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    deleniye(number_1, number_2)
except:
    print('Не Вводите абракадабру')
