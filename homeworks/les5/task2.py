"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os

file_path = os.path.join(os.path.dirname(__file__), 'task2.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    line_count = len(file.readlines())
    print(f'Количество строк в файле: {line_count}')

    file.seek(0)

    idx = 1
    while idx <= line_count:
        word_count = len(file.readline().split(' '))
        print(f'В {idx} строке {word_count} слов')
        idx += 1
