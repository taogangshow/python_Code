'''
class Dog:
    #私有方法
    def __test1(self):
        print("---1---")
    #公有方法
    def test2(self):
        print("---2---")
dog = Dog()
dog.__test1()
dog.test2()
'''
class Dog:
    def __send_msg(self):
        print("正在发送短信...")
    def send_msg(self,new_money):
        if new_money>10000:
            self.__send_msg()
        else:
            print("余额不足,请充值后,再发送短信...")
dog = Dog()
dog.send_msg(100)
        

