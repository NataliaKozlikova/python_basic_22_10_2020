"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
time = int(input('Введите время в секундах\n>>>'))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time - minute * 60 - hour * 3600
print('Время {0}:{1}:{2}'.format(hour, minute, second))
