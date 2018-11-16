def func(functionName):
    print("---func---1---")
    def func_in(*args,**kwargs):#如果a,b没有定义,那么会导致13行的调用失败
        print("---func_in---1---")
        functionName(*args,**kwargs)#如果没有a,b当作实参进行传递,那么会导致调用10行的函数失败
        print("---func_in---2---")
    print("---func---2---")
    return func_in
@func
def test(a,b,c):
    print("---test---%d---%d---%d"%(a,b,c))

@func
def test2(a,b,c,d):
    print("---test---%d---%d---%d---%d"%(a,b,c,d))

test(11,22,33)
test2(11,22,33,44)
