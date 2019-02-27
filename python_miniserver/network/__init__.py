from network.miniserver_01 import Web_server
from network.Web_User import Web_User
from network.clinet_01 import Web_Client


if __name__ == "network":
#2. 客户登录后，启动客户端
    userhelp = Web_User()
    userinfo = userhelp.login("xiaohong","123")
    if  userinfo:
        user1 = Web_Client(userinfo)
        user1.createConnter()
        print(userinfo[0])

        Web_server.loginusers[userinfo[0]]=userinfo
        user1.send_message("123")
        user1.send_message("345")
        user1.send_message("444444")


    #3. 用户登录
