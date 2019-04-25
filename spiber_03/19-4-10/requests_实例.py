import requests




s = requests.sessions.session()
requests.cook

url = "http://wwww.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
res = requests.get(url,headers=headers)
print(type(res.cookies))

print(type(res.request._cookies))