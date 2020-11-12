"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task4.txt')
file_path_new = os.path.join(os.path.dirname(__file__), 'task4_new.txt')

num_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open(file_path, 'r', encoding='UTF-8') as file, open(file_path_new, 'w', encoding='UTF-8') as file_new:
    idx = 1
    for line in file:
        my_line = line.split()
        my_line.remove(my_line[0])
        my_line.insert(0, num_dict[idx])
        file_new.write((' '.join(my_line)) + '\n')
        idx += 1
