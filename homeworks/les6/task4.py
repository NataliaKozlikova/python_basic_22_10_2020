"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


def go():
    print('Машина поехала')


def stop():
    print('Машина остановилась')


def turn(direction):
    if direction in ('Направо', 'Налево'):
        print(f'Машина повернула {direction}')
    else:
        raise ValueError('Направление движения только направо или налево')


class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.speed} км.ч')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        self.is_police = is_police
        super().__init__(color, name, True)


if __name__ == '__main__':
    a = TownCar('Черный', 'Ford')
    a.speed = 70
    print(a.color, a.name, a.show_speed())
    b = PoliceCar('Синий', 'Тойота', False)
    print(b.color, b.name)
