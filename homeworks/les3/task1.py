"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def my_division(a: float, b: float) -> float:
    """
    the division of a by b
    :param a: float
    :param b: float
    :return: a / b
    """
    while True:
        try:
            return a / b
        except ValueError:
            print('Введено не число!')
            continue
        except ZeroDivisionError:
            return float('nan')


assert my_division(12, 4) == 3
assert my_division(1, 0) * 0
