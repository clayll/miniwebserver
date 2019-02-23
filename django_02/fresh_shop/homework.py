
from io import  *
import os
import re

# 删除非空文件夹入口
def del_file_and_dir(path):
    # 定义递归函数，递归目录遍历所有的文件并且删除
    def del_recursion(path):
        # 遍历非空文件夹
        for dir in os.listdir(path):
            dir = os.path.join(path, dir)
            # 如果是文件，则直接删除
            if os.path.isfile(dir):
                # print("删除文件：%s " % os.path.join(input_path, dir))
                os.remove(dir)

            elif os.path.isdir(dir):
                # 如果是空目录则直接删除
                if len(os.listdir(dir)) == 0:
                    # print("删除空目录：%s" % os.path.join(path, dir))
                    os.rmdir(dir)
                else:
                    del_recursion(dir)
                    # 如果递归后路径是空的文件夹则直接删除
                    if len(os.listdir(dir)) == 0:
                        os.rmdir(dir)

    del_recursion(path)
    # 调用完递归后，把传入的最初文件夹删除
    if len(os.listdir(path)) == 0:
        os.rmdir(path)

# 1自己实现删除非空文件夹
# while True:
#     input_path = input("请输入要删除非空文件夹的绝对路径：（退出请输入q） ：")
#     try:
#         if input_path.upper() == 'Q':
#             break
#         # 2判断路径是否有效
#         if not os.path.exists(input_path):
#             raise Exception("该路径不存在，请重新输入！")
#         # 3判断是否为目录
#         if not os.path.isdir(input_path):
#             raise Exception("请输入文件夹路径！")
#         # 如果路径是空文件夹则不删除
#         if len(os.listdir(input_path)) == 0:
#             raise Exception("该目录是空文件，请重新输入！")
#         # 非空文件夹则递归全部删除
#         del_file_and_dir(input_path)
#
#     except Exception as rs:
#         print(rs)


def classify_txt(pathrul):
    txt_list = []
    other_list = []

    # 定义递归分类
    def classify_recursion(pathrul):
        for dir in os.listdir(pathrul):
            filename = os.path.join(pathrul, dir)
            if os.path.isfile(filename):
                r = re.match(r".+\.txt$", dir)
                if r:
                    txt_list.append(filename)
                else:
                    other_list.append(filename)
            else:
                classify_recursion(filename)

    classify_recursion(pathrul)
    return (txt_list, other_list)

# 2把所有txt文件和其它文件分类
# while True:
#     input_path = input("请输入要删除非空文件夹的绝对路径：（退出请输入q） ：")
#     try:
#         if input_path.upper() == 'Q':
#             break
#         # 2判断路径是否有效
#         if not os.path.exists(input_path):
#             raise Exception("该路径不存在，请重新输入！")
#         # 3判断是否为目录
#         if not os.path.isdir(input_path):
#             raise Exception("请输入文件夹路径！")
#         # 如果路径是空文件夹则不删除
#         if len(os.listdir(input_path)) == 0:
#             raise Exception("该目录是空文件，请重新输入！")
#         # 非空文件夹则递归全部删除
#         txt_list, other_list = classify_txt(input_path)
#         print("txt文本列表:")
#         [print(i) for i in txt_list]
#         print("其他文本列表:")
#         [print(i) for i in other_list]
#
#     except Exception as rs:
#         print(rs)


# 3列表推导式实现乘法口诀表
#
# result=[ str(a)+"*"+str(i) + "="+str(i*a)  for i in range(10) for a in range(10) if i >= a and i > 0 and a > 0]
#
# print(result)

# 4自己实现有序集合的切片

def custom_slice(sorted_ls ,slice_str):
    """
    自定义实现有序集合切片

    sorted_ls: 有序集合
    slice_str： 切片规则如：0:3
    """
    try:
        if not isinstance(sorted_ls, list):
            raise Exception("第一个参数请传入有序集合！")
        operls = slice_str.split(':')
        if len(operls) > 2:
            raise Exception("切片规则有错误，请输入：0:3或者 :2等，最多输入步长，既格式为：0:2")
        # 校验切片数据是否是数字
        for i in operls:
            try:
                if i != '':
                    int(i)
            except:
                raise Exception("切片规则只能输入整数！")

        start, end = operls[0], operls[1]
        if start == '':
            start = 0
        else:
            start = int(start)
        if end == '':
            end = len(sorted_ls)
        else:
            if int(end) < 0:
                end = len(sorted_ls) + int(end)
            else:
                end = int(end)

        for i in range(len(sorted_ls)):
            if i >= start and i < end:
                print(sorted_ls[i],end="\t")

    except Exception as re:
        print(re)

#
#
# basket = ['1', '2', '3', '4', '5', '6']
# custom_slice(basket, "1:6")
# custom_slice(basket, ":-1")
# print(basket[1:6])
# print(basket[:-1])

# 5.列表推导式把单词大写变成小写

while True:
    input_str = input("请输入要转换的字符串：（退出请输入q） ：")
    try:
        if input_str.upper() == 'Q':
            break
        print(str.join('', ([str.upper(i) for i in input_str])))

    except Exception as rs:
        print(rs)








