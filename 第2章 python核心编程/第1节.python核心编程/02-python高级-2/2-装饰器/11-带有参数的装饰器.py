def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---记录日志---%s"%arg)
            if arg == "hello world":
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func
#1.先执行func_arg("hello world")函数,这个函数return的结果就是func这个函数的引用
#2.@func
#3.使用@func对test函数进行装饰
@func_arg("hello world")
def test():
    print("---test---")
#带有参数的装饰器,能够起到在运行时,有不同的功能
@func_arg("hello python")
def test2():
    print("---test2---")
test()
test2()
