"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os
import random

file_path = os.path.join(os.path.dirname(__file__), 'task5.txt')

num_rand = [random.randint(1, 20) for _ in range(random.randint(10, 30))]

with open(file_path, 'w', encoding='UTF-8') as file:
    num_rand_str = ' '.join(map(str, num_rand))
    file.write(num_rand_str)

with open(file_path, 'r', encoding='UTF-8') as file:
    numbers = map(int, file.read().split(' '))

print(sum(numbers))
