def f(a, b):  # хотя изначально подставяться 20 и 50 , но потом изменяться на 100 и 200
    a = 100
    b.append(7)
    b[0] = 11
    print(a, b, 'local')  # 100 [11, 2, 3, 7] local
    print(id(a), id(b), 'local')  # 3016917912912 3016919281408 local local ID в памяти наших переменных


c = 'asd'
d = [1, 2, 3]
print(id(c), id(d), 'global')  # 3016919200880 3016919281408 global ID в памяти наших переменных
f(c, d)
# f(c, d[:]) # если так то передаст копии и d список не изменится (вывод ниже будет asd [1, 2, 3] global)
print(c, d, 'global')  # asd [11, 2, 3, 7] global d измениться с помощью b (так как это список)


def example(a, b, c):
    print(a, b, c)


# позиционный метод
example(1, 3, 5)  # 1 3 5 вывод, если ввести меньше или больше переменных то будет ошибка

# метод по имени
example(c=21, b=23, a=5)  # 5 23 21

# комбинированный метод
example(12, c=2, b=33)  # 12 33 2 , в а пойдёт первое значение, остальные названы


# значения по умолчанию
def example1(a, b='UPS', c='unknown'):  # ! в функции можно сначала заданные переменные, а потом можно по умолчанию
    print(a, b, c)


example1(1, 2)  # 1 2 unknown если значение с не задано, то оно будет взято по умолчанию ('unknown')
example1(3, 4, 6)  # 3 4 6 если значение с задано, то оно будет перезаписано
example1(3, c=123)  # 3 UPS 123 a-задали, b-по умолчанию, с-задали (хотя было по умолчанию)


# не используй изменяемые объекты(списки, словари) в качестве значений по умолчанию

def append_to_list(value: int, my_list: list = None):
    " функция добавляет число в список"
    if my_list is None:  # проверит если не задан список, то он снова будет его обнулять и добавлять к пустому
        my_list = []
    my_list.append(value)
    print(my_list)


a = [1, 2, 3]
append_to_list(10, a)  # [1, 2, 3, 10]
append_to_list(15, a)  # [1, 2, 3, 10, 15] # 10 добавилась в а и сохранилась там с прошлым вызовом функции
append_to_list(2)  # [2] добавит 2 к пустому списку
append_to_list(34)  # [34] добавит 34 к пустому списку (а не обновит my_list)


# тоже самое со словарями
def append_to_dict(key, value, my_dict=None):
    " функция добавляет число в словарь"
    if my_dict is None:  # проверит если не задан словарь, то он снова будет его обнулять и добавлять к пустому
        my_dict = {}
    my_dict[key] = value
    print(my_dict)


append_to_dict(10, 'asdf')  # {10: 'asdf'} ключ 10, значение 'asdf'
append_to_dict(1, 200)  # {10: 'asdf', 1: 200} если нет 61,62 строки   и {1: 200} если 61,62 строки активны
append_to_dict(15, 'Andrey', {34: 'wetwe'})  # {34: 'wetwe', 15: 'Andrey'}
