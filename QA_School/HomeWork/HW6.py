"""Напишите программу/функцию, которая печатает объекты списка один за другим.
В качестве входных данных используйте список.
например print_entities(["a", "b", "c"]) должен возвращать:
"a"
"b"
"c"
"""
abc = ["a", "b", "c"]


def print_entities(text):
    for i in text:
        print(f'"{i}"')


print_entities(abc)

"""Напишите программу/функцию, которая преобразует строки в кортежи.
например convert("abide") должен возвращать кортеж, например:
("a", "b", "i", "d", "e")
"""


def convert(text):
    line_tuple = tuple(text)
    return line_tuple


print(convert("abide"))

"""Напишите программу/функцию, которая удаляет дубликаты и возвращает только уникальные значения
в виде списка.
например remove_dups("abcdadab") должен возвращать ["a", "d", "c", "b"].
Обратите внимание, порядок элементов в списке не важен!
"""


def remove_dups(text):
    new_text = set(text)
    return list(new_text)


print(remove_dups("abcdadab"))

"""Напишите программу/функцию, которая собирает определенные данные в качестве параметров и
возвращает объект словаря.
например client("John", "Doe", "23.01.1934", "Мужчина", "Сан-Антонио", "TX", "78261")
должен возвращать объект словаря, например:
{
    "Name": "John",
    "Lastname": "Doe",
    "DOB": "01/23/1934",
    "Sex": "Male",
    "City": "San Antonio",
    "State": "TX",
    "ZipCode": "78261"
}
"""


def create_client_object(name, last_name, dob, sex, city, state, zip_code):
    client = {
        "Name": name,
        "LastName": last_name,
        "DOB": dob,
        "Sex": sex,
        "City": city,
        "State": state,
        "ZipCode": zip_code
    }
    return client


print(create_client_object("John", "Doe", "23.01.1934", "Мужчина", "Сан-Антонио", "TX", "78261"))
print(type(create_client_object))
