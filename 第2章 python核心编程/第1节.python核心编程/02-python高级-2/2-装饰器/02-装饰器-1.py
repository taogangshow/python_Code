def w1(func):
    def inner():
        print("---正在验证权限---")
        func()
    return inner
def f1():
    print("---f1---")
def f2():
    print("---f2---")

#innerfunc = w1(f1)
#innerfunc()

f1 = w1(f1)
f1()


