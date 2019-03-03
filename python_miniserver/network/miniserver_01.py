import socket, threading ,os
from network.DataHandler import DataHandler

class Web_server():
    # 用户保存类
    loginusers = {}
    # userHelper.init_tables()

    def __init__(self):
        print("服务启动")

    def auth(self , data):
        "验证用户是否登录"
        try:
            Web_server.loginusers[data["username"]] = data
            print(Web_server.loginusers)
        except KeyError:
            return None

    def delFile(self,data:dict):
        userinfo = data[0]
        filename = data[1]
        filecontent = data[2]
        if userinfo:
            if userinfo["to"] != "大家":
                if not Web_server.loginusers[data["username"]]:
                    print("对不起，{}不在线，请稍后再试！".format(data["to"]))
                    return
            print("{}对{}发送了文件，文件名称为：{}".format(userinfo["username"], userinfo["to"],filename))
        dirName = os.path.join(os.path.abspath("files"),filename)
        with open(dirName,"w",encoding="utf-8") as f:
            f.write(filecontent)


    def dealMsg(self,data:dict):
        # print("dels{}".format(Web_server.loginusers))
        if data["type"] == "speak":
            if data["to"] != "大家":
                if not Web_server.loginusers[data["username"]]:
                    print("对不起，{}不在线，请稍后再试！".format(data["to"]))
                    return
            print("{}对{}说：{}".format(data["username"],data["to"],data["msg"]))

        elif data["type"] == "auth":
            self.auth(data)
        elif data["type"] == "file":
            print(data)
            pass



    def connectClinet(self,newClinet,addr):
        print("聊天socket开始监听:"+threading.current_thread().getName())

        dataHandler = DataHandler()
        """连接客户端，接收消息"""
        print("客户端连接上了{}".format(addr))
        while True:
            content = newClinet.recv(1024)
            if content:
                print(content)
                dataHandler.reviceData(content)

                for data in dataHandler.getDataList():
                    self.dealMsg(data)

    def connectClinetFile(self,newClinet,addr):
        print("文件socket开始监听:"+threading.current_thread().getName())
        """连接客户端，接收消息"""
        dataHandler = DataHandler()
        print("文件客户端连接上了{}".format(addr))
        while True:
            content = newClinet.recv(1024)
            if content:
                print(content)

                dataHandler.reviceDataFile(content)

                for data in dataHandler.getDataListFile():
                    self.delFile(data)


    def run(self):
        self.socket = socket.socket()
        self.filesocket = socket.socket()
        self.socket.bind(("127.0.0.1", 10100))
        self.filesocket.bind(("127.0.0.1", 10101))
        self.socket.listen(5)
        self.filesocket.listen(3)
        while True:
            newClinet, addr = self.socket.accept()
            newClinet1, addr1 = self.filesocket.accept()
            t = threading.Thread(target=self.connectClinet, args=(newClinet,addr))
            t1 = threading.Thread(target=self.connectClinetFile,args=(newClinet1,addr1))
            t.start()
            t1.start()

    # @classmethod
    # def auth_User(cls,name, pwd):
    #     user =  cls.userHelper.login(name,pwd)
    #
    #     print("auth{}".format(user))
    #     return user



if __name__ == "__main__":
    # 1. 启动web服务器
    server = Web_server()
    server.run()




