import socket, threading
import time,random

def createConnter():
    ip_port = ("127.0.0.1", 10100)

    sk = socket.socket()
    sk.connect(ip_port)
    time.sleep(random.randint(1,4))
    sk.send("123".encode())
    sk.send("3333".encode())
    sk.close()
    threading.current_thread()

for i in range(10):
    t = threading.Thread(target=createConnter)
    t.start()