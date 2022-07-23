lol = input('Введите строчку: ')
list = lol.split()
print('Слова которые вы ввели: ')
for el in list:
    if len(el) <= 10:
        print(el)
    else:
        el = el[0:10]
        print(el)