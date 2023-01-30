"""
Сортировка списков Python 3. Методы sort и sorted
В видео познакомимся как сортировать списки и другие коллекции в Python.
Аргумент key позволяет выполнить сортировку по ключу
В  Аргумент key  вы должны передать объект-функцию, по результат которой будет выполнена сортировка.
В  Аргумент key можно передавать:
1) встроенные функции
2) собственные функции
3) встроенные методы объектов
4) анонимные функции lambda
Сортировка списка при помощи метода sort
Сортировка списка по возрастанию элементов
Сортировка списка по убыванию элементов
Сортировка строки при помощи функции sorted
Сортировка кортежа при помощи функции sorted
"""
# Аргумент key - встроенная функция:

a = [4, -10, 43, -300, 54, 289, -34, -8, 749]
print(sorted(a))  # [-300, -34, -10, -8, 4, 43, 54, 289, 749] стандартная сортировка
print(sorted(a, key=abs))  # [4, -8, -10, -34, 43, 54, 289, -300, 749] сортировка элементов по модулю

b = []  # записал в b отсортированный список а по модулю
for i in range(len(a)):
    b.append(abs(a[i]))
b.sort()
print(b)  # [4, 8, 10, 34, 43, 54, 289, 300, 749]


# Аргумент key - собственная функция:

def last(x):  # функция вернёт последнюю цифру от числа
    return x % 10, x // 10 % 10


# если сделать return -(x % 10), то сортировка в 34-й строке будет по убыванию, сначала выполнит возврат последней цифры
# x % 10 и если результат будет одинаковый, то возврат будет по предпоследней x // 10 % 10

print(sorted(b, key=last))  # [10, 300, 43, 4, 34, 54, 8, 289, 749] сортировка по последней цифре при return x % 10
print(sorted(b, key=last))  # [300, 10, 43, 4, 34, 54, 8, 749, 289]по последн.и предпоследн.return x % 10, x // 10 % 10

# Аргумент key - встроенные методы объектов:

f = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(f))  # ['BBB', 'DDD', 'ZZZ', 'aaa', 'eee', 'www'] сортировка сначала заглавные, потом маленькие
print(sorted(f, key=str.lower))  # ['aaa', 'BBB', 'DDD', 'eee', 'www', 'ZZZ'] перед сравнением все буквы станут мален.

# Аргумент key - анонимная функция lambda:

q = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(sorted(q, key=lambda x: int(x.split()[1])))  # ['www 14', 'eee 43', 'BBB 43', 'aaa 45', 'ZZZ 800', 'DDD 800']
# split разобьёт на 'ZZZ' и '79' возьмём[1] т.е. число '79' и представим чтобы сравнить как int
print(sorted(q, key=lambda x: (int(x.split()[1]), x.split()[0].lower())))
# ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'DDD 800', 'ZZZ 800']
# split разобьёт на 'ZZZ' и '79' возьмём[1] т.е. число '79' и представим чтобы сравнить как int
# затем если по числам они равны, то применим 2-е условие - сравним [0] элементы(слова с мален.)всё должно быть в
# скобках поскольку lambda принимает только один аргумент (мы его представили как кортеж) и lower тоже со скобками

# если (-int(x.split()[1]) , то числа отсортируются по убыванию

# если числа по возрастанию, а буквы по убыванию, то нужно дважды создать сортировку
w = ['ZZZ 800', 'aaa 45', 'eee 43', 'AaA 800', 'BBB 43', 'AAA 14']
w_1 = sorted(w, key=lambda x: (int(x.split()[1])))
print(sorted(w_1, key=lambda x: (x.split()[0].lower()), reverse=True))
# ['ZZZ 800', 'eee 43', 'BBB 43', 'AAA 14', 'aaa 45', 'AaA 800']

print(sorted(q, key=lambda x: (int(x.split()[1]), x.split()[0].lower()), reverse=True))
# ['ZZZ 800', 'DDD 800', 'aaa 45', 'eee 43', 'BBB 43', 'www 14'] сортировка чисел и слов по убыванию
