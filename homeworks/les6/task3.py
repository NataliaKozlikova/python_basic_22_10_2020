"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
(должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position
(должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера
на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._income = {'wage': 0, 'bonus': 0}

    def get_full_name(self):
        return f'{self.surname}, {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


class Position(Worker):
    def __init__(self, position: str, name: str, surname: str, wage: int, bonus: int):
        self.position = position
        super().__init__(name, surname)
        self._income['wage'] = wage
        self._income['bonus'] = bonus


if __name__ == '__main__':
    a = Position('секретарь', 'Ольга', 'Иванова', 50000, 25000)
    print(a.position)
    print(a.get_full_name())
    print(a.get_total_income())