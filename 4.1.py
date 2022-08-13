from sys import argv

print('Введите значения для рассчета зарплаты сотрудника, выработка в часах, ставка в час, премия')
script_name, first_param, second_param, third_param = argv
zp = (int(first_param) * int(second_param)) + int(third_param)
print(f"Зароботная плата сотрудника состовляет {zp}")
