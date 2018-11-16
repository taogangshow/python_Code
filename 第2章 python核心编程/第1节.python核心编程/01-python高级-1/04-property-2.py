class Test(object):
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        print("---getter---")
        return self.__num
    @num.setter
    def num(self,new_num):
        print("---setter---")
        self.__num = new_num

t = Test()

t.num = 500#相当于调用了t.setNum(500)
print(t.num)#相当于调用了t.getNum()


