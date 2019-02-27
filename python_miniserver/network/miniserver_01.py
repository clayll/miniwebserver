import socket, threading
from  network.Message import Message


class Web_server():

    def __init__(self):
        print("服务启动")


    # 存储已经登录的用户
    loginusers = {}


    def connectClinet(self,newClinet,addr):
        print("开始监听:"+threading.current_thread().getName())

        """连接客户端，接收消息"""
        print("客户端连接上了{}".format(addr))
        while True:
            content = newClinet.recv(1024)
            if content:
                content = Message.unpackMsg(content)
                print(content.decode())



    def run(self):
        self.socket = socket.socket()
        self.socket.bind(("127.0.0.1", 10100))
        self.socket.listen(5)
        while True:
            newClinet, addr = self.socket.accept()
            t = threading.Thread(target=self.connectClinet, args=(newClinet,addr))
            t.start()



if __name__ == "__main__":
    # 1. 启动web服务器
    server = Web_server()
    server.run()




