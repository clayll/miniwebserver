import sqlite3

class Web_User():
    def __init__(self, name, pwd ,email):
        self.name = name
        self.pwd = pwd
        self.email = email
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



    def register(self):
        """注册用户"""
        insert_dt_cmd = '''INSERT INTO USER (NAME,PWD,EMAIL) VALUES ('{}','{}','{}');
           '''.format(self.name,self.pwd,self.email)
        self.conn.execute(insert_dt_cmd)
        self.conn.commit()

    def auth_user(self):
        """验证用户"""
        result = self.conn.execute("select * from USER where NAME='{}'".format(self.name))
        print(result.fetchall())

user1 = Web_User("xiaohong","123",r"123123@163com")
# user1.init_tables()
user1.auth_user()