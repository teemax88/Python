import sys


# print(sys.getrecursionlimit())  # после импорта покажет сколько рекурсий поддержит программа (1000 по умолчанию)
# sys.setrecursionlimit(2000)  # установит новый предел рекурсии
# print(sys.getrecursionlimit())  # после импорта покажет сколько рекурсий поддержит программа (2000)

# найдёт пробелы
def find_probel(x):
    count = 0
    if len(x) == 0:
        return count
    if x[0] == ' ':
        count = 1
    return count + find_probel(x[1:])


print(find_probel('asd asd as wer er'))


# факториал
def fact(a):
    if a <= 0:
        return 1
    return a * fact(a - 1)


print(fact(5))


# функция преобразует с рекурсией любой сложности список к простому списку

def flatten(base_list, total_list=None):
    if total_list == None:  # точка окончания цикла (рекурсии)
        total_list = []
    for elem in base_list:  # прошли в цикле по всему списку
        if type(elem) == list:  # если элемент список,то
            flatten(elem, total_list)  # то возьмём функцию от элемента
        else:
            total_list.append(elem)  # если элемент не список(число), то добавим его в новый список
    return total_list  # результат наш новый список из чисел


print(flatten([1, [2, 3, [4]], 5]))
print(flatten([[[[9]]], [1, 2], [[8]]]))  # [9, 1, 2, 8]


# или так проще
def flatten(base_list):
    for elem in base_list:  # прошли в цикле по всему списку
        if type(elem) == list:  # если элемент список,то
            flatten(elem)  # то возьмём функцию от элемента
        else:
            total_list.append(elem)  # если элемент не список(число), то добавим его в новый список
    return total_list  # результат наш новый список из чисел


total_list = []
print(flatten([1, [2, 3, [4]], 5]))  # [1, 2, 3, 4, 5]
total_list = []
print(flatten([[[[9]]], [1, 2], [[8]]]))  # [9, 1, 2, 8]
