import re
import requests
import pprint
import json

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
url = "https://36kr.com/"
r = requests.get(url, headers = head)
content = r.content.decode()

result = re.findall(r"\"feedPostsLatest\|post\":\[\{.*?\}\]",content)
print(len(result))
result = re.sub(r"\"feedPostsLatest\|post\":","",result[0])
result = json.loads(result)
with open("36kr.json","w",encoding="utf-8") as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))


# s = r'"idebarNewsflash|newsflash":[{"id":"156338"}],"sdfs|dasf":[{"123":"133"}]'
#
# print(re.findall(r"\"idebarNewsflash\|newsflash\":\[{.*}]",s))