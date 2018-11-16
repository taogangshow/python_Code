class Cat:
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫在喝水...")
    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))
tom = Cat("汤姆",18)
tom.eat()
tom.drink()
#tom.name="汤姆"
#tom.age=18
tom.introduce()
lanmao = Cat("蓝猫",12)
#lanmao.name="蓝猫"
#lanmao.age=12
lanmao.introduce()
