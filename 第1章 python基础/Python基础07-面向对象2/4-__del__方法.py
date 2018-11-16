class Dog():
    def __del__(self):
        print("游戏结束GameOver!")
dog1 = Dog()
dog2 = dog1
del dog1#不会调用__del__方法,因为这个对象还有其他变量指向它,即引用计数不为0
del dog2#此时会调用__del__方法,即引用计数为0
print("=============")
#如果在程序结束时,有些对象还存在，那么python解释器会自动调用它们的__del__方法来完成清理工作
