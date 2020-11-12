"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task3.txt')

with open(file_path, 'r', encoding='UTF-8') as file:

    print('Фамилии сотрудников c окладом менее 20000 руб.:')
    line_count = 0
    for line in file:
        my_line = line.split()
        my_sal = sum(int(itm) for itm in my_line[1:] if itm.isdigit())
        for itm in my_line:
            if itm.isdigit() and int(itm) < 20000:
                print((' '.join(my_line)))
        line_count += 1

    print(f'Средняя величина дохода сотрудников: {int(my_sal/line_count)} руб.')
