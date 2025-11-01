import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1", verify=False)

print(response.json())

data = {
    "userId": 1,
    "title": "Новая задача",
    "completed": False
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data, verify=False)

print(response.status_code)

data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data, verify=False)

print(response.json())

headers = {"Authorization": "Bearer my_swcret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers, verify=False)

print(response.json())
print(response.headers)

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params, verify=False)

print(response.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files, verify=False)

print(response.json())

with httpx.Client as client:
    response_1 = client.get(url="https://jsonplaceholder.typicode.com/todos/1")
    response_2 = client.get(url="https://jsonplaceholder.typicode.com/todos/2")

print(response_1.json())
print(response_2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_swcret_token"}, verify=False)

response = client.get("https://httpbin.org/get")

print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url", verify=False)
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/delay/5", timeout=2, verify=False)
except httpx.ReadTimeout:
    print(f"Запрос превысил лимит времени")
