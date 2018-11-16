class Cat:
    #属性

    #方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫在喝水...")
    def introduce(self):
        print("%s的年龄是:%d"%(tom.name,tom.age))
        
#创建一个对象
tom = Cat()
#调用tom指向的对象中的方法
tom.eat()
tom.drink()
#向tom指向的对象中添加name.age属性
tom.name="汤姆"
tom.age=18
#获取属性的一种方式
#print("%s的年龄是:%d"%(tom.name,tom.age))
tom.introduce()

lanmao = Cat()
lanmao.name="蓝猫"
lanmao.age=12
lanmao.introduce()
