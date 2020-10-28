"""
4.Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
while True:
    user_num = input("Введите целое число\n>>>")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Ошибка! Введено не число')

result = 0
while user_num and result != 9:
    tmp = user_num % 10
    if tmp > result:
        result = tmp
    user_num //= 10

print(result)