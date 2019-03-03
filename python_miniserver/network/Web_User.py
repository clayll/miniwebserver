import sqlite3


class Web_User():

    conn = sqlite3.connect('chat.db')

    @classmethod
    def init_tables(cls):
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS USER
                (NAME TEXT,
                PWD TEXT,
                EMAIL TEXT);
                '''
            # 主要就是上面的语句
            cls.conn.execute(create_tb_cmd)
            cls.conn.commit()
        except:
            print("Create table failed")

    def getConnction(self):
        pass

    @classmethod
    def register(cls,name, pwd ,email):
        """注册用户"""
        insert_dt_cmd = '''INSERT INTO USER (NAME,PWD,EMAIL) VALUES ('{}','{}','{}');
           '''.format(name,  pwd ,email)
        cls.conn.execute(insert_dt_cmd)
        cls.conn.commit()

    @classmethod
    def login(cls,name,pwd):
        """验证用户"""
        result = cls.conn.execute("select  * from USER where NAME='{}' and PWD ='{}'".format(name, pwd))
        user =  result.fetchall()
        if user:
            return user[0]
        return None