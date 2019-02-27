import json, struct

class Message():
    @classmethod
    def packMsg(cls,send_data):
        """打包消息协议"""
        return  struct.pack("H", len(send_data)) + send_data

    @classmethod
    def unpackMsg(self, send_data):
        """解包协议"""
        data_len = struct.unpack("H", send_data[0:2])

        send_data = send_data[2:data_len[0]+2]
        return send_data

    @classmethod
    def sendData(cls,userinfo,msg,toUser=None):

        send_object = dict()
        send_object['a'] = 'auth'
        send_object['username'] = userinfo[0][0]
        send_object['password'] = userinfo[0][1]
        send_object['msg'] = msg
        send_data = json.dumps(send_object)
        send_data = send_data.encode('utf-8')
        return cls.packMsg(send_data)

