import struct


class DataHandler():
    """处理消息体，每一个线程形成一个Datahandler对象"""
    def __init__(self):
        self.data_list = []

    def reviceData(self,data):
        """接收客户端发送的消息"""
        self.datas = self.datas+data

    def getDataList(self):
        """返回解析的数据列表"""
        return self.data_list

    def analysis_Data(self):
        if len(self.datas) > 2:
            dataLen = struct.unpack("H", self.data[0:2])[0]
            if len(self.datas) > dataLen+2:
                tempdata = self.datas[2:2+dataLen]
                self.data_list.append(tempdata)
                self.datas = self.datas[2+dataLen:]

