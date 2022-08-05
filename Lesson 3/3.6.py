def function(text):
    proverka = {
        'Английский': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z"]}
    my_list = list(text.split())
    pos = 0
    for i in my_list:
        h = True
        for a in i:  # Проверка на то что в слове все латинские маленькие буквы
            if not a in proverka['Английский']:
                h = False
                break
        if h is True:  # Если слово подходит, то переводит первую букву в верхний регистр
            my_list.insert(pos, i.title())
            my_list.pop(pos + 1)
        pos += 1
    print(' '.join(my_list))


text = input('Введите строчку: ')
function(text)
