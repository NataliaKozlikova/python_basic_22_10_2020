"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

my_list = [4, 6, 4, 76, -3, 3, 5, 9, 65, 100, 5, 9]
result = [itm for itm in my_list if my_list.count(itm) == 1]
print(result)
assert result == [6, 76, -3, 3, 65, 100]
