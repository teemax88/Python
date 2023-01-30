# Выражения - генераторы не хранят в памяти все свои элементы, а выдают их по одному по мере надобности
# Генератор - итератор, элементы которого можно итерировать только один раз
# Итератор - объект, который поддерживает функцию next(). Помнит о том, какой элемент будет браться следующим
# Итерируемый объект - объект, который предоставляет возможность обойти поочередно свои элементы.
# Может быть преобразован к итератору.

# Генератор списка
a = [x ** 2 for x in range(1, 6)]
print(a)  # [1, 4, 9, 16, 25] создаст список из чисел от 1 до 5 в квадрате

# Выражения-генераторы (как генератор списка только в круглых скобках)
b = (x ** 2 for x in range(1, 6))
print(next(b))  # 1 вызов итерируемого объекта сначала первый, потом последующий
print(next(b))  # 4
print(next(b))  # 9
print(next(b))  # 16
print(next(b))  # 25
# или можно обойти в цикле, но только 1 раз
for i in b:
    print(i)  # 1  4  9  16  25 (вывод будет только 1 раз или print(next(b)) или через цикл
print(sum(b))  # выведет сумму чисел в b только в первый раз прохода по ним(потом 0)

# генератор не хранит в памяти элементы, а удаляет их сразу после вывода (поэтому ошибок не будет)
# c = [z for z in range(10000000)] # создаст, но очень долго и возможно будет Memory Error
# c = (z for z in range(10000000))
# for i in c:
#     print(i) # вывод всех элементов генератора

# можно с помощью генератора создать список
q = (i * 2 for i in range(5))
q_1 = list(q)  # создали список из генератора q
print(q_1)  # [0, 2, 4, 6, 8]
q_2 = list(q)  # создали список из генератора q (но он будет пустой поскольку генератор от q уже сработал)
print(q_2)  # [] получим пустой список поскольку генератор уже сработал и это будет только 1 раз

# len(q) - нельзя применить длину к генератору
# q[2]  - нельзя применить индекс к генератору

# https://habr.com/ru/post/320288/ всё о генераторах
