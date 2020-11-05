"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def insert_sum(*args):
    """
    the sum of list items, setting the character to exit the program
    :param args: list
    :return: sum args, exit character
    """
    result = 0
    exit_flag = False
    for itm in args:
        try:
            result += float(itm) if itm else 0
        except ValueError:
            if itm == 'q':
                exit_flag = not exit_flag
                break
    return result, exit_flag


user_sum = 0
while True:
    user_input = input('введите числа через пробел\n>>>').split(' ')
    result_sum, user_exit = insert_sum(*user_input)
    user_sum += result_sum
    print(f'сумма: {user_sum}')

    if user_exit:
        print('До свиданья!')
        break