"""
5.Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""
while True:
    proceeds = input("Введите сумму выручки в руб.\n>>>")
    if proceeds.isdigit():
        proceeds = int(proceeds)
        break
    print('Ошибка! Введено не число')

while True:
    cost = input("Введите сумму издержек в руб.\n>>>")
    if cost.isdigit():
        cost = int(cost)
        break
    print('Ошибка! Введено не число')

fin_result = proceeds - cost

if fin_result > 0:
    ratio = proceeds / cost
    print(f'Ваша прибыль составила: {fin_result} руб.\nрентабельность: {ratio}')
    while True:
        worker_count = input('Введите количество сотрудников\n>>>')
        if worker_count.isdigit():
            worker_count = int(worker_count)
            break
        print('Ошибка! Введено не число')
    profit_workers = fin_result // worker_count
    print(f'Прибыль на одного сотрудника составляет: {profit_workers} руб.')

elif not fin_result:
    print('фирма сработала с нулевым результатом')

else:
    print(f'Издержки превысили выручку! Убытки составили: {fin_result} руб.')
