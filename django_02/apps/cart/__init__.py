import time
class User1:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __iter__(self):
        return self

    def __next__(self):
        x =  self.b
        self.b = self.b+self.a
        self.a = x
        return self.b

d = User1(1,2)


class OddNumber(object):
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        return (self.max)

