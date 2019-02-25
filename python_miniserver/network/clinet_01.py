import socket, threading
import time,random

def createConnter():
    ip_port = ("127.0.0.1", 10100)

    sk = socket.socket()
    sk.connect(ip_port)
    return sk


sk = createConnter()
sk.send("123".encode())
sk.send("345".encode())
sk.send("678".encode())
sk.send("906".encode())
sk.send("13".encode())
sk.send("1234".encode())
sk.send("234".encode())
sk.send("3333".encode())
