import json

maximum = 0
max_name = ''
max_lastname = ''
with open('manager_sales.json') as file:
    data = json.load(file)
    for elem in data:
        name = elem['manager']['first_name']
        lastname = elem['manager']['last_name']
        total = 0
        for car in elem['cars']:
            total += car['price']
        if total > maximum:
            maximum = total
            max_name = name
            max_lastname = lastname
    print(max_name, max_lastname, maximum)
