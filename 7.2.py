from abc import ABC, abstractmethod


class Workout(ABC):
    summary = 0

    def __init__(self, value):
        self.value = value

    @property
    @abstractmethod
    def spesies():
        """Memo"""

    def __add__(self, other):
        Workout.summary += self.spesies + other.spesies
        return Zero(0)

    def __str__(self):
        resault = round(Workout.summary, 5)
        Workout.summary = 0
        return f"{resault}"

class Coat(Workout):
    @property
    def spesies(self):
        return (self.value / 6.5) + 0.5


class Costume(Workout):
    @property
    def spesies(self):
        return (2 * self.value + 0.3) / 100
class Zero(Workout):
    @property
    def spesies(self):
        return 0
a = Coat(24)
b = Costume(26)
print(a+b+b+a)