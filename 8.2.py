class Devising:
    def __init__(self):
        n_1 = input("Введите делимое число: ")
        n_2 = input("Введите делитель: ")
        try:
            self.n_1 = int(n_1)
            self.n_2 = int(n_2)
        except:
            print("Ошибка, некорректный ввод")

    def __str__(self):
        if self.n_2 == 0:
            return f"Ошибка, деление на 0"
        else:
            return f"Результат деления {self.n_1} на {self.n_2} = {self.n_1 / self.n_2}"


print(Devising())
