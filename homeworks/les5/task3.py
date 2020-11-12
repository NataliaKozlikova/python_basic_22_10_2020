"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task3.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    line_count = len(file.readlines())
    file.seek(0)

    idx = 0
    itm_sum = 0
    print('Фамилии сотрудников c окладом менее 20000 руб.:')
    while idx <= line_count:
        my_line = file.readline().split()
        for itm in my_line:
            if itm.isdigit() and int(itm) < 20000:
                print((' '.join(my_line)))
            if itm.isdigit():
                itm_sum += int(itm)
        idx += 1

    print(f'Средняя величина дохода сотрудников: {int(itm_sum/line_count)} руб.')
