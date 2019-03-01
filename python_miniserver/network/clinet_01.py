import socket
from network.Message import Message
from network.miniserver_01 import Web_User
# from network.Web_User import Web_User


class Web_Client():

    def __init__(self, userinfo):
        self.userinfo = userinfo

    def createConnter(self):
        """连接服务器"""
        ip_port = ("127.0.0.1", 10100)
        sk = socket.socket()
        sk.connect(ip_port)
        self.sk = sk

    def send_message(self,msg,toUser=None):
        """发送消息"""
        self.sk.send(Message.sendData(userinfo,msg,toUser))




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
    userhelp = Web_User()
    userinfo = userhelp.login("xiaohong","123")
    userinfo2 = userhelp.login("xiaoming","123")

    if userinfo2:
        user2 = Web_Client(userinfo2[0])
        user2.createConnter()
        # Web_server.loginusers[userinfo2[0][0]] = userinfo2[0]
        user2.send_message("我是小明")

    if  userinfo:
        user1 = Web_Client(userinfo[0])
        user1.createConnter()
        # Web_server.loginusers[userinfo[0][0]]=userinfo[0]
        user1.send_message("我是小红")
        user1.send_message("我来了")
        user1.send_message("在不在，我有问题要问你",toUser="xiaoming")

while True:
    pass