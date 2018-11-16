#1.打印功能提示
print("*"*50)
print("---欢迎您进入名字查询系统---")
print("1:添加一个新的名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("5:退出程序")
print("*"*50)
names = []#定义一个空的列表来存储添加的名字
while True:
    #2.获取用户的选择
    num = int(input("请输入功能序号:"))
    #3.根据用户的选择执行相应的功能
    if num==1:
        new_name = input("请输入名字:")
        names.append(new_name)
        print("添加成功:", names)
    elif num==2:
        rm_name = input("请输入你要删除的名字:")
        if rm_name in names:
            names.remove(rm_name)
            print("删除成功")
        else:
            print("请检查名字是否输入正确,或者按4查询是否存在此名字")
    elif num==3:
        mod_name = input("请输入你要修改的名字:")
        if mod_name in names:
            #获取删除名字的下标
            s = names.index(mod_name)
            #获取用户修改后的名字并修改
            names[s] = input("请输入修改后的名字:")
            print("修改成功")
        else:
            print("请检查名字是否输入正确,或者按4查询是否存在此名字")
    elif num==4:
        find_name = input("请输入要查询的名字:")
        if find_name in names:
            print("已找到你要找的人")
        else:
            print("查无此人")
    elif num==5:
        break
    else:
        print("输入无效,请重新输入")
