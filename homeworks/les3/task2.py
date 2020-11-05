"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def client_info(name: str,
                surname: str,
                birth_year: int,
                city: str,
                email: str,
                phone: int
                ):
    """
    displays information about the user on the screen
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: None
    """
    return f"{name} {surname} {birth_year} г.р., проживает в {city}. Контакты: {email}, {phone}"


print(client_info(name='Иван', surname='Петров', birth_year=2001, city='Москва', email='ivanpetrov@mail.ru',
                  phone=9031256798))
