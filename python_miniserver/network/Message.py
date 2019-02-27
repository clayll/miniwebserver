import json, struct
from network.miniserver_01 import Web_server

class Message():
    @classmethod
    def packMsg(cls,send_data):
        """打包消息协议"""
        return  struct.pack("H", len(send_data)) + send_data

    @classmethod
    def unpackMsg(self, send_data):
        """解包协议"""
        data_len = struct.unpack(send_data[0:2])
        send_data = send_data[2:data_len+2]
        return send_data

    def getUser(self, username):
        user = Web_server.loginusers[username]
        return user

    @classmethod
    def sendData(cls,fromUser,msg,toUser=None):
        userinfo = Web_server.loginusers[fromUser]
        if not userinfo:
            print("请先登录")
            return
        print("开始发送消息")
        print(userinfo)
        send_object = dict()
        send_object['a'] = 'auth'
        send_object['username'] = userinfo[0][0]
        send_object['password'] = userinfo[0][1]
        send_object['msg'] = msg
        send_data = json.dumps(send_object)
        send_data = send_data.encode('utf-8')
        return cls.packMsg(send_data)

