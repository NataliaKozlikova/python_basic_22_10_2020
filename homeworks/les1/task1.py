"""
1.Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""
variable_str = "Привет!"
variable_int = 10
variable_float = 15.5

print(variable_str)
print(variable_int)
print(variable_float)

user_name = input('Введите ваше имя\n>>>')
user_surname = input('Введите вашу фамилию\n>>>')
user_age = input("Введите ваш возраст\n>>>")

print('Привет, {0} {1}! Ваш возраст {2}'.format(user_name, user_surname, user_age))
