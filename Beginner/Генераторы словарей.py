# создадим словари через генератор словарей (в нём ключ:значение)
a = {i: i ** 2 for i in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} словарь в котором ключ i и его значение i**2
# a1 = {}  # во 2й строке тоже самое что и в 3-5 строке
# for i in range(1, 6):
#     a[i] = i**2

a1 = {word: len(word) for word in ['hello', 'world', 'www']}  # {'hello': 5, 'world': 5, 'www': 3}
# содзали словарь а1 в котором ключом будет слово со списка, значением его длинна

data = {  # сделаем с помощью генератора Имя Фамилия начин.с большой буквы,остальные мален.,значение int
    'джЕфф Безос': '177',
    'Илон МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГейтС': '124',
}
data1 = {key.title(): int(value) for key, value in data.items()}  # 'Джефф Безос': 177
# items() возьмёт пары и присвоит key, value ключ и значение, title() сделает первую большую,а остальные маленькие

# data2 = {} в 16й строке сделали тоже самое что в 19-21
# for key, value in data.items():
#     data2[key.title()] = int(value)

# создадим словарь из вложенного списка чтобы можно было обратиться по ключу
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [51, 'Andrey', '1234']
]
print(users[3])  # [51, 'Andrey', '1234'] а нам нужно найти его по 51 (создадим ключ в словаре)
usersslov = {person[0]: person[1:] for person in
             users}  # создаст словарь с ключом 1-е значение в списке,знач. остальное
print(usersslov)
