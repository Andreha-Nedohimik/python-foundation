class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"profit": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def get_total_income(self):
        return sum(self._income.values())


manager = Position("fef", "memo", "cleaner", 300, 50)
print(manager.get_full_name())
print(manager._position)
print(manager.get_total_income())