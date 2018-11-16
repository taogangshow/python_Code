#coding=utf-8
high=input("请输入您的身高:")
high_num=int(high)
if high_num>180:
    print("高")
elif high_num<170:
    print("矮")
else:
    print("正常")
    
