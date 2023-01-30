# В данном уроке поговорим о том, что такое замыкания (closures)
# Для создания замыкания нам понадобиться создать вложенную функцию, которая будет использовать переменную,
# объявленную за ее пределами

# функция будет считать среднее-арифметическое
def sr_arifm():
    sp_numbers = []  # создали пустой список в который будем добавлять числа

    def num(number):
        sp_numbers.append(number)
        print(sp_numbers)
        return sum(sp_numbers) / len(sp_numbers)

    return num


a = sr_arifm()
print(a(3))  # [3] 3.0
print(a(12))  # [3, 12] 7.5
# если вызовем функцию sr_arifm() ещё раз то будет опять новый список
b = sr_arifm()
print(b(34))  # [34]  34.0


# можно написать такую же функцию, но брать мы будем переменные а не список
# функция будет считать среднее-арифметическое
def sr_arifm1():
    summa = 0
    count = 0

    def num1(number1):
        nonlocal summa, count  # если не поставить, то переменные не смогут записывать во внешние области
        summa += number1
        count += 1
        return summa / count

    return num1


q1 = sr_arifm1()
print(q1(23))  # 23.0
print(q1(4))  # 13.5

# напишем функцию которая будет считать сколько времени прошло между вызовами функции
from datetime import datetime  # показывает текущее время


def data():
    start = datetime.now()

    def timer():
        return datetime.now() - start

    return timer


e = data()
e()  # в консоли datetime.timedelta(seconds=18, microseconds=389034) разница между вызовом в первый раз и е()


# подставим в значения функции 1-ю функцию и веведем текст который будет считать сколько раз мы её вызвали
def plus(a, b):
    return a + b


def umnogenie(a, b, c):
    return a * b * c


def counter(value):
    count = 0

    def inner(*args, **kwargs):  # можно только *args поскольку нам поступали только кортежи
        nonlocal count
        count += 1
        print(f"Функция {value.__name__} вызывалась {count} раз")  # .__name__ нужно чтобы вывести название функции
        return value(*args, **kwargs  # можно только *args поскольку нам поступали только кортежи

    return inner


t = counter(plus)
print(t(12, 5))  # Функция plus вызывалась 1 раз  17 (12 и 5 подставяться вместо a,b)
u = counter(umnogenie)
print(u(3, 5, 7))  # Функция umnogenie вызывалась 1 раз 105 (3, 5 , 7 подставяться вместо a,b,c)
