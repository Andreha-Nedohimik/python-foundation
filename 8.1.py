class Data:
    def __init__(self, time):
        self.time = time

    @classmethod
    def get_number(cls, time):
        return [number for number in map(int, time.split('-'))]

    @staticmethod
    def check_time(time):
        d, m, a = time.split('-')
        map(int, d, m, a)
        if int(d) < 1 or int(d) > 31:
            print("Ошибка значения числа")
        if int(m) < 1 or int(m) > 12:
            print("Ошибка значения месяца")
        if int(a) < 1:
            print("Ошибка значения года")


time_now = Data(input('Введите время в формате ДД-ММ-ГГГГ: '))
time_now = Data(123 - 32 - 222)
Data.check_time('41-23-244')
print(Data.get_number('41-23-244'))
