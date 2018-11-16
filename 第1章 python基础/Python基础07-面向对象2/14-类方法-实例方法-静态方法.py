class Game(object):
    #类属性
    num = 0
    #实例方法
    def __init__(self):
        #实例属性
        self.name = "laowang"
    #类方法
    @classmethod
    def add_num(cls):#3.不管是使用类去调还是对象去调,这个cls永远都指向Game这个类
        cls.num = 100
    #静态方法 类方法和实例方法都必须要有一个参数,而静态方法可以没有,静态方法一般完成最基本的功能,既和类没有关系也和实例对象没关系
    @staticmethod
    def print_menu():
        print("-----------------------")
        print("-----穿越火线V11.1-----")
        print("------1.开始游戏-------")
        print("------2.结束游戏-------")
        print("-----------------------")

game = Game()
#Game.add_num()#1.可以通过这个类的名字来调用类方法
game.add_num()#2.还可以通过这个类创建出来的对象来调用这个类方法
print(Game.num)
#Game.print_menu()#通过类去调用静态方法
game.print_menu()#通过实例对象去调用静态方法
