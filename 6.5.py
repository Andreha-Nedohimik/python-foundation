class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем ручкой {self.title}")
class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем карандашом {self.title}")
class Handle(Stationery):
    def draw(self):
        print(f"Рисуем маркером {self.title}")
stationery = Stationery("Memo")
pen = Pen("Feno")
pencil = Pencil("Mgemo")
handle = Handle("fwfwfwfwfwf@")
stationery_all = [stationery, pen, pencil, handle]

for i in stationery_all:
    i.draw()