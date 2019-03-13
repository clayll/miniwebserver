

import threading,time,queue

def foo(name):
    time.sleep(2)
    print("name:{}\n".format(name))

def testThread():
    myAttend = []
    for x in range(5):
        t = threading.Thread(target=foo,args=(x,))
        t.setDaemon(True)

        t.start()
        t.join()
        myAttend.append(t)

    t3 = threading.Thread(target=foo, args=(56,))
    t3.setDaemon(True)
    t3.start()


    print("main end")

q = queue.Queue(maxsize=5)

def produce():
    for x in range(5):

        s = "生成了item:{}\n".format(x)
        q.put(s)
        print(s)
        # time.sleep(2)

def customer():
    while True:
        time.sleep(1)
        item = q.get()
        print("已经完成了：{}\n".format(item))
        q.task_done()
        # print("队列是否为空：{}".format(q.empty()))

if __name__ == "__main__":
    t = threading.Thread(target=produce)
    t.setDaemon(True)
    t.start()
    # t.join()
    for i in range(3):
        t = threading.Thread(target=customer)
        t.setDaemon(True)
        t.start()

    #
    q.join()
    print("--end--")