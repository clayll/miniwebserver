dictionary = {}
while True:
    input_fun = input("请输入功能：1.添加单词 2.查询单词 3.退出")
    try:
        i = int(input_fun)
        if i == 1:
            key = input("添加单词:")
            value = input("添加单词定义:")
            dictionary[key] = value
        if i == 2:
            key = input("输入查询单词:")
            if key in dictionary:
                print("单词定义: "+dictionary[key])
            else:
                print("没有查询到对应单词")
        if i == 3:
            break

    except:
        print("输入错误请重新输入！")