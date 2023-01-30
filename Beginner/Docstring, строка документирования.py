help(abs)  # покажет что делает встроенная функция abs(x, /) Return the absolute value of the argument.
print(abs.__doc__)  # покажет что делает встроенная функция Return the absolute value of the argument.


def KakayatoFunction(c):
    # комментарий не влияет на первую строку поскольку Python его не видит
    # если поставить """enter""" то программа сама предложит :param c:  и :return:
    """
    Наша функция которая ничего не далает, но в ней можно описать что
    она должна делать и это увидеть в help или .__doc__
    :param c:
    :return:
    """
    a = 12 * 123
    b = (23 * a) / c
    return b


help(KakayatoFunction)  # если нет первой строки,то ничего не будет.Если есть то обычно это описание функции
print(KakayatoFunction.__doc__)  # Наша функция которая ни... (отображается только 1-я строчка после комментария)

import random  # выделить слово и нажать ctrl+q или если зажать ctrl+левой мышкой мы "провалимся" в этот метод
