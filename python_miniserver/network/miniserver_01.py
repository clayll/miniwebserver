import socket, threading
from network.DataHandler import DataHandler
import sqlite3

class Web_server():

    def __init__(self):
        print("服务启动")


    # 存储已经登录的用户
    loginusers = {}

    def auth(self , username):
        "验证用户是否登录"
        try:
             return Web_server.loginusers[username]
        except KeyError:
            return None

    def dealMsg(self,data:dict):

        print("dels{}".format(Web_server.loginusers))
        if data["type"] == "speak":
            if data["to"] != "大家":
                if not self.auth(data["username"]):
                    print("对不起，{}不在线，请稍后再试！".format(data["to"]))
                    return
            print("{}对{}说：{}".format(data["username"],data["to"],data["msg"]))


    def connectClinet(self,newClinet,addr):
        print("开始监听:"+threading.current_thread().getName())

        dataHandler = DataHandler()
        """连接客户端，接收消息"""
        print("客户端连接上了{}".format(addr))
        while True:
            content = newClinet.recv(1024)
            if content:
                dataHandler.reviceData(content)
                for data in dataHandler.getDataList():
                    self.dealMsg(data)


    def run(self):
        self.socket = socket.socket()
        self.socket.bind(("127.0.0.1", 10100))
        self.socket.listen(5)
        while True:
            newClinet, addr = self.socket.accept()
            t = threading.Thread(target=self.connectClinet, args=(newClinet,addr))
            t.start()

    @classmethod
    def addLoginUser(cls,username, userinfo):
        cls.loginusers[username] = userinfo
        print("addLoginUser-cls{}".format(cls.loginusers))
        print("addLoginUser-Web_server{}".format(Web_server.loginusers))

class Web_User():
    def __init__(self):
        self.conn = sqlite3.connect('chat.db')

    def init_tables(self):
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS USER
                (NAME TEXT,
                PWD TEXT,
                EMAIL TEXT);
                '''
            # 主要就是上面的语句
            self.conn.execute(create_tb_cmd)
            self.conn.commit()
        except:
            print("Create table failed")

    def getConnction(self):
        pass



    def register(self,name, pwd ,email):
        """注册用户"""
        insert_dt_cmd = '''INSERT INTO USER (NAME,PWD,EMAIL) VALUES ('{}','{}','{}');
           '''.format(name,  pwd ,email)
        self.conn.execute(insert_dt_cmd)
        self.conn.commit()

    def login(self,name,pwd):
        """验证用户"""
        result = self.conn.execute("select  * from USER where NAME='{}' and PWD ='{}'".format(name, pwd))
        user =  result.fetchall()
        if user:
            Web_server.addLoginUser(user[0][0],user[0])
        return user[0]

if __name__ == "__main__":
    # 1. 启动web服务器
    server = Web_server()
    server.run()




