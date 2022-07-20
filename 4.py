number = int(input('Введите целопе положительное число: '))
x = 0
while number > 1:
    if x < number % 10:
        x = number % 10
    number = number // 10
print('Наибольшая цифра в числе: ', x)
