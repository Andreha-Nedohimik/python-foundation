my_list = [1, 2, 3, 4, 6, 5]
input_number = 0
while input_number != 'Exit':
    my_list.sort(reverse = True)
    print('Текущий рейтинг состовляет: ', end= '\n')
    for el in my_list:
        print (el, end= ',')
    print('', 'Вы хотите ввести обновить рейтинг? Если да то введите число, если нет то введите Exit', sep='\n')
    input_number = input()
    while input_number != 'Exit':
        input_number = input('Введите число от 0 до 10, или Exit: ')
        try:
            int(input_number)
        except ValueError:
            print('Некорректный ввод')
            continue
        if input_number =='Exit' or 0 <= int(input_number) <= 10:
            break
        else:
            print('Некорректный ввод')
    if input_number == 'Exit':
        break
    else:
        my_list.append(int(input_number))
print('Спасибо, текущий рейтинг: ', my_list)
print('Извините, я немного считерил, но только в защите от ввода, это же не критично?')