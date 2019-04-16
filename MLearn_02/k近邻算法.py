from sklearn import neighbors
from sklearn import datasets
from sklearn import model_selection
import numpy as np

def irisShow():

    # 加载花的数据
    rs = datasets.load_iris()
    # 数据说明
    print(rs.feature_names)
    print(rs.target_names)
    #特征值
    x = rs["data"]
    #目标值
    y = rs["target"]

    # 训练数据与测试数据

    x_train, x_test, y_train, y_test = \
        model_selection.train_test_split(x, y, test_size = 0.25, random_state = 42)

    nkn = neighbors.KNeighborsClassifier(n_neighbors=8)
    nkn.fit(x_train, y_train)
    x_test[0,0]=20
    x_test[3,0] = 70
    print(nkn.predict(x_test))
    print(nkn.score(x_test,y_test))

def neighbors_1():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]

    neigh = neighbors.KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X, y)
    print(neigh.predict([[0.9]]))  # 预测出所在类样本标签
    print(neigh.predict_proba([[0.9]]))  # 预测

z = 0

def myIter():
    global z
    import time
    x = (i for i in range(10))
    for j in x:

        z = z+1
        print("myItenr:{}".format(z))

def myIter1():
    global z
    x = (i for i in range(10))
    for j in x:

        z = z+1
        print("myItenr1:{}".format(z))

def simple_continue():
    print("strart")
    for i in range(10):
        x = yield
        print("recived:",x)
from collections import deque

def student(name, homeworks):
    for homework in homeworks.items():
        yield (name, homework[0], homework[1])  # 学生"生成"作业给老师

class Teacher(object):
    def __init__(self, students):
        self.students = deque(students)

    def handle(self):
        """老师处理学生作业"""
        while len(self.students):
            student = self.students.pop()
            try:
                homework = next(student)
                print('handling', homework[0], homework[1], homework[2])
            except StopIteration:
                pass
            else:
                self.students.appendleft(student)

# coroutine.py
import asyncio
import datetime
@asyncio.coroutine  # 声明一个协程
def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(2)



if __name__ == '__main__':
    # irisShow()
    # x = simple_continue()
    # next(x)
    # # x.send("测试")
    # x.send("123")
    # x.send("cds")
    # Teacher([
    #     student('Student1', {'math': '1+1=2', 'cs': 'operating system'}),
    #     student('Student3', {'math': '2+2=4', 'cs': 'computer graphics'}),
    #     student('Student2', {'math': '3+3=5', 'cs': 'compiler construction'})
    # ]).handle()
    loop = asyncio.get_event_loop()  # 获取一个event_loop
    tasks = [display_date(1, loop), display_date(2, loop)]
    loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
    loop.close()


