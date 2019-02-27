import socket
from network.Message import Message
# from network.miniserver_01 import Web_server
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
        self.sk.send(Message.sendData(self.userinfo[0],msg,toUser))




# sk = createConnter()
# sk.send("123".encode())
# sk.send("345".encode())
# sk.send("678".encode())
# sk.send("906".encode())
# sk.send("13".encode())
# sk.send("1234".encode())
# sk.send("234".encode())
# sk.send("3333".encode())

#2. 客户登录后，启动客户端
# userhelp = Web_User()
# userinfo = userhelp.login("xiaohong","123")
# print(userinfo)
# if  userinfo:
#     user1 = Web_Client(userinfo)
#     user1.createConnter()
#     print(userinfo[0])
#     Web_server.loginusers[userinfo[0]]=userinfo
#     user1.send_message()
#
# #3. 用户登录
# print("123")