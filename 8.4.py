class Storage_Org_tech:
    def __init__(self, volume):
        self.volume = volume
        self.number_techs = 0
        self.sum_cost = 0
        self.storage = {}
        self.list_of_tech_type = {}
        self.number_unic_tech = 0
        self.close_volume = 0

    def show_all_tech(self):
        return f"На сейчас на складе находится {self.number_techs} ед. техники, {self.number_unic_tech} типов,занимающие {self.close_volume}, Общая стоимость {self.sum_cost}, свободного места осталось {self.volume - self.close_volume}."

    def show_all_unic_tech(self):
        return f"Сейчас на складе находятся: {', '.join(self.list_of_tech_type)}."

    def add_tech(self, tech_stats, *кол_во):
        if type(кол_во) == tuple:
            кол_во = 1
        if self.close_volume + tech_stats["size"] > self.volume:
            print("Ошибка, на складе слишком мало места, склад заполнен.")
        elif int(кол_во) < 1:
            print('Ошибка, нельзя добавить того чего нет')
        else:
            if self.list_of_tech_type.get(tech_stats["name"]) == None:
                self.list_of_tech_type[tech_stats["name"]] = 1
                self.number_unic_tech += 1
                self.storage[f"{tech_stats['name']}"] = tech_stats
                if type(кол_во) == int:
                    while int(кол_во) > 0:
                        self.close_volume += tech_stats["size"]
                        self.sum_cost += tech_stats["price"]
                        self.number_techs += 1
                        кол_во -= 1

    def show_king_tech(self, tech_name):
        if self.list_of_tech_type.get(tech_name) == None:
            return f"Ошибка, техники с таким названием нет."
        else:
            return f"Название {self.storage[tech_name]['name']}, стоимость {self.storage[tech_name]['price']}, размеры {self.storage[tech_name]['size']}, Особенности {self.storage[tech_name]['species']}, описание {'отсутствует' if ''.join(list(self.storage[tech_name]['description'])) == '' else ''.join(list(self.storage[tech_name]['description']))}."

    def player_add_techs(self):
        memo = input('Для возвращение в меню напишите <Назад>, для добавления напишите <Добавить>: ')
        while memo != 'Назад':
            if memo == 'Добавить' or memo == "1":
                list_stats = {"Имя": '', "Цену": 0, "Размеры (в кубомертах)": 0, "Особенность": '',
                              "Описание (опционально)": '', "Количество": 0}
                for stat, stat_number in list_stats.items():
                    print(f"Напишите {stat}: ", end='')
                    list_stats[stat] = input()
                    if list_stats[stat] == '':
                        while list_stats[stat] == '':
                            print("Ошибка, неккоректный ввод, попробуйте еще раз: ", end='')
                            list_stats[stat] = input()
                    if stat == "Цену" or stat == "Размеры (в кубомертах)" or stat == "Количество":
                        try:
                            list_stats[stat] = int(list_stats[stat])
                            continue
                        except:
                            chek = False
                            while chek == False:
                                print(f"Необходимо ввести целое число, попробуйте ввести {stat} еще раз: ", end='')
                                list_stats[stat] = input()
                                if list_stats[stat] == '':
                                    continue
                                try:
                                    list_stats[stat] = int(list_stats[stat])
                                    chek = True
                                except:
                                    chek = False
                print(list_stats)
                new_tech = Принтер(list_stats["Имя"], list_stats["Цену"], list_stats["Размеры (в кубомертах)"],
                                   list_stats["Особенность"],
                                   list_stats["Описание (опционально)"])
                print(new_tech.show_stats())
                Склад.add_tech(new_tech.stats(), list_stats["Количество"])
            else:
                memo = input(
                    'Неккоректный ввод.\nДля возвращение в меню напишите <Назад>, для добавления напишите <Добавить>: ')
                continue
            print(f'Спасибо, вы успешно добавили технику {list_stats["Имя"]}, хотите добавить еще одну? ')
            memo = input('Для добавления техники напишите <Добавить>, для выхода <Выход>: ')

    def menu(self):
        print('Здравствуйте, вы зашли в меню склада.')
        print('Для того чтобы выйти из программы введите <Выход>.',
              'Для того чтобы посмотреть технику введите <Показать технику>.',
              'Для того чтобы посмотреть определенную технику напишите <Посмотреть <название техники>>.',
              'Для того чтобы добавить технику напишите <Добавить>.',
              'Если вы забыли какие команды есть напишите <Помощь>', sep='\n')
        memo = ''
        while memo != 'Выход':
            memo = input('Что вы хотите?: ')
            if memo == 'Показать технику':
                print(Склад.show_all_unic_tech())
                print(Склад.show_all_tech())
            elif memo == 'Добавить' or memo == "1":
                Склад.player_add_techs()
            elif memo == 'Выход':
                break
            elif memo == 'Помощь':
                print('Для того чтобы выйти из программы введите <Выход>.',
                      'Для того чтобы посмотреть технику введите <Показать технику>.',
                      'Для того чтобы посмотреть определенную технику напишите <Посмотреть <название техники>>.',
                      'Для того чтобы добавить технику напишите <Добавить>.',
                      'Если вы забыли какие команды есть напишите <Помощь>', sep='\n')
            elif memo == '':
                print('Ошибка, неккоректный ввод, попробуйте еще раз.')
                continue
            else:
                test_list = []
                test_list = memo.split()
                if test_list[0] == 'Посмотреть':
                    try:
                        print(Склад.show_king_tech(test_list[1]))
                        continue
                    except:
                        print('Неккоректный ввод, попробуйте еще раз. Если забыли команды напишите <Помощь>')
                else:
                    print('Неккоректный ввод, попробуйте еще раз. Если забыли команды напишите <Помощь>')
        print('Спасибо что воспользовались нашим складом! Желаем вам хорошего дня и настроения!')


