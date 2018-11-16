import random,time
class shuangSeQiu(object):
    def __init__(self):
        self.redball = []
        self.blueball = []
    def getRedBall(self):
            while True:
                rednum = random.randint(1, 33)
                if rednum not in self.redball:
                    self.redball.append(rednum)
                    if len(self.redball)==6:
                        break
    def getBlueBall(self):
        bluenum = random.randint(1,16)
        self.blueball.append(bluenum)

    def printShuangSeQiu(self):
        self.redball.sort()
        self.redball.append(self.blueball)
        print("正在为您生成随机号码...请稍后...\n")
        time.sleep(2)
        print("随机生成的双色球号码为:%s\n"%self.redball)
class selfShuangSeQiu(object):
    def __init__(self,num1,num2,num3,num4,num5,num6):
        self.selfredball = []
        self.selfblueball = []
        self.selfnewball = []
        self.num = []
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6
        if self.num1 <=33 and self.num1>=1:
            self.selfredball.append(self.num1)
        else:
            print("您输入号码<%d>超过红球范围(1-33)"%self.num1)
        if self.num2 <= 33 and self.num2 >= 1:
            self.selfredball.append(self.num2)
        else:
            print("您输入号码<%d>超过红球范围(1-33)"%self.num2)
        if self.num3 <= 33 and self.num3 >= 1:
            self.selfredball.append(self.num3)
        else:
            print("您输入号码<%d>超过红球范围(1-33)"%self.num3)
        if self.num4 <= 33 and self.num4 >= 1:
            self.selfredball.append(self.num4)
        else:
            print("您输入号码<%d>超过红球范围(1-33)"%self.num4)
        if self.num5 <= 33 and self.num5 >= 1:
            self.selfredball.append(self.num5)
        else:
            print("您输入号码<%d>超过红球范围(1-33)"%self.num5)
        if self.num6 <= 33 and self.num6 >= 1:
            self.selfredball.append(self.num6)
        else:
            print("您输入号码<%d>超过红球范围(1-33)"%self.num6)
    def getRedBall(self):
        if self.selfblueball != []:
            self.selfredball.sort()
            self.selfredball.append(self.selfblueball)
            #self.selfredball.sort()
            #print(self.selfredball)
        for i in self.selfredball:
            if i not in self.selfnewball:
                self.selfnewball.append(i)

            elif self.selfnewball.count(i)>=2:
                self.selfredball.remove(i)
                print("有重复号码:%s ,不符合双色球规则\n"%i)
                continue
            else:
                self.num.append(i)
        if(len(self.selfnewball))==7:
            print("输入成功,正在为您生成,请稍后...\n")
            time.sleep(2)
            print("您输入的双色球号码为:%s\n" % self.selfnewball)
        else:
            if self.num != []:
                print("有重复号码:%s ,不符合双色球规则\n" %self.num)
                print("生成随机双色球号码不成功,请重新输入...\n")
            else:
                time.sleep(2)
                print("生成随机双色球号码不成功,请重新输入...\n")
    def getBlueBall(self,num7):
        self.num7 = num7
        if self.num7 >16:
            print("您输入号码<%d>超过篮球范围(1-16)\n"%self.num7)
        elif self.num7<1:
            print("您输入号码<%d>超过篮球范围(1-16)\n"%self.num7)
        else:
            self.selfblueball.append(self.num7)
def print_menu():
    print('''
                    ----------功能列表------------
                    -------1:打印随机号码--------- 
                    -------2:自助选取号码--------- 
                    -------3:退出程序------------- 
                    ''')
def main():
    print_menu()
    while True:
        content = int(input("请选择功能:"))
        test = shuangSeQiu()
        if content == 1:

            test.getRedBall()
            test.getBlueBall()
            test.printShuangSeQiu()
            time.sleep(1)
        elif content == 2:
            print("请依次输入6个红球的号码(1-33)")
            num1 = int(input("请输入第1个红球号码:"))
            num2 = int(input("请输入第2个红球号码:"))
            num3 = int(input("请输入第3个红球号码:"))
            num4 = int(input("请输入第4个红球号码:"))
            num5 = int(input("请输入第5个红球号码:"))
            num6 = int(input("请输入第6个红球号码:"))
            print("请输入第7位蓝球的号码(1-16)")
            num7 = int(input("请输入第7个蓝球号码:"))
            test1 = selfShuangSeQiu(num1,num2,num3,num4,num5,num6)
            test1.getBlueBall(num7)
            test1.getRedBall()
        elif content == 3:
            print("正在退出...请稍后...\n")
            time.sleep(2)
            break
        else:
            print("sorry 没有这个功能选项请重新输入...\n")

if __name__ == "__main__":
    main()



