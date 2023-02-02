from json.decoder import JSONDecodeError
import requests

payload = {"name": "Timur"}  # задаем переменной параметры, как в Postman при GET запросе

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# URL и потом передаем ему параметры, которые сохранили в переменную

print(response.text)
print(response.status_code)

print("******---------------******")

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])
except JSONDecodeError:
    print("Response is not JSON format")

print("******---------------******")


response = requests.get("https://playground.learnqa.ru/api/check_type")
print(response.text)

print("******---------------******")

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)
