# Декоратор - это функция, которая в качестве аргумента принимает другую функцию и возвращает функцию-замыкание.
# Декораторы нужны для расширения функционала переданной функции за счет обертки в замыкании.
# Но при обычном создании декораторы вы потеряете имя свой оригинальной функции, и также ее документацию.
# В видео я покажу как сохранить имя декорируемой функции и строку документации
from functools import wraps


def decor(func):
    @wraps(func)  # будет отображать данные как если бы были строки 15,16
    def inside(*args, **kwargs):
        print('1 decor')
        func(*args, **kwargs)
        print(('2 decor'))

    # inside.__name__ = func.__name__  # в этой строке и ниже (до return) можно сказать что имя и докум.будут с func(Name)
    # inside.__doc__ = func.__doc__    или то что мы сделали в 5-й и 9-й строке
    return inside


@decor  # повесили функцию Name внутрь функции decor
def Name(surname, name):
    """
    Функция передаёт привет фамилия имя
    :param surname:
    :param name:
    :return:
    """
    print('Hello ', surname, name)


Name('Asm', "And")  # 1 decor  Hello  Asm And  2 decor

help(Name)  # вывод данных о ней
