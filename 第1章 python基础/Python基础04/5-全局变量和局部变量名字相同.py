a = 100

def test():
    #global a
    a = 200
    print("a=%d"%a)

def test1():
    print("a=%d"%a)

test()
test1()
