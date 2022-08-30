from random import choice
class Car:
    direction = ["налево", "направо", "назад",]
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police is False:
            police = "полицейская машина"
        else:
            police = "не полишейская магина"
        print(f"Машина: {color} {name} со скоростью {speed} км/ч, {police}")
    def go(self):
        print(f"{self.name} едет")
    def stop(self):
        print(f"{self.name} остановилась")
    def turn(self,):
        print(f"{self.name} повернула {choice(self.direction)}")
    def show_speed(self):
        print(f"{self.name} скорость {self.speed}")


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)
    def show_speed(self):
        return print(f"Внимание! У {self.name} скорость {self.speed}, Машина превышает скорость! ") if self.speed > 60 else super().show_speed()
class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)

class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        return print(f"Внимание! У {self.name} скорость {self.speed}, Машина превышает скорость! ") if self.speed > 40 else super().show_speed()

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)

police_car = PoliceCar("Мазда с мигалками на крыше", "Черно-белая", 500)
work_car = WorkCar("заниженная приора", "Зеленая", 20)
sport_car = SportCar("Москвич 79 года", "Черная", 800)
town_car = TownCar("Лада приора", "Белая", 80)
print()
cars = [police_car, work_car, sport_car, town_car]
print()
for i in cars:
    i.go()
    i.show_speed()
    i.turn()
    i.stop()
    print()
    print()