for i in range(3):
    for j in range(5):  # 00000 вывод цикл из 5ти раз будет производться 3 раза = 15 раз
        print(i, end='')  # 11111
    print()  # перевод но новую#22222 строку

for i in 'ab':
    for j in 'qwe':
        print(i, j, end='  ')  # a q  a w  a e  b q  b w  b e
# длинна пароля 3
from string import printable  # импорт printable (все значения)

# print(printable) #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
for b1 in printable:
    for b2 in printable:
        for b3 in printable:
            print(b1, b2, b3)  # выведет все возможные варианты из 3-х элементов

for j in range(1, 10):
    for i in range(1, 11):
        print(i, '*', j, '=', i * j, end=' ')
    print()  # выведет таблицу умножения
# 1 * 1 = 1 2 * 1 = 2 3 * 1 = 3 4 * 1 = 4 5 * 1 = 5 6 * 1 = 6 7 * 1 = 7 8 * 1 = 8 9 * 1 = 9 10 * 1 = 10
# 1 * 2 = 2 2 * 2 = 4 3 * 2 = 6 4 * 2 = 8 5 * 2 = 10 6 * 2 = 12 7 * 2 = 14 8 * 2 = 16 9 * 2 = 18 10 * 2 = 20
# 1 * 3 = 3 2 * 3 = 6 3 * 3 = 9 4 * 3 = 12 5 * 3 = 15 6 * 3 = 18 7 * 3 = 21 8 * 3 = 24 9 * 3 = 27 10 * 3 = 30
# 1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16 5 * 4 = 20 6 * 4 = 24 7 * 4 = 28 8 * 4 = 32 9 * 4 = 36 10 * 4 = 40
# 1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25 6 * 5 = 30 7 * 5 = 35 8 * 5 = 40 9 * 5 = 45 10 * 5 = 50
# 1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36 7 * 6 = 42 8 * 6 = 48 9 * 6 = 54 10 * 6 = 60
# 1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49 8 * 7 = 56 9 * 7 = 63 10 * 7 = 70
# 1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64 9 * 8 = 72 10 * 8 = 80
# 1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81 10 * 9 = 90

# сколько 6-ти буквенных слов содержащих ровно 2 гласных и начин.и заканч. на согласные можно создать
# из букв Т,Ы,К,В,А ? Каждая из допустимых букв может входить в слово несколько раз.
count = 0
for b1 in 'ТЫКВА':  # циклы переберут все варианты слов с этими буквами (5букв ** 6букв в слове)=15625 вариантов
    for b2 in 'ТЫКВА':
        for b3 in 'ТЫКВА':
            for b4 in 'ТЫКВА':
                for b5 in 'ТЫКВА':
                    for b6 in 'ТЫКВА':
                        itog = b1 + b2 + b3 + b4 + b5 + b6  # запись слов в переменную
                        if itog[0] in 'ТКВ' and itog[-1] in 'ТКВ':  # если первая и последняя согласные
                            if itog.count('Ы') + itog.count('А') == 2:  # если в слове 2-е гласные
                                count += 1  # то увеличим счётчик на 1
print(count)  # ответ 1944 слова

for i in range(1, 10001):  # цикл от 1-го до 100000
    x = i
    su = 0
    while x > 0:
        su = su + x % 10
        x = x // 10
    print(i, su)  # выведет число и сумму его элементов например 929 20
