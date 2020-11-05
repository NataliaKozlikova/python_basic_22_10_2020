"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать  в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x: float, y: int) -> float:
    """
    raise x to a power y
    :param x: float
    :param y: int
    :return: x to the power of y
    """
    return x ** y


def my_func2(x: float, y: int) -> float:
    """
    raise x to a power y
    :param x: float
    :param y: int
    :return: x to the power of y
    """
    result = 0
    for _ in range(abs(y)):
        result += x
    return result if y > 0 else 1 / result


assert my_func(2, -2) == 0.25
assert my_func2(2, -4) == 0.125
