input_number = int(input('Введите время в секундах: '))
sec = input_number % 60
minuts = (input_number // 60) % 60
hours = input_number // 3600
n = '0'
if sec < 10:
    sec = n + str(sec)
if minuts < 10:
    minuts = n + str(minuts)
if hours < 10:
    hours = n + str(hours)
print(f"Это время равно: {hours}:{minuts}:{sec}")
