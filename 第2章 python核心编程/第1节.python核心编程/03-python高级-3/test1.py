class Test(object):
    def __init__(self,x):
        self.x = x
        self.y = "哈哈"
    def __getattribute__(self,z):
        if z == "x":
            return "呵呵"
        else:
            return object.__getattribute__(self,z)


t = Test("python")
print(t.x)
print(t.y)



