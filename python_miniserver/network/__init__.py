import struct, os,re,base64
#
# s = struct.pack("HHi",123,32,31)
#
# print(s)
# print(len(s))
#
# # print(struct.unpack("HHi",s))
# s = b'\\\x00\x1f\x00\x8a\x02\x00\x00'
# print(len(s))
# b'\\\x00\x00\x00\x1f\x00\x00\x00\x8a\x02'
# print(struct.unpack("HHi",s))
#
# filename =b'\xe7\xbd\x91\xe4\xb8\x8a\xe6\xb5\x8b\xe8\xaf\x84\xe6\xb7\xbb\xe5\x8a\xa0\xe6\xb5\x8b\xe8\xaf\x84\xe4\xba\xba.txt\xef\xbb\xbf\xe7\xac\xac\xe4\xb8\x80\xe6\xad\xa5 \xef\xbc\x9a \r\n\t\xe8\x8e\xb7\xe5\x8f\x96SurveyAcivity \xe8\xa1\xa8ID \xef\xbc\x88\xe5\x8f\xaf\xe9\x80\x9a\xe8\xbf\x87Tit'
# print(filename.decode())

# r = re.match(".*\.(gif|jpeg|png|jpg|bmp)$","结束处理 (1).png").group()
#
#
#
# print(r)

# with open(r"F:\重要资料\统计学\练习\test.txt",'r',encoding="utf-8") as f:
#     content = f.read()
#
# print(type(content))
# with open(os.path.join(os.path.abspath("files"), "ceshi.txt"),"w",encoding="utf-8") as f:
#     f.write(content)

#
# bcontnt = base64.b64encode(content)
#
#
# r = base64.b64decode(bcontnt)
#
# with open(os.path.join(os.path.abspath("files"), "ceshi.jpg"),"wb") as f:
#     f.write(r)
#
# while True:
#     pass
# # print(1552098054.3432496 - 1552098077.6566389)
# import  time
# from  threading import  Thread
# # print(type(time.time()))
# # print(time.time())
# def line1():
#
#     for i in range(5):
#         time.sleep(1)
#         print("line1:{}".format(i))
#
#
# def line2():
#     for i in range(5):
#         time.sleep(1)
#         print("line2:{}".format(i))
#
# t = Thread(target=line1)
# t1 = Thread(target=line2)
#
# t.start()
# t1.start()

# test = {}
# test["a"] = "123"
# test["b"] = "231"
#
# print(type(test.keys()))
#
# for i in list(test.keys()):
#     if i == "b":
#         del test[i]
#         continue
#
# for i in test:
#     print(i)
