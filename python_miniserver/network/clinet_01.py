import socket
from network.Message import Message
from network.miniserver_01 import Web_server
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

    def send_message(self,msg,toUser=None):
        userinfo = Web_server.loginusers[self.userinfo[0]]
        if not userinfo:
            print("请先登录")
            return
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
    if  userinfo:
        user1 = Web_Client(userinfo)
        user1.createConnter()
        print(userinfo[0])

        Web_server.loginusers[userinfo[0]]=userinfo
        user1.send_message("123")
        user1.send_message("345")
        user1.send_message("444444")