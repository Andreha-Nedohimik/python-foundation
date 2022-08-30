class Клетка:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return Клетка(self.size + other.size)

    def __sub__(self, other):
        if self.size >= other.size:
            return Клетка(self.size - other.size)
        else:
            return f"Ошибка вычитания, размеры первой клетки слишком малы"

    def __mul__(self, other):
        return Клетка(self.size * other.size)

    def __truediv__(self, other):
        return Клетка(self.size // other.size)

    def make_order(self, prm):
        return '\n'.join(['*' * prm for i in range(self.size // prm)]) + '\n' + '*' * (self.size % prm)

    def __str__(self):
        return f"{self.size}"


a = Клетка(20)
b = Клетка(30)
print(a.make_order(3))
list = [a - b, a + b, a * b, a / b]
for i in list:
    print(i)
