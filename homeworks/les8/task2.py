"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt=''):
        self.txt = txt


while True:
    try:
        user_div = float(input('Введите число (делимое) \n>>>'))
        user_divr = float(input('Введите число (делитель) \n>>>'))

        if user_divr == 0:
            raise OwnError('На ноль делить нельзя')

        result = user_div / user_divr
        print(f'{user_div} / {user_divr} = {result}')
        break
    except ValueError:
        print('Вы ввели не число')
    except OwnError as err:
        print(err)
