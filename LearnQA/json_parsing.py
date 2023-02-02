import json

string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)
# мы с помощью библиотеки JSON парсим нашу строку, она превращается в объект(словарь)
# и мы его сохраняем в переменную

print(obj['answer'])
# мы обращаемся к ключу answer в словаре obj и возвращаем его значение

# проверяем наличие ключа
key = "answer"

if key in obj:
    print(obj['answer'])
else:
    print(f"Ключа {key} в JSON нет")
