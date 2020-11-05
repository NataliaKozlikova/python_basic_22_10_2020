"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_min(a: list) -> float:
    """
    finds the minimum element in the list
    :param a: list
    :return: min item
    """
    a.sort()
    return a[0]


def my_max(a, b, c) -> float:
    """
    finds the minimum argument
    :param a: float
    :param b: float
    :param c: float
    :return: max argument
    """
    args = [a, b, c]
    args.sort()
    args.reverse()
    return args[0]


def my_sum(a: list) -> float:
    """
    sum of items in the list
    :param a: list
    :return: sum items
    """
    sum_el = 0
    for itm in a:
        sum_el += itm
    return sum_el


def my_func(a, b, c):
    """
    sum of the largest arguments
    :param a: float
    :param b: float
    :param c: float
    :return: sum of the largest arguments
    """
    args = [a, b, c]
    return my_sum(args) - my_min(args)


my_func2 = lambda a, b, c: my_max(a + b, b + c, c + a)


assert my_func(12, 1, 3) == 15
assert my_func2(4, 8, 9) == 17
