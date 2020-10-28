"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
while True:
    user_num = input("Введите целое число\n>>>")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Ошибка! Введено не число')

count = 0
category = user_num

while category:
    category //= 10
    count += 1

nn_multi = 10 ** count + 1
nnn_multi = 10 ** (count * 2) + nn_multi
result = user_num + (user_num * nn_multi) + (user_num * nnn_multi)

print(result)

"""
# Вариант 2

user_num = input("Введите целое число\n>>>")
result = int(user_num) + int(user_num * 2) + int(user_num * 3)

print(result)
"""