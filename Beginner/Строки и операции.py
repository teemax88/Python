x, y, z = input().split()  # ВВОД НЕСКОЛЬКИХ ПЕРЕМЕННЫХ В STR ПО УМОЛЧАНИЮ

print('df')  # никакой разницы со следующим
print("df")

"""hello
world
456"""  # вывод 'hello\nworld\n456'

print('Hello\nworld\nwow')  # \n - перенос на следующую строку

d = ' '  # присвоили пробел переменной d

a = 'hello'  # присвоили hello переменной a
print('he' in a)  # ответ True символы he есть в переменной а
print('eh' in a)  # ответ False символов eh нет в переменной а(не в том порядке)

b = 'world'  # присвоили world переменной b
print(a + b)  # вывод helloworld (конкатенация строк)
print(a + ' ' + b)  # вывод hello world (c пробелом)
print('a' * 5)  # вывод aaaaa (умножение только на целое число (без дробей)
print(len('hello'))  # вывод кол-ва знаков (5)в слове. len(lenght-длина)

# например
s = input('Введите слово')
print('Вы ввели', len(s), ' символов')
s = 'asdfg'
print('f' in s)  # ответ True (проверили есть ли 'f'в переменной s

print('asd' + str(3))  # а так можно привести число 3 в строку путём str)
# print('asd'+3) ## так нельзя !!! (нельзя числа конкатенировать с текстом)

# "abc"+'sdf' ##конкатенация (сцепление 2-х и более строк) в программе
# 'abcsdf' ## вывод в программе

print(ord('a'))  # ord показывает какой машинный код в символе а
print('asd' < 'z')  # Ответ True поскольку Python сравнивает коды символов а не символы
# и проверяет только по первым символам (т.е. a(97) и z(122))
'asdf' < 'asdfg'  # первое меньше хотя сравнивает по первым ,но если первые символы одинаковые
# то больше та которая длиннее

print('Я стану крутым программистом!\n' * 3)  # выведет надпись 3 раза с новой строки
