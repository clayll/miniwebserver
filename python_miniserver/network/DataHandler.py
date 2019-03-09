import struct , json ,base64

class DataHandler():
    """处理消息体，每一个线程形成一个Datahandler对象"""
    def __init__(self):
        self.data_list = []
        self.datas=b''
        self.filedatas = b''
        self.datafile_list = []

    def reviceData(self,data):
        """接收客户端发送的消息"""
        self.datas = self.datas+data
        self.analysis_Data()

    def reviceDataFile(self,data):
        """接收客户端发送的消息"""
        self.filedatas = self.filedatas+data
        self.analysis_Data_file()

    def getDataList(self):
        """返回解析的数据列表,获取数据后"""
        while len(self.data_list) > 0:
            yield self.data_list.pop(0)

    def getDataListFile(self):
        """返回解析的数据列表,获取数据后"""
        while len(self.datafile_list) > 0:
            yield self.datafile_list.pop(0)

    def analysis_Data(self):
        while len(self.datas) > 2:
            dataLen = struct.unpack("H", self.datas[0:2])[0]
            tempdata = self.datas[2:2+dataLen]
            tempdata = tempdata.decode("utf-8")
            tempdata = json.loads(tempdata)
            self.data_list.append(tempdata)
            self.datas = self.datas[2+dataLen:]

    def analysis_Data_file(self):
        """解析文件内容"""
        while len(self.filedatas) > 8:
            """解包协议发送消息,文件名称，文件内容"""

            data_len = struct.unpack("HHi", self.filedatas[0:8])
            data = self.filedatas[8:8+data_len[0]]
            data = data.decode("utf-8")
            data = json.loads(data)
            data_name = self.filedatas[8 + data_len[0]:8 + data_len[0]+ data_len[1]].decode("utf-8")
            if data['type'] == 'img':
                tempdata = self.filedatas[8 + data_len[0] + data_len[1]: 8 + data_len[0]+ data_len[1]+data_len[2]]
                l = len(tempdata)
                content_data = base64.b64decode(tempdata)
            else:
                content_data = self.filedatas[8 + data_len[0] + data_len[1]: 8 + data_len[0]+ data_len[1]+data_len[2]].decode("utf-8")

            self.datafile_list.append((data, data_name, content_data))
            self.filedatas = self.filedatas[8 + data_len[0] + data_len[1]+data_len[2]:]


