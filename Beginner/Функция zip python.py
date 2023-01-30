"""
видео вы узнает что такое функция zip и что она делает. как работает функция zip в Python
Функция zip принимает на вход несколько итерабельных последовательностей, и возвращает итератор zip object.
zip object будет состоять из кортежей, и в каждый такой кортеж будут входить элементы коллекций,
имеющие одинаковый индекс.
Рассмотрим примеры использования функции zip с двумя коллекциями
Рассмотрим примеры использования функции zip с двумя коллекциями разной длины
Рассмотрим примеры использования функции zip с 3 коллекциями разной длины (определение по наименьшей коллекции)
Разберем как можно из объекта zip вновь получить наши коллекции
Про распаковка при помощи звездочки * можно посмотреть здесь
https://www.youtube.com/watch?v=mcAB5...
"""
a = [1, 2, 3, 5]
b = [12, 14, 16, 20]
c = 'asd'
for i in range(4):  # вывод первых элементов с 2-х списков
    print(a[i], b[i])  # 1 12 2 14 3 16 5 20

rez = list(zip(a, b, c))  # zip создаст кортеж из итерации элементов (a,b) и запишет их в список
print(rez)  # [(1, 12, 'a'), (2, 14, 's'), (3, 16, 'd')] поскольку в c нет последнего элемента, то вывод 3-х элементов

# можно присвоить сразу переменным
for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)  # 1 12 a
    # 2 14 s
    # 3 16 d

# можно получить списки из кортежа zip (* распакует кортеж)
col_1, col_2, col_3 = zip(*rez)
print(col_1, col_2, col_3)  # (1, 2, 3) (12, 14, 16) ('a', 's', 'd')
