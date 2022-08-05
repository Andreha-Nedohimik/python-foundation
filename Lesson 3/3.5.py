def summa(stop):
    summary = 0
    first_sum = 0
    h = 'r'
    while h != stop:
        my_list = input('Введите числа для их сложения: ').split()
        for i in my_list:
            try:
                if i == stop:
                    h = stop
                    break
                else:
                    summary += int(i)
                    first_sum += int(i)
            except:
                print('Ругаюсь!!!!')
                break
        print(f"Итоговая сумма равна {summary}, промежуточная {first_sum}")
        first_sum = 0


stop = input('Введите стоп символ: ')
summa(stop)
