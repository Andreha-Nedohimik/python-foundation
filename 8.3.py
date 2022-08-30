class Checker:
    def __init__(self):
        test_list = []
        inp_ut = None
        print("Чтобы прервать ввод чисел введите stop")
        while 2 != 5:
            inp_ut = input("Введите число чтобы добавить его в список: ")
            if inp_ut == 'stop':
                break
            try:
                test_list.append(int(inp_ut))
            except:
                print("Ошибка, вводите только числа")
        self.test_list = test_list
    def __str__(self):
        return f"{self.test_list}"

my_list = Checker()
print(my_list)