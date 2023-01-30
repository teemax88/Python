"""Как отсортировать словарь Python. Сортировка словаря по значениям"""
heroes = {
    'Andrey': 38,
    'Kristina': 37,
    'Mother': 60,
    'Artur': 14,
    'Father': 65,
    'Moska': 14,
    'Aleksey': 38
}
# для сортировки словаря(неупорядоченной коллекции) по ключам достаточно обойти его в цикле отсортировав по ключам
for i in sorted(heroes):  # если не указывать, то сортировка по ключу
    print(i, heroes[i])
# Aleksey 38
# Andrey 38
# Artur 14
# Father 65
# Kristina 37
# Moska 14
# Mother 60

# или оставить его в кортеже и отсортивать по чему захочется
for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):  # сначала по значению,если одинак.то по ключу
    print(*i)
# Artur 14
# Moska 14
# Kristina 37
# Aleksey 38
# Andrey 38
# Mother 60
# Father 65
# Как вариант, по значениям можно отсортировать sorted(heroes, key=heroes.get)
