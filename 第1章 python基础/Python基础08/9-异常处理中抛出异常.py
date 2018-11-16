class Test(object):
    def __init__(self,switch):
        self.switch = switch
    def throw(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("已捕获到异常，信息如下:")
                print(result)
            else:
                raise
test = Test(True)
test.throw(11,0)

print("-----------华丽的分割线-----------")

test.switch = False
test.throw(11,0)
