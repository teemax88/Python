import math

a = math.trunc(32.3)
print(a)    # ответ 32 ##trunc отсекает дробную часть числа
# (в функции может быть только 1 число)

b = int(32.234)
print(b)    # ответ 32 ##тоже самое что trunc только без импорта math(приводит число к int)

c = math.floor(32.987)
print(c)    # ответ 32 (с отрицанием следующее меньшее целое число) ##floor округление вниз

c = math.floor(-32.987)
print(c)    # ответ -33
# math.floor (5) будет 5 поскольку 5 уже целое ближайшее меньшее число

s = math.ceil(3.234)
print(s)    # ceil округление в большую сторону (ответ 4)

s = math.ceil(-3.234)
print(s)    # ceil округление в большую сторону (ответ -3)

# например
print(math.ceil(10 / 3))  # ответ 4 (10/3=3.33 в большую сторону=4)
print(math.floor(10 / 3))  # ответ 3 (10/3=3.33 в меньшую сторону=3)
print(math.trunc(10 / 3))  # ответ 3 (10/3=3.33 отсекли дробную часть=3)
