"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_list = input('Введите несколько слов разделенных пробелами\n>>>')
user_list = user_list.split(' ')

for ind, word in enumerate(user_list):
    print(f'{ind}:{word[:10]}')
