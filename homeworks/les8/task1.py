"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def date_to_int(cls, date_str):
        return [int(itm) for itm in date_str.split('-')]

    @staticmethod
    def date_valid(date_str):
        date_valid = [int(itm) for itm in date_str.split('-')]
        # валидация проводится по одному из вариантов для числа, месяца и года
        if (date_valid[1] not in range(1, 13)) or \
                (date_valid[0] not in range(1, 32)) or \
                (date_valid[2] not in range(1, 2021)):
            return f'Неверный формат даты'
        else:
            return f'Дата указана корректно'


print(Date.date_to_int('21-12-2020'))
print(Date.date_valid('01-12-2020'))
