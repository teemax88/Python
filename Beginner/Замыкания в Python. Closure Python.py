# В данном уроке поговорим о том, что такое замыкания (closures)
# Для создания замыкания нам понадобиться создать вложенную функцию, которая будет использовать переменную,
# объявленную за ее пределами
# если Return нет в функции, то по умолчанию return = None

def main_func():
    def in_function():
        print('Печать со встроенной функции in_function ')

    in_function()


main_func()  # Печать со встроенной функции in_function


def main_func1(name):
    # name = 'Андрей'
    def in_function():
        print('Привет мой друг', name)  # использовали замыкание (переменную name не внутри функции)

    return in_function


b = main_func1('Andrey')  # в переменную b присвоили результат функции (b стала функцией)
b()  # Привет мой друг Андрей или Привет мой друг Andrey (если нет 17-й строки)


# вложенная функция которая прибавляет значения с 2-х переменных
def adder(value):
    def inner(invalue):
        print(value + invalue)

    return inner


r = adder(3)  # в переменную(функцию) r записали value=3
r(5)  # 8 ответ поскольку invalue=5 подставили в функцию adder
r(2)  # 5 ответ поскольку invalue=2 подставили в функцию adder
z = adder(12)
z(7)  # 19 ответ поскольку invalue=7 подставили в функцию adder
z(3)  # 15 ответ поскольку invalue=3 подставили в функцию adder


# функция счётчик (сколько раз вызывалась эта функция)
def counter():
    count = 0

    def incounter():
        nonlocal count  # покажет что пользоваться нужно переменной в 46-й строке и изменять её
        count += 1
        return count

    return incounter


w = counter()
print(w())  # вызов 1 раз
print(w())  # вызов 2 раза
y = counter()  # при присвоении в новую переменную счётчик сброситься
print(y())  # вызов 1 раз
