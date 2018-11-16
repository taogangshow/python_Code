#1.打印功能提示
print("="*50)
print("名片管理系统v1.0")
print("1.添加一个新的名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示所有的名片")
print("6.退出系统")
print("="*50)
#定义一个列表用来存储名片
card_infors = []
while True:
    #2.获取用户的输入
    num = int(input("请输入操作序号:"))

    #3.根据用户的输入执行相应的功能
    if num == 1:
        new_name = input("请输入新的名字:")
        new_qq = int(input("请输入新的QQ:"))
        new_weixin = input("请输入新的微信:")
        new_addr = input("请输入新的地址:")
        #定义一个字典用来存储新的名片
        new_infor = {}
        new_infor['name']=new_name
        new_infor['qq']=new_qq
        new_infor['weixin']=new_weixin
        new_infor['addr']=new_addr
        #将一个字典添加到列表中
        card_infors.append(new_infor)
        print("添加新名片成功")
    elif num ==2:
        del_name = input("请输入你要删除的名字:")
        find_flag = 0#默认表示没有找到
        for temp in card_infors:
            if del_name==temp['name']:
                find_flag = 1#表示找到了
                card_infors.remove(temp)
                print("删除成功")
                break
        if find_flag==0:#表示没有找到
            print("没有你要删除人的信息...")
    elif num ==3:
        mod_name = input("请输入你想要修改的名字:")
        find_flag = 0#默认没有找到
        modify_flag = 0#默认没有修改成功
        sign = 0
        for temp in card_infors:
            sign+=1
            if mod_name==temp['name']:
                find_flag=1#表示找到了
                print("1.修改名字")
                print("2.修改QQ")
                print("3.修改weixin")
                print("4.修改地址")
                print("5.退出修改")
                while True:
                    print(card_infors)
                    num2 = int(input("请输入修改选项:"))
                    if num2==1:
                        card_infors[sign-1]['name']=input("请输入你要修改的正确名字:")
                        modify_flag = 1
                    elif num2==2:
                        card_infors[sign-1]['qq']=int(input("请输入你要修改的正确QQ:"))
                        modify_flag = 1
                    elif num2==3:
                        card_infors[sign-1]['weixin']=int(input("请输入你要修改的正确weixin:"))
                        modify_flag = 1
                    elif num2==4:
                        card_infors[sign-1]['addr']=input("请输入你要修改的正确地址:")
                        modify_flag = 1
                    elif num3==5:
                        break
                    else:
                        print("输入错误,请重新输入")
                    if modify_flag==1:#判断是否修改成功
                        print("修改成功")
                        break
                break
        if find_flag==0:
            print("没有你要修改人的信息...")
    elif num ==4:
        find_name = input("请输入你想要查找的名字:")
        find_flag = 0#默认表示没有找到
        for temp in card_infors:
            if find_name==temp['name']:
                print("姓名\tQQ\t微信\t地址")
                print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
                find_flag=1#表示找到了
        if find_flag==0:#表示没有找到
            print("查无此人")
    elif num ==5:
        print("姓名\tQQ\t微信\t地址")
        for temp in card_infors:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
    elif num ==6:
        break
    else:
        print("输入错误,请重新输入")
    print("")
