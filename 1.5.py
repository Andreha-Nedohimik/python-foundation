gain = int(input('Введите выручку фирмы: '))
cost = int(input('Введите издержку фирмы: '))
if cost > gain:
    print('Фирма работает с убытком')
else:
    print('Ретабельность выручки фирмы состовляет', cost / gain)
    number_people = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы в рассчете на одного сотрудника состовляет', (gain - cost) / number_people)
