import requests
import json

class fanyi:
    def __init__(self, url, headers={"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"}):
        self.url = url
        self.hearders = headers


    def parseUrl(self, p):
        p = {"query":p}
        return requests.post(self.url, headers=self.hearders, params=p)


if __name__ == "__main__":
    # response = requests.get("http://www.baidu.com")
    # print((response.cookies))
    # print((response.encoding))
    # print(requests.utils.dict_from_cookiejar(response.cookies))

    # print(requests.utils.cookiejar_from_dict({'BDORZ': '27315'}))
    # proxies = {"http":"http://221.7.255.168:80"}
    # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    # response1 = requests.get("http://www.baidu.com",verify = False, headers = headers, proxies = proxies)
    # assert response1.status_code == 200

    # 1.解析访问网站的URL地址
    f = fanyi("https://fanyi.baidu.com/langdetect")
    fromstr = "蜘蛛"
    r = f.parseUrl(fromstr)

    # 2.获取翻译前以及翻译后的语言
    src = json.loads(r.content.decode())['lan']

    # 3.封装调用翻译结果的内容
    fromstr = {"query": "蜘蛛","from":"zh","to": "en"}
    # 4.提交翻译，获取翻译结果
    f = fanyi("https://fanyi.baidu.com/basetrans")
    r = f.parseUrl(fromstr)
    print(r.content.decode())
