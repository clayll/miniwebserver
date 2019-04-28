#coding:utf-8
import pymysql
import datetime

class viewDao:
    def __init__(self):
        #数据名字和数据库连接密码要换掉
        self.gxviewdb = pymysql.connect(user='root', db='gxview', passwd='123456', host='localhost',
                             charset='utf8')  # 指定编码格式为utf-8，否则显示乱码

    def saveview(self, views):
        sql = 'insert gxviewtable(viewname, viewlink, viewimglink, viewlength, viewtype,createTime) values ("%s","%s","%s","%s","%s","%s")'%(views[0],views[1],views[2],views[3],views[4],datetime.datetime.now())
        cursor = self.gxviewdb.cursor()
        cursor.execute(sql)
        self.gxviewdb.commit()
        cursor.close()

    def changeview(self, viewdatas):
        viewnameindex = 2
        for data in viewdatas:
            sql = "UPDATE gxviewtable SET viewused = 1 WHERE viewname = '%s'" % (data[viewnameindex])
            try:
                cursor = self.gxviewdb.cursor()
                cursor.execute(sql)
                # 提交到数据库执行
                self.gxviewdb.commit()
            except:
                # 发生错误时回滚
                self.gxviewdb.rollback()
        print("数据库已经修改")

    def savetest(self, i):
        pass

    def findviewunused(self, viewcount):
        cursor = self.gxviewdb.cursor()
        sql = "select * from gxviewtable where viewused=0 limit %d" %(viewcount)
        cursor.execute(sql)
        viewtuple = cursor.fetchall()
        cursor.close()
        return viewtuple

    def findviewname(self):
        cursor = self.gxviewdb.cursor()
        sql = "select viewname from gxviewtable"
        cursor.execute(sql)
        viewtuple = cursor.fetchall()
        cursor.close()
        return viewtuple

    def closegxviewdb(self):
        self.gxviewdb.close()