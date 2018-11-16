class Dog:
    def __init__(self,new_name):
        self.name = new_name
        self.__age = 0 #定义了一个私有属性,属性的名字是__age
    def set_age(self,new_age):
        if new_age>0 and new_age<=100:
            self.__age = new_age
        else:
            self.__age = 0
    def get_age(self):
        return self.__age
dog = Dog("小黑")
dog.set_age(10)
age = dog.get_age()
print(age)
print(dog.__age)
