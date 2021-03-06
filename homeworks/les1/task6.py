"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена
составить не менее b километров. Программа должна принимать
значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
while True:
    day_result = input('Сколько километров пробежал спортсмент в 1-й день?\n>>>')
    if day_result.isdigit():
        day_result = int(day_result)
        break
    print('Ошибка! Введено не число')

while True:
    reach_result = input('Какого результата ему нужно достичь в км?\n>>>')
    if reach_result.isdigit():
        reach_result = int(reach_result)
        break
    print('Ошибка! Введено не число')

day_count = 1

print('Результат:')

while reach_result > day_result:
    print(f'{day_count}-й день: {round(day_result,2)} км')
    day_result *= 1.1
    day_count += 1

print(f'{day_count}-й день: {round(day_result,2)} км')

print(f'на {day_count}-й день спортсмен достиг результата — не менее {int(day_result)} км')