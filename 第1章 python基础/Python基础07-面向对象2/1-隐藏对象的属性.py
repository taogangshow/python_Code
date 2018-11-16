class Dog:
    #def __str__(self):
        #return "%s的年龄是:%d"%(self.name,self.age)
    def set_name_age(self,new_name,new_age):
        self.name = new_name
        if new_age>0 and new_age<=100:
            self.age = new_age
        else:
            self.age = 0
    def get_name_age(self):

        return self.name,self.age
dog = Dog()
dog.set_name_age("小黑",10)
name_age = dog.get_name_age()
print(name_age)
#print(dog)
#dog.name = "小黑"
#dog.age = 10
#print("%s的年龄是:%d"%(dog.name,dog.age))
