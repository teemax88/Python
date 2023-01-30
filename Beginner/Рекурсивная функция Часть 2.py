# # функция запишет в скобки (от центра ( , и после центра ) )
# def recursion(x):
#     if len(x) <= 2:  # точка выхода из рекурсии
#         return x
#     return x[0] + '(' + recursion(x[1:-1]) + ')' + x[-1]  # запись результата
#
#
# x = input()  # фываапФВЦЙФ
# print(recursion(x))  # ф(ы(в(а(а(п)Ф)В)Ц)Й)Ф


# функция возводит число в степень
def stepen(x, n):
    if n == 0:
        return 1
    if n < 0:  # если степень отрицательная
        return 1 / stepen(x, abs(n))
    if n % 2 == 0:
        return stepen(x, n // 2) * stepen(x, n // 2)
    if n % 2 != 0:
        return stepen(x, n - 1) * x


print(stepen(5, 4))  # 625
print(stepen(5, -3))  # 0.008


# создадим функцию которая будет показывать на каком уровне вложенные списки
def vl_spiski(w, level=1):
    print(*w, 'Level = ', level)
    for i in w:
        if type(i) is list:
            vl_spiski(i, level + 1)


w = [1, 23, [3, 4, [3]], [2, 4, 8, [33, 12], 12, 34]]
vl_spiski(w)
# 1 23 [3, 4, [3]] [2, 4, 8, [33, 12], 12, 34] Level =  1
# 3 4 [3] Level =  2
# 3 Level =  3
# 2 4 8 [33, 12] 12 34 Level =  2
# 33 12 Level =  3
