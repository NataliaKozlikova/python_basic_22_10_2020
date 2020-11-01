"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
while True:
    month_num = input('Введите номер месяца (от 1 до 12)\n>>>')
    if month_num.isdigit():
        month_num = int(month_num)
        if (month_num >= 1) and (month_num <= 12):
            break
    print('Ошибка! Введено не число или числое не попадаетв диапазон от 1 до 12')

month_list = ['январь',
              'февраль',
              'март',
              'апрель',
              'май',
              'июнь',
              'июль',
              'август',
              'сентябрь',
              'октябрь',
              'ноябрь',
              'декабрь']

print(f'Месяц:', month_list[month_num - 1])

month_dict = {1: 'зима',
              2: 'зима',
              3: 'весна',
              4: 'весна',
              5: 'весна',
              6: 'лето',
              7: 'лето',
              8: 'лето',
              9: 'осень',
              10: 'осень',
              11: 'осень',
              12: 'зима'}

print(f'Время года:',month_dict[month_num])

"""
season_list = ['зима',
               'весна',
               'лето',
               'осень']

season_idx = month_num // 3 % 4

print(season_list[season_idx])
"""