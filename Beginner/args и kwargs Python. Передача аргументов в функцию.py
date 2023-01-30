# * может использоваться в присвоении переменных (если * есть, то будет присвоен список из значений) и может быть 1-а

a, b, c = 5, 8, 'asd'  # print((a, b, c)) = (5, 8, 'asd')
a, b, c = [12, True, 'dfg']  # print((a, b, c)) = (12, True, 'dfg')
# a, b, c = [True, 7, 12, 2.23, 'wer', 3] # print((a, b, c)) = ошибка поскольку переменных 3, а значений 6
a, *b, c = [True, 7, 12, 2.23, 'wer', 3]  # print((a, b, c)) = (True, [7, 12, 2.23, 'wer'], 3)
a, b, *c = [True, 7, 12, 2.23, 'wer', 3]  # print((a, b, c)) = (True, 7, [12, 2.23, 'wer', 3])
*a, b, c = (5, 8)  # print((a, b, c)) = ([], 5, 8) в а запись пустого списка
print((a, b, c))

# * помогает распаковать списки, кортежи и т.д.
w = [1, 2, 45]
print(*w)  # 1 2 45 распаковал список при выводе

s = [4, 10]
print(list(range(1, 5)))  # [1, 2, 3, 4] вывод списка от 1го до 4-х
# print(list(range(s))) # TypeError поскольку программа не может распаковать наш список s и подставить значения
print(list(range(*s)))  # [4, 5, 6, 7, 8, 9] вывод списка от 4-х до 9-ти


def fun(a, b, c, d):
    print(a, b, c, d)


fun(1, 2, 3, 4)  # 1 2 3 4
a = ('asd', True, 78, [3, 4, 5])
# fun(a) # ТypeError поскольку программа не может распаковать наш кортеж а и подставить значения
fun(*a)  # asd True 78 [3, 4, 5]


# * в функции поможет из полученных элементов создать кортеж tuple (*args)

def cort(*args):
    print(args, type(args))
    # посчитает сумму кортежа
    s = 0
    for i in args:
        s += i
    return s


cort(1, 34, 5, 7, 89)  # (1, 34, 5, 7, 89) <class 'tuple'>
print(cort(1, 34, 5, 7, 89))  # 136 сумма кортежа


# ** в функции поможет из полученных элементов создать словарь (**kwargs)

def dict_1(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


dict_1(a=23, b=12)  # {'a': 23, 'b': 12} <class 'dict'> создаст словарь и потом выведет а 23  b 12


def dict_tuple(*args, **kwargs):  # преобразует значения в кортеж, а именные значения в словарь
    print(args, kwargs)


dict_tuple(1, 23, 45, 23, 'asd', a=12, b=3, c=45)  # (1, 23, 45, 23, 'asd') {'a': 12, 'b': 3, 'c': 45}

print(1, 2, 3, 'asd', sep='  ', end='!')  # 1  2  3  asd!


def out_print(*args, sep='#', end='$'):
    print(args, sep, end)


out_print(1, 2, 3, 'asd', sep=90)  # (1, 2, 3, 'asd') 90 $ (sep заменился на 90 а не был взят по умолчанию)
