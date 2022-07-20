input_number = int(input('Введите время в секундах: '))
sec = input_number % 60
minuts = (input_number // 60) % 60
hours = input_number // 3600
print(f"Это время равно: {hours:02}:{minuts:02}:{sec:02}")
