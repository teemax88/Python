# локальная переменная - внутри функции (существует только в функции)
# глобальная переменная - по всей программе (и внутри функции тоже)
# встроенные переменные - те, которые уже есть print, abs, input и т.д

def variable():  # название функции это глобальная переменная
    a, b, c = 1, 2, 4  # локальные переменные
    w = 'локальная'
    print(a, b, c, w, y)  # если есть локальная w то программа будет выводить её,если нет то глобальную


w = 'глобальная'  # глобальные переменные
y = 100  # глобальные переменные
print(w)  # вывод глобальная (переменная глобальная)
variable()  # вывод функции и вывод 1 2 4 локальная 100


def s(a, b, c):  # название функции это глобальная переменная
    # local
    # global a # при такой записи изменения которые были сделаны с а будут изменены и в глобальной а
    a = 30
    # a[1] = 77
    print(a, b, c, 'local')


# global
a = [1, 2, 3]
b = 200
c = 300
s(a, b, c)  # 30 200 300 local переменная а заменена на локальную(если 20я строка вместо 19й [1, 77, 3] 200 300 local)
print(a, b, c, 'global')  # [1, 2, 3] 200 300 global переменная а взята глобальная


# если 20я строка вместо 19й то вывод [1, 77, 3] 200 300 global поскольку список это изменяемый объект и
# если он изменился в локальной области, то поменялся и в глобальной

def Square(x):
    return x ** 2


input = Square  # встроенная
print(input(3))  # ответ 9 поскольку в input было присвоено результат функции Square(и input перестал вводить с клавы)


def example():
    r = 100  # local значение

    def example_in():
        # nonlocal r # если строка активная, то возьмёт r = 'asd'
        r = 'asd'  # enclosing значение
        print(r, t, 'ex_in')  # вывод asd 5 ex_in

    example_in()
    print(r, t, 'example')  # вывод 100 5 example


r = 333  # global значение
t = 5
example()
