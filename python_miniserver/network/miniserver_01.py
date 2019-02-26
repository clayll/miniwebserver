import socket, threading

class Web_server():
    def __init__(self):
        self.socket = socket.socket()
        self.socket.bind(("127.0.0.1", 10100))


def connectClinet():
    newClinet, addr = s.accept()
    """连接客户端，接收消息"""
    print("客户端连接上了{}".format(addr))
    while True:
        content = newClinet.recv(1024)
        if content:
            print(content.decode())



def send_message(self):
    pass

def run(self):
    self.socket.listen(10)
    t = threading.Thread(target=connectClinet)
    t.start()






