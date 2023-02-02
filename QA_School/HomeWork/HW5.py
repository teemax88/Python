"""Напишите функцию для сравнения двух чисел.
Например. compare(2, 3) должен возвращать False, иначе должен возвращать True."""


def compare(x, y):
    if x > y:
        print(True)
    else:
        print(False)


compare(4, 3)

"""Измените предыдущую функцию, чтобы сравнивать только положительные числа.
В случае отрицательных чисел он вернет оператор печати, 
например: «Можно сравнивать только положительные числа!»."""


def compare(x, y):
    if x > 0 and y > 0:
        if x > y:
            print(True)
        else:
            print(False)
    else:
        print("Можно сравнивать только положительные числа!")


compare(5, 3)

"""Напишите функцию для суммирования двух чисел.
Например. add(4, 5) в результате должен вернуть 9."""


def add(x, y):
    z = x + y
    return z


print(add(8, 5))

"""Напишите функцию для вычитания 2 чисел.
Например. sub(4, 2) в результате должен вернуть 2."""


def sub(x, y):
    z = x - y
    return z


print(sub(8, 5))

"""Напишите функцию, которая возвращает тип ввода.
Например. give_a_type("test") должен возвращать оператор печати, например: "string"."""


def give_a_type(test):
    print(type(test))


give_a_type(45.2)

"""Напишите функцию, которая печатает ввод вертикально.
Например. print_vertical("test me please") должен вернуть:
    t
    e
    s
    t
    
    m
    e
    
    p
    l
    e
    a
    s
    e"""


def print_vertical(text):
    for i in text:
        print(i)


print_vertical("test me please")

"""Напишите функцию, которая объединяет 2 строки.
Например. concat("abc", "123") должен возвращать оператор печати, например: "adc123"."""


def concat(text_1, text_2):
    print(text_1 + text_2)


concat("abc", "123")
