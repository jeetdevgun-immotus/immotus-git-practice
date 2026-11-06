import requests

url = "https://jsonplaceholder.typicode.com/todos?userId=1"

response = requests.get(url, timeout=10)

print(response.status_code)

data = response.json()

print(type(data))
print(len(data))
for task in data:
    print(task["title"])