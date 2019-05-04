#coding:utf-8
import pymysql
import datetime
from urllib import request

class viewDao:
    def __init__(self):
        #数据名字和数据库连接密码要换掉
        self.gxviewdb = pymysql.connect(user='root', db='gxview', passwd='123456', host='localhost',
                             charset='utf8')  # 指定编码格式为utf-8，否则显示乱码

    def saveview(self, views):
        sql = 'insert gxviewtable(viewname, viewlink, viewimglink, viewlength, viewtype,createTime,viewused) values ("%s","%s","%s","%s","%s","%s","%d")'%(views[0],views[1],views[2],views[3],views[4],datetime.datetime.now(),0)
        cursor = self.gxviewdb.cursor()
        cursor.execute(sql)
        self.gxviewdb.commit()
        last_id = cursor.lastrowid
        cursor.close()
        try:
            # 保存图片
            filePath = self.savePicInto(views[2],last_id)
            self.updateViewImgPathById(filePath,last_id)
        except Exception as ex:
            print("更新图片失败：",ex)


    def changeview(self, viewdatas):
        viewnameindex = 0
        for data in viewdatas:
            sql = "UPDATE gxviewtable SET viewused = 1 WHERE id = %d" % (data[viewnameindex])
            try:
                cursor = self.gxviewdb.cursor()
                cursor.execute(sql)
                # 提交到数据库执行
                self.gxviewdb.commit()
            except:
                # 发生错误时回滚
                self.gxviewdb.rollback()
        print("数据库已经修改")


    """
    查询未发布的视频
    """
    def findviewunused(self, viewcount):
        cursor = self.gxviewdb.cursor()
        sql = '''select id,
        viewname,
        viewlink, 
        viewimgPath,
        viewimglink,
        viewlength,
        createTime from gxviewtable 
        where viewused=0  order by createTime Desc limit %d''' %(viewcount)
        cursor.execute(sql)
        viewtuple = cursor.fetchall()
        cursor.close()
        return viewtuple

    def findviewname(self):
        cursor = self.gxviewdb.cursor()
        sql = "select viewname from gxviewtable "
        cursor.execute(sql)
        viewtuple = cursor.fetchall()
        cursor.close()
        return viewtuple

    """
    更新图片的路径
    """
    def updateViewImgPathById(self,filePath,rowId:int):
        sql = "UPDATE gxviewtable SET viewimgPath = '%s' WHERE id = %d" % (filePath,rowId)
        try:
            cursor = self.gxviewdb.cursor()
            cursor.execute(sql)
            # 提交到数据库执行
            self.gxviewdb.commit()
        except:
            # 发生错误时回滚
            self.gxviewdb.rollback()
        print("图片路径已经更新")

    def savePicInto(self,imgurl:str,fileId:int):
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        req = request.Request(imgurl,headers = headers)
        response = request.urlopen(req)
        filePath = "E:/weixinPic/{0}.jpg".format(fileId)
        with open(filePath,mode="wb") as f:
            f.write(response.read())

        return filePath

    """获取未发布的数量"""
    def getUnPubulishCount(self):
        cursor = self.gxviewdb.cursor()
        sql = "SELECT count(*) FROM gxview.gxviewtable where viewused=0"
        cursor.execute(sql)
        count = cursor.fetchone()
        return count


    def closegxviewdb(self):
        self.gxviewdb.close()