#coding=utf-8
import os,time
runing = True
while runing:
    a=input("关机(s)OR重启(r)?(q退出)")
    put = a.lower()
    if put == "q" or put == "quit":
        runing = False
        print ("程序退出")
        break
    seconds = int(input("请输入暂停时间(单位:秒)"))
    time.sleep(seconds)
    print ("暂停时间:"),seconds
    runing = False
    
    if put == "s":
       print ("关机中...")
       os.system('shutdown -s -f -t 10')
    elif put == 'r':
         print ("重启中...")
         system('reboot')
    else:
        print ("错误请重新输入")
        runing = True
print ("程序结束~~~!")
input("***************************")
