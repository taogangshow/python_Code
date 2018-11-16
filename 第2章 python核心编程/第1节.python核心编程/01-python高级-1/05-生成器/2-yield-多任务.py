def test1():
    while True:
        print("---test1---")
        yield None

def test2():
    while True:
        print("---test2---")
        yield None

t1 = test1()
t2 = test2()
while True:
    t1.__next__()
    t2.__next__()
#多任务一共有三种:协程,进程,线程
#以上代码属于协程,协程一般最快
