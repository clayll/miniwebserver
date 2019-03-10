import sqlite3


class Web_User():

    conn = sqlite3.connect('chat.db')

    @classmethod
    def init_tables(cls):
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS USER_INFO
                (NAME TEXT,
                PWD TEXT,
                EMAIL TEXT,
                LOGINNAME TEXT);
                '''
            # 主要就是上面的语句
            cls.conn.execute(create_tb_cmd)
            cls.conn.commit()
        except:
            print("Create table failed")

    def getConnction(self):
        pass

    @classmethod
    def register(cls,name,loginName, pwd ,email):
        """注册用户"""
        insert_dt_cmd = '''INSERT INTO USER_INFO (NAME,PWD,EMAIL,LOGINNAME) VALUES ('{}','{}','{}','{}');
           '''.format(name,  pwd ,email,loginName)
        cls.conn.execute(insert_dt_cmd)
        cls.conn.commit()
        print("注册成功")

    @classmethod
    def login(cls,loginName,pwd):
        """验证用户"""
        result = cls.conn.execute("select  * from USER_INFO where LOGINNAME='{}' and PWD ='{}'".format(loginName, pwd))
        user =  result.fetchall()
        if user:
            print("登录成功")
            return user[0]
        return None


if __name__ == "__main__":
    Web_User.init_tables()
    while True:
        args = input("输入1.注册用户;输入2.验证注册是否成功;输入Q退出")
        if args == '1':
            loginname = input("输入登录名:")
            name = input("输入显示名:")
            pwd = input("输入密码:")
            email = input("输入电子邮箱:")
            Web_User.register(name, loginname, pwd, email)

        elif args == '2':
            loginname = input("输入登录名:")
            pwd = input("输入密码:")
            Web_User.login(loginname,pwd)
        elif args.upper() == "Q":
            break
        else:
            print("输入错误重新输入")
