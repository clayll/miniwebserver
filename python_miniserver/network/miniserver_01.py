import socket, threading

def connectClinet(newClinet, addr):
    print("客户端连接上了{}".format(addr))
    content = newClinet.recv(1024)
    if content:
        print(content.decode())


s =socket.socket()
s.bind(("127.0.0.1", 10100))
s.listen(20)
print("开始监听")

while True:
    newClinet, addr = s.accept()
    t = threading.Thread(target=connectClinet, args=(newClinet, addr))
    t.start()



