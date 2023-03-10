heroes = {
    'Andrey': 38,
    'Kristina': 37,
    'Mother': 60,
    'Artur': 14,
    'Father': 65
}
# for i in heroes: # выведет ответ по ключам
#     print(i) # Andrey Kristina Mother Artur Father
#     print(i, heroes[i]) # Andrey 38 Kristina 37 Mother 60 Artur 14 Father 65

# for i in sorted(heroes):  # вывод отсортированного списка по ключам (но значения в хаотичном порядке)
#     print(i, heroes[i])  # Andrey 38 Artur 14 Father 65 Kristina 37 Mother 60

# сортировка по значениям , ключ lambda в котором будет сначала учитываться значение(para[1]) а потом сортировка по
# ключу (para[0]) , т.е. словарь отсортирует вывод по значениям, если значения совпадают то по ключу
for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
    print(i)  # ('Artur', 14) ('Kristina', 37) ('Andrey', 38) ('Mother', 60) ('Father', 65)
