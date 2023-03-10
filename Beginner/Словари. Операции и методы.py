# словарь = dictionary (dict) в нём { ключ : значение }
r = dict(moskva=495, piter=812, penza=8412)  # 2й способ создаст такой же словарь но в качестве ключей только строки
print(r)  # {'moskva': 495, 'piter': 812, 'penza': 8412}

a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
r1 = dict(a)  # внесёт в словарь данные со вложенного списка 3й способ
print(r1)  # {'moskva': 495, 'piter': 812, 'penza': 8412}

q = dict.fromkeys(['a', 'b', 'c'], 100)  # создаст словарь где ключами будут 'a' 'b' 'c' а значения присвоит 100 всем
print(q)  # {'a': 100, 'b': 100, 'c': 100}

v = {}  # создаст пустой словарь или v = dict()

d = {  # создали словарь d (ключ = 'moskva' значение = 495) 1й способ создания словаря (самый распостранённый)
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}
print(d)  # {'moskva': 495, 'piter': 812, 'penza': 8412}
print(len(d))  # 3 посчитает сколько пар (ключей)
print('moskva' in d, 2 in d, 'asd' not in d)  # True False True узнает есть ли ключ в словаре

if 'Kharkov' in d:  # если в словере d есть ключ 'Kharkov' то выведем его на печать
    print(d['Kharkov'])
else:  # если нет то добавим его в словарь
    d['Kharkov'] = 572
print(d)  # {'moskva': 495, 'piter': 812, 'penza': 8412, 'Kharkov': 572}

for key in d:
    print(key, d[key])  # вывод ключ и его значение moskva 495 и т.д.
# методы словаря
# d.clear()  очистит наш словарь до {}
rez = {}
rez.update(d)  # добавит в список rez данные со списка d
rez = dict(
    a)  # добавит в список rez данные со списка a (Конструктор dict() копирует первые элементы словаря в новый словарь,
# а затем выполняет метод update(), чтобы обновить новый словарь вторым элементом словаря
# Источник: https://pythonpip.ru/examples/obedinenie-dvuh-slovarey-v-python

rez2 = {**d, **rez}  # если будет * то добавяться только ключи, ** добавятся ключи и значения в новый словарь
print(d.get('moskva'))  # 495 выведет значение ключа
print(d['moskva'])  # 495 выведет значение ключа (тоже самое)
print(
    d.get('asd', 'Такого ключа нет'))  # Такого ключа нет. выведет значение ключа(если его нет то выведет пропис.надпись
# можно вывести что угодно вместо 'Такого ключа нет' например 100 или [1, 2, 3]
# a[i] = a.get(i, 0) + 1 добавит ключ [i] в словарь а и при первом назначении добавит значание 1 ,потом +1 к каджому
d.setdefault('Kyiv', 44)  # если ключа нет то добавит его в словарь , если уже есть то ничего не сделает
print(d)  # {'moskva': 495, 'piter': 812, 'penza': 8412, 'Kharkov': 572, 'Kyiv': 44}
print(d.pop('penza'))  # выведет значение ключа 'penza' но удалит его из списка 8412
print(d)  # {'moskva': 495, 'piter': 812, 'Kharkov': 572, 'Kyiv': 44}
print(d.popitem())  # выведет последнее значение ключа и значения но удалит его из списка ('Kyiv', 44)
print(d)  # {'moskva': 495, 'piter': 812, 'Kharkov': 572}
print(d.keys())  # dict_keys(['moskva', 'piter', 'Kharkov']) вывод всех ключей в словаре
print(d.values())  # dict_values([495, 812, 572]) вывод всех значений в словаре
for i in d.values():
    print(i)  # вывод только элементов из списка d (пройти можно его элементы или ключи если d.keys() ) 495 812 572
print(d.items())  # dict_items([('moskva', 495), ('piter', 812), ('Kharkov', 572)]) вывод всех пар
for i in d.items():
    print(i)  # вывод только пар из списка d ('moskva', 495) ('piter', 812) ('Kharkov', 572)
    print(i[0], i[1])  # вывод отдельно элементов из списка d moskva 495  piter 812  Kharkov 572

for key, value in d.items():  # в key будет ключ , в value будет значение со словаря d
    print(key, value)  # moskva 495  piter 812  Kharkov 572

d1 = {
    1: 'one',
    'two': 2,
    3: [3, 3, 3],
}
d1[44] = 'forty'  # добавит к словарю d1 ключ 44 и значение в него 'forty'
print(d1)  # {1: 'one', 'two': 2, 3: [3, 3, 3], 44: 'forty'} вывод всего словаря
print(d1['two'])  # 2 выведет только значение ключа
d1[1] = 'один'  # изменит значение ключа 1 на новое 'один'
del d1['two']  # удалит ключ 'two' в словаре d1
print(d1)  # {1: 'один', 3: [3, 3, 3], 44: 'forty'}

# ззанесём данные из строки в словарь
s = 'Asmolovskiy Andrey Kharkov HIIT 5 4 5 5 4 3 5'
s = s.split()  # разбили строку в список пробелами ['Asmolovskiy', 'Andrey', 'Kharkov', 'HIIT', '5', '4', '5', '5', '4', '3', '5']
person = {}
person['Last name'] = s[0]  # внесли в ключ 'Last name' значение из списка s[0] 'Asmolovskiy' и т.д.
person['First name'] = s[1]
person['City'] = s[2]
person['University'] = s[3]
person['marks'] = []  # создали ключ 'mаrks' с пустым списком в значении
for i in s[4:]:  # прошли в цикле от 4го индекса до конца и добавили в список 'marks' значения с s преобразовав их в int
    person['marks'].append(int(i))
print(
    person)  # {'Last name': 'Asmolovskiy', 'First name': 'Andrey', 'City': 'Kharkov', 'University': 'HIIT', 'marks': [5, 4, 5, 5, 4, 3, 5]}
