from test import test
from test import __all__
from pprint import pprint
import sys, os, datetime

import demjson
from collections import namedtuple, deque, OrderedDict
print(os.path.join(os.path.abspath(""),"test"))
# sys.path.append()

# pprint(sys.path)

print(__all__)
test.number = 130
print(demjson.encode({"a":123}))


test.read()



P = namedtuple("Point",["x","y"])
P.x = 12
P.y = 13

l = [i for i in range(10)]
d = deque(l)
d.appendleft(12)
d.append(411)
print(d)


class mydict(dict):
    def __init__(self, default_factory, *args, **kwargs):
        self.default_factory = default_factory
        dict.__init__(self, *args, **kwargs)
    def __getitem__(self, item):
        if item not in self:
            return self.default_factory()
        return self.get(item)



m = mydict(lambda :"123123NOne")
m[13]=13

print(m[13])
print(m[1234])

order = OrderedDict()
order["c"] = 2
order["b"] = 1
order["d"] = 3

print(order.keys())


class mycountdict(dict):
    def __init__(self,s=None,*args , **kwargs):

        dict.__init__(self, *args, **kwargs )

        for ch in s:
            if ch not in self:
                self[ch]=0
            self[ch] = self[ch] + 1


print(mycountdict(s="ceshiceshi"))
t = datetime.datetime.now()
print(t)
print(t.timestamp())
print(datetime.datetime.fromtimestamp(1550575221))



input_str = "ces123ddddd"
try:

    print(str.join('', ([str.upper(i) for i in input_str])))

except Exception as rs:
    print(rs)

print("\n\t\t\t\t\t\t九九乘法表：")
for i in range(1,10):
    print(" ".join(["%d*%d=%d"%(m,i,m*i) for m in range(1,i+1)]))