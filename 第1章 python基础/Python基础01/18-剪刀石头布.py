#导入所需包
import random
#获取玩家的输入
player = int(input("请输入　0剪刀　1石头 2布:"))
#让电脑随机出一个
computer = random.randint(0,2)
#玩家获胜的条件
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
    print ("恭喜你，你可以去high了")
#平局的条件
elif player == computer:
    print ("平局...不要走，决战到天亮")
else:
    print("你输了...回家拿钱，再来!!!")

input("退出<enter>")
