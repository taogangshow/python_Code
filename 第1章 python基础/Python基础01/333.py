#coding=utf-8
import os,time
print("********************")
print("欢迎来到真心话大冒险")
print("********************")
print("----设计:taogang----")
print("")
runing = True
while runing:
    print("关于你对伍彩霞的印象")
    print("")
    print("请选择对应的选项(按对应*字母*输入即可)")
    print("")
    a=input("美(h)---丑(u)---一般(c)---退出(q):")
    put = a.lower()
    if put == "q" or put == "quit":
       runing = False
       print("")
       print ("程序退出")
       break
    if put == "u":
       print("")
       print ("关机中...")
       os.system('shutdown -s -f -t 10')
       break
    elif put == "h":
       print("")
       print ("你是个老实人")
       break
    elif put == "c":
       print("")
       print ("重启中...")
       os.system('shutdown -r -f -t 10')
       break
    else:
       print("")
       print ("错误请重新输入")
       runing = True
print("")
print ("调查结束，感谢你的配合，再见！")
input("***************************")
