def func(functionName):
    print("---func---1---")
    def func_in():
        print("---func_in---1---")
        ret = functionName()#保存返回来的hello world
        print("---func_in---2---")
        return ret #把hello world返回到15行处的调用
    print("---func---2---")
    return func_in
@func
def test():
    print("---test---")
    return "hello world"

ret = test()
print("test return value is %s"%ret)
