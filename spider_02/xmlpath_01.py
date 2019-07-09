from lxml import  html
import json
from pprint import pprint

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div'''

html = html.etree.HTML(text)

print(html)

# s =html.xpath("//li/a/@href")
# pprint(etree.tostring(s[0])   if len(s) > 0 else None )

result = html.xpath("//*[@href='link4.html']")


for r in result:
    print(r.tag)


s = '[{"id":"J_12431121","m":"49.80","op":"31.10","p":"31.10"}]'

x = json.loads(s)
print(x[0]["op"])