class Org_tech:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
        self.all_stats = {}

    def show_stats(self):
        return f"{self.all_stats}"

    def stats(self):
        return self.all_stats


class Принтер(Org_tech):
    def __init__(self, name, price, size, species, *description):
        self.name = name
        self.size = size
        self.price = price
        self.species = species
        self.description = description
        self.all_stats = {'name': self.name, "price": self.price, "size": self.size, "species": self.species,
                          "description": self.description}


class Сканер(Org_tech):
    def __init__(self, name, price, size, species, *description):
        self.name = name
        self.size = size
        self.price = price
        self.species = species
        self.description = description
        self.all_stats = {'name': self.name, "price": self.price, "size": self.size, "species": self.species,
                          "description": self.description}


class Ксерокс(Org_tech):
    def __init__(self, name, price, size, species, *description):
        self.name = name
        self.size = size
        self.price = price
        self.species = species
        self.description = description
        self.all_stats = {'name': self.name, "price": self.price, "size": self.size, "species": self.species,
                          "description": self.description}


Склад = Storage_Org_tech(500000000000)
Ксерокс_1 = Ксерокс("Никита", 2400, 10, "Желтый лист бумаги", "Абобус")
Ксерокс_2 = Ксерокс("Ваня", 1, 0.001, "Бумага из не очень хорошего материала", 'd')
Сканер_1 = Сканер("Иосиф", 100000, 5, "Сканирует только золотую бумагу")
Сканер_2 = Сканер("Андрей", 5000, 100, "Гофрированная бумага")
Принтер_1 = Принтер("Марина", 0.005, 1000000, "Соболезную", "R.I.P. (Локалььные мемы)")
Принтер_2 = Принтер("Папира", 1500000, 46, "Очень хороший принтер")
МОй_список = [Ксерокс_1, Ксерокс_2, Сканер_2, Сканер_1, Принтер_1, Принтер_2]
for el in МОй_список:
    Склад.add_tech(el.stats())
count = 0
while count < 200:
    Склад.add_tech(Принтер_1.stats())
    count += 1
Склад.menu()
