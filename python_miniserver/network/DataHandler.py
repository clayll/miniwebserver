import struct , json


class DataHandler():
    """处理消息体，每一个线程形成一个Datahandler对象"""
    def __init__(self):
        self.data_list = []
        self.datas=b''

    def reviceData(self,data):
        """接收客户端发送的消息"""
        self.datas = self.datas+data
        self.analysis_Data()

    def getDataList(self):
        """返回解析的数据列表,
        获取数据后
        """

        while len(self.data_list) > 0:
            yield self.data_list.pop(0)

    def analysis_Data(self):
            while len(self.datas) > 2:
                dataLen = struct.unpack("H", self.datas[0:2])[0]
                tempdata = self.datas[2:2+dataLen]
                tempdata = tempdata.decode("utf-8")
                tempdata = json.loads(tempdata)
                self.data_list.append(tempdata)
                self.datas = self.datas[2+dataLen:]

