if 4 > 5:  # если 4>5 то выполняется print(1) и print(2).Иначе print(6).print(7) выполняется и так без инструкций
    print(1)  # отступы должны быть на 1-м уровне(4 пробела или TAB) иначе будет синтактическая ошибка
    print(2)  # блок IF закрывается последней строкой с отступом
else:
    print(6)
print(7)  # в первой строке можно записать if 4 > 5 and 2>5 or 1>3: например или if 5: (можно поставить любое непустое
# значение и программа приведёт это в True а значит условие выполняется)

a = int(input())  # ВВели 2-а числа и выведем максимальное (с 9 по 14 строку)
b = int(input())
c = a
if b > a:
    c = b
print(c)

a = int(input())  # ВВели 2-а числа и выведем меньшее затем большее (с 16 по 20 строку)
b = int(input())
if b > a:
    a, b = b, a  # в переменную а записал данные с b , а в переменную b записал с а
print(a, b)

a = int(input())  # проверка на чётность
if a % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
