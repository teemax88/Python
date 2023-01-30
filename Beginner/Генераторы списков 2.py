a = [  # создали список кортеж
    ('Asmolovskiy', 1983),
    ('Lukov', 2002),
    ('Petrov', 1991)
]
#
print(a[2][0])  # выведет Petrov
b = [i[0] for i in a]
print(b)  # вывод ['Asmolovskiy', 'Lukov', 'Petrov']
c = [i[0] for i in a if i[0].startswith('A')]
print(c)  # вывод ['Asmolovskiy'] сверху добавит слово в список с если оно начинается на 'A'
d = [i[0] for i in a if i[1] > 1990]
print(d)  # вывод ['Lukov', 'Petrov'] сверху добавит слово в список d если i[1] больше 1990
e = [i[0][0] for i in a if i[1] > 1990]
print(e)  # вывод ['L', 'P'] сверху добавит первую букву в слове в список e если i[1] больше 1990

a = {  # создали словарь (в котором ключ = фамилия, значение= вложенный словарь состоящий из 3-х ключей(age,hobby,car)
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
}
b = [i for i in a]
print(b)  # ['Sidorov', 'Lukov', 'Petrov'] выведет ключи переменной а
c = [a[i] for i in a]
print(c)  # [{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'}, {'age': 2002, и т.д. выведет все элементы
d = [a[i]['car'] for i in a]
print(d)  # ['BMW', 'Opel', 'BMW'] выведет ключи car
e = [a[i]['car'] for i in a if a[i]['age'] > 1993]
print(e)  # ['BMW', 'Opel'] выведет ключи car если age > 1993
e1 = [(i, a[i]['car']) for i in a if a[i]['age'] > 1993]  # не забудь про ()
print(e1)  # [('Sidorov', 'BMW'), ('Lukov', 'Opel')] выведет фамилию и ключи car если age > 1993
e2 = [(i, a[i]['car']) for i in a if a[i]['age'] > 1993 and a[i]['hobby'] == 'soccer']  # не забудь про ()
print(e2)  # [('Sidorov', 'BMW')] выведет фамилию и ключи car если age > 1993 и hobby = soccer

s = 'asdgqdsA22ASDGAGAHfgsfsdflk;lm,;64'  # создали строку
s1 = [int(i) for i in s if i.isdigit()]  # в список попадут только цифры (isdigit()), isalpha() будут только буквы
print(s1)  # ['2', '2', '6', '4'] если не делать int(i) и [2, 2, 6, 4]

# заполним список (n строк, m столбцов) случайными числами от -10 до 10
import random

n = 4
m = 4
w = [[random.randint(-10, 10) for j in range(m)] for i in
     range(n)]  # для каждого значения i(n раз) будет формир.генератор слева
print(w)  # [[-1, -7, 10, 5], [-7, -5, -3, 5], [5, 8, -2, 3], [0, 5, -6, 4]]
w1 = [w[i][j] for i in range(n) for j in range(m) if i == j]
print('Главная диагональ ', w1)  # [-1, -5, -2, 4] вывод только главной диагонали
w2 = [w[2][j] for j in range(m)]
print('Вторая строка ', w2)  # [5, 8, -2, 3] вывод только 2й строки
w3 = [w[i][0] for i in range(n)]
print('Нулевая столбец ', w3)  # [-1, -7, 5, 0] вывод только 0й столбец

t1 = 5  # сделаем таблицу умножения
t2 = 5
t = [[i * j for i in range(1, t1 + 1)] for j in range(1, t2 + 1)]  # если не вводить внутренние [] будет в 1-м списке
for i in t:
    print(i)  # [1, 2, 3, 4, 5] вывод
    # [2, 4, 6, 8, 10]
    # [3, 6, 9, 12, 15]
    # [4, 8, 12, 16, 20]
    # [5, 10, 15, 20, 25]
