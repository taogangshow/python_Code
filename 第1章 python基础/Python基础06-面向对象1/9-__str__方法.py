class Cat:
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    def __str__(self):
        return "%s的年龄是:%d"%(self.name,self.age)
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫在喝水...")
    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))
tom = Cat("汤姆",18)
lanmao = Cat("蓝猫",12)

print(tom)
print(lanmao)

