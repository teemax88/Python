name = 'Андрей'
mid_name = 'Александрович'
balance = 32.56

text = ("Дорогой " + name + ' ' + mid_name + """ баланс вашего лицевого счёта
составляет """ + str(balance) + " рублей")  # можно так (тяжело)
print(text)

text_1 = """Дорогой {0} {1} баланс вашего лицевого счёта
составляет {2} рублей""".format(name, mid_name, balance)  # так проще и лучше(c {0} по ..{2}
print(text_1)  ## после .format(вставил наши переменные) ТОЛЬКО """тескт"""

text_2 = """Дорогой {n} {m} баланс вашего лицевого счёта
составляет {b} рублей""".format(n=name, m=mid_name, b=balance)  # вместо {номер} присвоил имя
print(text_2)  ## после .format(вставил наши переменные с присвоением имени) ТОЛЬКО """тескт"""
