import json

maximum = 0
max_id = 0
# max_lastname = ''
with open('group_people.json') as file:
    data = json.load(file)
    for elem in data:
        id_group = elem['id_group']
        total = 0
        for fem in elem['people']:
            if fem['gender'] == 'Female' and fem['year'] > 1977:
                total += 1
        if total > maximum:
            maximum = total
            max_id = id_group
    print(max_id, maximum)
