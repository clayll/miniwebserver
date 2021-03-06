import socket, threading ,os,time
from network.DataHandler import DataHandler

class Web_server():
    # 用来保存已经通过验证的用户
    loginusers = {}


    def __init__(self):
        print("服务启动")

    def auth(self, data):
        "验证用户是否登录"
        try:
            data["time"] = time.time()
            Web_server.loginusers[data["loginName"]] = data
            print(Web_server.loginusers)
        except KeyError:
            return None

    def heartbeat(self, data):
        """得到用户心跳包"""
        try:
            userinfo = Web_server.loginusers[data["loginName"]]
            if userinfo:
                print("收到{}心跳包,更新在线时间{}".format(data["username"],data["time"]))
                Web_server.loginusers[data["loginName"]]["time"] = data["time"]
            else:
                print("请先该用户未登录")
        except KeyError:
            print("心跳包过期，请重新登录")


    def checkUserOnline(self):
        """1分钟检查一次，用户是否在线，没有发送心跳包的移除登录状态"""
        while True:
            time.sleep(5)
            try:
                for i in list(Web_server.loginusers.keys()):
                    userData = Web_server.loginusers[i]
                    print("检查：{}".format(userData["username"]))
                    if (time.time() - userData["time"]) > 15:
                        print("心跳包检查到{}用户未发送心跳包，将其移除".format(userData["username"]))
                        del Web_server.loginusers[i]
                        continue

            except Exception as ex:
                print(ex)


    def dealFile(self, data:dict):

        userinfo = data[0]
        filename = data[1]
        filecontent = data[2]
        if userinfo:
            if userinfo["to"] != "大家":
                if not Web_server.loginusers[data["loginName"]]:
                    print("对不起，{}不在线，请稍后再试！".format(data["to"]))
                    return
            print("{}对{}发送了文件，文件名称为：{}".format(userinfo["username"], userinfo["to"],filename))
        dirName = os.path.join(os.path.abspath("files"), filename)
        if userinfo["type"] == "img":
            with open(dirName,"wb") as f:
                f.write(filecontent)
        else:
            with open(dirName,"w",encoding="utf-8") as f:
                f.write(filecontent)


    def dealMsg(self,data:dict):
        '''处理群里或者私了信息，如果未登录会提示先登录验证'''
        # print("dels{}".format(Web_server.loginusers))
        if data["type"] == "speak":
            try:
                Web_server.loginusers[data["loginName"]]
            except KeyError:
                print("检测到{}未登录验证，请先登录验证".format(data["username"]))
                return

            if data["to"] != "大家":
                try:
                    Web_server.loginusers[data["to"]]
                except KeyError:
                    print("对不起，{}不在线，请稍后再试！".format(data["to"]))
                    return

            print("{}对{}说：{}".format(data["username"],data["to"],data["msg"]))

        elif data["type"] == "auth":
            self.auth(data)
        elif data["type"] == "heartbeat":
            self.heartbeat(data)


    def connectClinet(self,newClinet: socket,addr):
        ''''连接聊天客户端'''
        print("聊天socket开始监听:"+threading.current_thread().getName())

        dataHandler = DataHandler()
        """连接客户端，接收消息"""
        print("客户端连接上了{}".format(addr))
        while True:
            try:
                content = newClinet.recv(1024)
                if content:
                    dataHandler.reviceData(content)
                    for data in dataHandler.getDataList():
                        self.dealMsg(data)
            except ConnectionResetError as r:
                print("客户端{}已经关闭".format(addr))
                newClinet.close()



    def connectClinetFile(self,newClinet,addr):
        ''''连接文件客户端'''
        print("文件socket开始监听:"+threading.current_thread().getName())
        """连接客户端，接收消息"""
        dataHandler = DataHandler()
        print("文件客户端连接上了{}".format(addr))
        while True:
            content = newClinet.recv(1000000)
            if content:
                print(content)

                dataHandler.reviceDataFile(content)

                for data in dataHandler.getDataListFile():
                    self.dealFile(data)

    def connection_func(self):
        '''用于监听聊天客户端'''
        while True:
            newClinet, addr = self.socket.accept()
            t = threading.Thread(target=self.connectClinet, args=(newClinet,addr))
            t.start()

    def connectionfile_func(self):
        '''用于监听文件客户端'''
        while True:
            newClinet1, addr1 = self.filesocket.accept()
            t1 = threading.Thread(target=self.connectClinetFile,args=(newClinet1,addr1))
            t1.start()

    def run(self):
        self.socket = socket.socket()
        self.filesocket = socket.socket()
        self.socket.bind(("127.0.0.1", 10100))
        self.filesocket.bind(("127.0.0.1", 10101))
        self.socket.listen(5)
        self.filesocket.listen(3)
        # while True:
            # newClinet, addr = self.socket.accept()
            # newClinet1, addr1 = self.filesocket.accept()
            # t = threading.Thread(target=self.connectClinet, args=(newClinet,addr))
            # t1 = threading.Thread(target=self.connectClinetFile,args=(newClinet1,addr1))
        # 聊天客户端线程
        t = threading.Thread(target=self.connection_func)
        # 文件客户端线程
        t1 = threading.Thread(target=self.connectionfile_func)
        # 检查客户端心跳包
        t2 = threading.Thread(target=self.checkUserOnline)
        t.start()
        t1.start()
        t2.start()




if __name__ == "__main__":
    # 1. 启动web服务器
    server = Web_server()
    server.run()




