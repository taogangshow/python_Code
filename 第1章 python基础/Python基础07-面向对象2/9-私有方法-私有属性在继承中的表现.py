class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def test1(self):
        print("------test1-----")
    def __test2(self):
        print("------test2-----")
    def test3(self):
        self.__test2()
        print(self.__num2)
class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)
b = B()
#b.test1()
#b.__test2() 私有方法并不能被继承
#print(b.num1)
#print(b.__num2) 私有属性不能被继承

b.test3()
b.test4()
#总结:如果调用的继承的父类中的公有方法，那么可以在这个共有方法中去访问父类中的私有属性和私有方法
#但是 如果在子类中实现了一个共有方法,那么这个方法是不能调用父类中的私有属性和私有方法的
