fef = open("Test1.txt", "r")
n_line = 0
n_word = 0
all_word = 0
n_character = 0
for line in fef.readlines():
    n_line += 1
    for word in line.split():
        n_word += 1
        all_word += 1
        for character in word:
            n_character += 1
    if n_word > 4:
        print(f"В {n_line}-й строке {n_word} слов")
    else:
        print(f"В {n_line}-й строке {n_word} слова")
    n_word = 0
print(f"Всего в файле {n_line} строк, {all_word} слов и {n_character} символов")
fef.close()
