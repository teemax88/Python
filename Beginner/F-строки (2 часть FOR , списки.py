gender = {
    'male': 'Дорогой',
    'female': 'Дорогая'
}  ## создали словарь в котором будем ниже подставлять пол человека
a = [
    ['Семён', 'Семёнович', 32.56, 'male'],
    ['Тамара', 'Ивановна', 13.12, 'female'],
    ['Михаил', 'Анатольевич', 238.12, 'male'],
]  ## создали вложенный список 'а' с данными о нескольких людях
for name, midname, balance, g in a:  ## создали цикл for в котором будем записывать в переменные данные брать которые будем из списка 'a'
    text = f"""{gender[g]} {name} {midname} баланс вашего лицевого счёта
составляет {balance} рублей"""  ## т.е.name='Семён' , midname='Семёнович' и т.д. по списку
    print(text)  ## g ищет по списку {gender[g]} по словарю gender
