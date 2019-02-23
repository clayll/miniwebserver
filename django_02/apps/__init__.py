class C:

    name = "C公有静态字段"


    def func(self):
        print( C.name)

    @classmethod
    def func2(cls):
        print(cls.name)

    @staticmethod
    def func3():
        print(C.name)

class A:
    name = "A公有静态字段"

    def func(self):
        print(C.name)

class D(A, C):

    def show(self):
        print (self.name)



#
# obj = C()
# obj.func()     # 类内部可以访问
# obj.func2()
# C.func2()
# C.func3()

#
obj_son = D()
obj_son.show() # 派生类中可以访问
def logging(level):
    def wrapper(func):
        def debug(*args, **kwargs):
            import inspect
            caller_name = inspect.stack()[1][3]
            print("[%s]: enter {}()" % level.format(caller_name) )
            return func(*args, **kwargs)
        return debug
    return wrapper

def wrapper(func):
    def debug(*args, **kwargs):
        import inspect
        caller_name = inspect.stack()[1][3]
        print("[]: enter {}()" .format(caller_name) )
        return func(*args, **kwargs)
    return debug

@logging("info")
def say_hello(somting):
    print(somting)
@logging("debugger")
def say_goodbye(somting, xx):
    print(somting+xx)

def xx(d):
    print(d)

# s = wrapper(xx)
# s(("xxxxx"))

# say_hello("heelo")
# say_goodbye("test", "123")

class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)
@logging
def say(something):
    print("say {}!".format(something))

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

response = requests.get("http://www.sina.com", headers=headers)
print(response.text)
assert response.status_code == 200