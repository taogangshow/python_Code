class Cat:
    #属性

    #方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫在喝水...")
#创建一个对象
tom = Cat()
#调用tom指向的对象中的方法
tom.eat()
tom.drink()
#向tom指向的对象中添加name.age属性
tom.name="汤姆"
tom.age=18
