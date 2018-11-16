ticket = input("是否有车票(1代表有,2代表没有)")
if ticket !="1":
    print("没有车票还不赶紧去买")
else:
    print("通关,接下来请您接受安检...")
    knifelenght = int(input("请输入您携带刀的长度(cm):"))
    if knifelenght <= 10:
        print("顺利通过安检,请到候车室候车...")
    else:
        print("您携带的刀具不符合规定,不允许坐车")
