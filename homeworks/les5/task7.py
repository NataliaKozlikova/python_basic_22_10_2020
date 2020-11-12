"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import os
import json

file_path = os.path.join(os.path.dirname(__file__), 'task7.txt')
list_profit = []
dict_profit = {}
idx = 0
count = 0

with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        my_line = line.split(' ')
        list_profit.append(int(my_line[2]) - int(my_line[3]))
        dict_profit[my_line[0]] = list_profit[idx]
        if list_profit[idx] > 0:
            count += 1
        sum_profit = sum(itm for itm in list_profit if itm > 0)
        idx += 1

    my_list = [dict_profit, {'average_profit': sum_profit / count}]

with open('task7.json', 'w') as write_file:
    json.dump(my_list, write_file)
