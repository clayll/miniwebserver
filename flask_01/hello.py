import requests

response = requests.get("http://www.baidu.com")

print(response.status_code)

print(response.content.decode())

