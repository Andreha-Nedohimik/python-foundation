class Complex_number:
    def __init__(self, real_number, complex_number):
        self.real_number = real_number
        self.complex_number = complex_number

    def __add__(self, other):
        return Complex_number(self.real_number + other.real_number, self.complex_number + other.complex_number)

    def __mul__(self, other):
        return Complex_number(self.real_number * other.real_number - self.complex_number * other.complex_number,
                              self.real_number * other.complex_number + self.complex_number * other.real_number)

    def __str__(self):
        return f"{self.real_number}+{self.complex_number}i"


a = Complex_number(1, 2)
b = Complex_number(3, -4)
print(a)
print(b)
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b}={a * b}")
