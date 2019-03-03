import requests
s = "http://c.hiphotos.baidu.com/forum/w%3D96%3Bq%3D45%3Bg%3D0/sign=72626c2a7ecf3bc7e800c1eaea718795/7d5e1e67d0160924be73323cda0735fae7cd34e3.jpg?&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F7d5e1e67d0160924be73323cda0735fae7cd34e3.jpg"
s= requests.utils.unquote(s)

x = s.split("&src=")
print(x)