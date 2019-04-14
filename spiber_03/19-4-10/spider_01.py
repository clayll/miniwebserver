from urllib import request
import urllib

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
url = "https://www.qiushibaike.com/8hr/page/5/"
req = request.Request(url,headers=headers)
response = request.urlopen(req)
print(response.text)


