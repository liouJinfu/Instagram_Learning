#-*- encoding:UTF-8 -*-
import time
def log(func):
    def wrapper(*args, **kvargs):
        print "before calling",func.__name__, time.time()
        func(*args, **kvargs)
        print 'end calling', func.__name__, time.time()
    return wrapper
@log
def hello(name, age):
    print 'hello',name, age

def log1(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            print "before calling", func.__name__, "level =",level
            func(*args,**kvargs)
            print "end calling", func.__name__, "level =",level
        return wrapper
    return inner

@log1(level="INFO")
def hello2(name, age):
    print 'hello', name, age
if __name__ == '__main__':
    hello("jinfu", 2)
    hello2('hello1', 3)