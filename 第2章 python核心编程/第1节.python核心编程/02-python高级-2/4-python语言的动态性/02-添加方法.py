import types
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s正在吃..."%self.name)

def run(self):
    print("%s正在跑..."%self.name)
p1 = Person("p1",18)
p1.eat()
#p1.run = run
#p1.run()#虽然p1对象中 run属性已经指向了8行的函数,但是这句代码还不正确
        #因为run属性指向的函数,是后来添加的,即p1.run()的时候,并没有把p1当作第
        #1个参数,导致了第8行的函数调用的时候,出现缺少参数的问题
p1.run = types.MethodType(run,p1)
p1.run()
