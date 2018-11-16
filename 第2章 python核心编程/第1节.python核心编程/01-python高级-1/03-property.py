class Test(object):
    def __init__(self):
        self.__num = 100
    def setNum(self,new_num):
        print("---setter---")
        self.__num = new_num
    def getNum(self):
        print("---getter---")
        return self.__num
    num = property(getNum,setNum)

t = Test()
#print(t.__num)
#t.__num = 200

print(t.getNum())
t.setNum(50)
print(t.getNum())
print("-"*50)
t.num = 500#相当于调用了t.setNum(500)
print(t.num)#相当于调用了t.getNum()
#注意点:
#t.num 到底是调用getNUm()还是setNum(),要根据实际的场景来判断
#1.如果是给t.num赋值,那么一定是调用setNum()
#2.如果是获取t.num的值,那么就一定调用getNum()
#property的作用:相当于把方法进行了封装,开发者在对属性设置数据的时候更方便


