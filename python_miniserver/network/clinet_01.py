import socket,os,time,threading
from network.Message import Message
from network.Web_User import Web_User


class Web_Client():

    def __init__(self, userinfo):
        self.userinfo = userinfo

    def createConnter(self):
        """连接服务器"""
        ip_port = ("127.0.0.1", 10100)
        sk = socket.socket()
        sk.connect(ip_port)
        self.sk = sk

    def createConnterFile(self):
        ip_port = ("127.0.0.1", 10101)
        sk_file = socket.socket()
        sk_file.connect(ip_port)
        self.sk_file = sk_file

    def send_message(self,msg,toUser=None):
        """发送消息"""
        self.sk.send(Message.sendData(self.userinfo,msg,toUser))

    def send_auth(self,userinfo):
        self.sk.send(Message.sendAuth(userinfo))

    def send_file(self,userinfo,filePath):
        filename = os.path.basename(filePath).encode("utf-8")
        with open(filePath, "rb") as f:
            content_data = f.read()

        self.sk_file.send(Message.sendData_file(filename,content_data,userinfo))

    def __send_heartbeat(self,userinfo):
        while True:
            time.sleep(5)
            self.sk.send(Message.sendHeartbeat(userinfo,time.time()))

    def send_heartbeat_func(self, userinfo):
        t = threading.Thread(target=self.__send_heartbeat,args=(userinfo,))
        t.start()




    # sk = createConnter()
# sk.send("123".encode())
# sk.send("345".encode())
# sk.send("678".encode())
# sk.send("906".encode())
# sk.send("13".encode())
# sk.send("1234".encode())
# sk.send("234".encode())
# sk.send("3333".encode())

if __name__ == "__main__":
#2. 客户登录后，启动客户端
    # 1 发送群聊
    zhangxiang = Web_User.login("zhangxiang","123")
    maike = Web_User.login("maike","123")
    print(zhangxiang)
    if zhangxiang:
        # 初始化用户
        web_zhangxiang = Web_Client(zhangxiang)
        web_maike = Web_Client(maike)
        # 链接服务器
        web_zhangxiang.createConnter()
        web_zhangxiang.createConnterFile()
        web_zhangxiang.send_auth(zhangxiang)
        web_maike.createConnter()
        # 发送心跳包
        web_zhangxiang.send_heartbeat_func(zhangxiang)
        while True:
            args = input("输入1.发起用户验证;输入2.发起群聊;3.发起私聊;4.发送文件；5.发送图片；输入Q退出")
            if args == "1":
                # 发送服务器登录验证
                web_zhangxiang.send_auth(zhangxiang)
            if args == "2":
                args = input("输入发送的消息：")
                web_zhangxiang.send_message(args)
            if args == "3":
                web_maike.send_auth(maike)
                args = input("输入发送的消息：")
                to = input("输入对方登录名：")
                web_zhangxiang.send_message(args, to)
            if args == "4":
                args = input("请输入文件路径：")
                # F:\重要资料\统计学\练习\test.txt
                web_zhangxiang.send_file(zhangxiang,args)
            if args == "5":
                args = input("请输入文件路径：")
                # F:\重要资料\统计学\练习\px90第三阶段.jpg
                web_zhangxiang.send_file(zhangxiang,args)
            if args.upper() == "Q":
                break


    userinfo = None #Web_User.login("xiaohong","123")
    userinfo2 =None # Web_User.login("xiaoming","123")

    if userinfo2:


        user2 = Web_Client(userinfo2[0])
        user2.createConnter()
        # Web_server.loginusers[userinfo2[0][0]] = userinfo2[0]
        user2.send_auth(userinfo2)
        # user2.send_message("我是小明")

    if  userinfo:
        user1 = Web_Client(userinfo[0])
        user1.createConnter()
        # Web_server.loginusers[userinfo[0][0]]=userinfo[0]
        user1.send_auth(userinfo)
        # user1.send_message("我是小红")
        # user1.send_message("我来了")
        # user1.send_message("在不在，我有问题要问你",toUser="xiaoming")
        # user1.createConnterFile()
        # filePath = r"C:\Users\刘靓\Documents\Tencent Files\20960180\FileRecv\截图1.jpg"
        # user1.send_file(userinfo,filePath)
        # filePath = "F:\重要资料\统计学\练习\px90第二阶段.jpg"
        # user1.send_file(userinfo, filePath)
        # filePath = "F:\重要资料\统计学\练习\px90第三阶段.jpg"
        # user1.send_file(userinfo, filePath)
        user1.send_heartbeat_func(userinfo)
