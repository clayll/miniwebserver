import json, struct,re,base64

class Message():
    @classmethod
    def packMsg(cls,send_data):
        """打包消息协议"""
        return  struct.pack("H", len(send_data)) + send_data

    @classmethod
    def packFile(cls,send_data,filename_data,content_data):
        """打包文件名称长度，文件长度"""
        send_datal = len(send_data)
        filename_datal = len(filename_data)
        content_datal = len(content_data)
        s = struct.pack("HHi",send_datal,filename_datal,content_datal)
        return s+send_data+filename_data+content_data

    @classmethod
    def unpackMsg(self, send_data):
        """解包协议"""
        data_len = struct.unpack("H", send_data[0:2])
        send_data = send_data[2:data_len[0]+2]
        return send_data

    @classmethod
    def unpackFile(self, send_data):
        """解包协议发送消息,文件名称，文件内容"""
        data_len = struct.unpack("HHi", send_data[0:8])
        send_data = send_data[8:data_len[0]]
        data_name = send_data[8+data_len[0]: data_len[1]]
        content_data = send_data[8+data_len[0]+data_len[1]:data_len[2]]
        return send_data,data_name,content_data

    @classmethod
    def sendData(cls,userinfo,msg,toUser=None):
        send_object = cls.__gen_sendObj__(userinfo)
        send_object['msg'] = msg
        if toUser:
            send_object['to'] = toUser
        else:
            send_object['to'] = "大家"
        send_data = json.dumps(send_object)
        send_data = send_data.encode('utf-8')
        return cls.packMsg(send_data)

    @classmethod
    def sendData_file(cls, filename,filedata ,userinfo, msg="", toUser=None):
        send_object = cls.__gen_sendObj__(userinfo,type="file")
        send_object['msg'] = msg
        if toUser:
            send_object['to'] = toUser
        else:
            send_object['to'] = "大家"
        # 判断是否是图片传送
        r = re.match(".*\.(.gif|jpeg|png|jpg|bmp)$", filename.decode("utf-8"))
        if r:
            send_object['type'] = 'img'
            filedata = base64.b64encode(filedata)



        send_data = json.dumps(send_object)
        send_data = send_data.encode('utf-8')
        return cls.packFile(send_data,filename,filedata)

    @classmethod
    def sendAuth(cls,userinfo):
        send_object = cls.__gen_sendObj__(userinfo,type="auth")
        send_data = json.dumps(send_object)
        send_data = send_data.encode('utf-8')
        return cls.packMsg(send_data)

    @classmethod
    def sendHeartbeat(cls, userinfo, time:float):
        send_object = cls.__gen_sendObj__(userinfo, type="heartbeat")
        send_object["time"] = time
        send_data = json.dumps(send_object)
        send_data = send_data.encode('utf-8')
        return cls.packMsg(send_data)

    @classmethod
    def __gen_sendObj__(cls,userinfo,type='speak'):
        send_object = dict()
        send_object['type'] = type
        send_object['username'] = userinfo[0]
        send_object['password'] = userinfo[1]
        send_object['email'] = userinfo[2]
        send_object['loginName'] = userinfo[3]
        return send_object

