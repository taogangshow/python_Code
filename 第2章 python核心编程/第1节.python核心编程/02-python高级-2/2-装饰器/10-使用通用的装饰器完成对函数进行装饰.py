def func(functionName):
    def func_in(*args,**kwargs):
        print("---日志记录---")
        ret = functionName(*args,**kwargs)
        return ret 
    return func_in
@func
def test():
    return "hello world"

@func
def test2():
    print("---test2---")

@func
def test3(a):
    print("---test3---a=%d"%a)
    
ret = test()
print("test return value is %s"%ret)
ret2 = test2()
print("test2 return value is %s"%ret2)
test3(11)
