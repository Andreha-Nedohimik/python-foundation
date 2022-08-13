import itertools
from itertools import count, cycle


def iter_number(number, end):
    for el in count(number):
        if el > end:
            break
        else:
            print(el, end=' ')


def iter_cycle(test_list, end):
    c = 0
    for el in cycle(test_list):
        if c > end:
            break
        print(el)
        c += 1


try:
    a, b = map(int, input('Введите числа начала и конца счета: ').split())
except:
    print('Ошибка, пожалуйста введите числа начала и конца ввода')
iter_number(a, b)
final_list = input('\nВведите пожалуйста предложение: ').split()
iter_cycle(final_list, 16)
