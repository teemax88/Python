a = [12, 23, 45, 67, 8]  ## создали список переменных а
s = [1, 23, 56]  # создали список переменных s
n = a + s  # ответ склеивание 2-х строк [12, 23, 45, 67, 8, 1, 23, 56]
n.sort()  # отсортирует от малелького до большого [ 1, 8, 12, 23, 23, 45, 56, 67]
min(n), max(n)  # выведет минимальное и максимальное значение соответсвенно
# работа как со строками так же и с индексами
a[0]  ## покажет 0 элемент списка т.е. 12, порядок 0,1,2,3 и т.д.
a[-1]  ## покажет последний элемент в списке т.е. 8
a[2:4]  # индекс со 2го по 4й невключая [45, 67]
a[3:]  # индекс со 3го по последний [67, 8]
a[::2]  # покажет все чётные элементы [12, 45, 8]
a[1::2]  # покажет все нечётные элементы [23, 67]
a[::-1]  # элементы наоборот [8, 67, 45, 23, 12]
# списки изменяемые обьекты (в отличии от строк) т.е.
a[2] = 100  # заменил 2й индекс на 100
# теперь а выглядит [12, 23, 100, 67, 8]
a[1:3] = 23, 45  # заменит срез индеска с 1го по 2й вкл. на 23 и 45 [12, 23, 100, 67, 8]
a[1:3] = 1, 2, 5, 7  # заменит срез индеска с 1го по 2й вкл. на большее кол-во [12, 1, 2, 5, 7, 67, 8]
del a[1]  # удалим 1 элемент [12, 2, 5, 7, 67, 8]
b = a  # в перменную b сохраним список а , но при изменении a будет меняться и b поскольку хранит ссылку на обьект
b = a[:]  # так сохранит отдельный список и можно изменять а и при этом не измениться b
