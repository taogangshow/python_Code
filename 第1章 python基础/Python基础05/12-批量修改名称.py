import os
folder_name = input("请输入要修改名称的文件夹:")
file_names = os.listdir(folder_name)
for name in file_names:
    #例:将[东京出品]-1.txt　修改成1.txt把前面的给删除了
    #找到将去掉的下标,[0:-]这部分不要,[-+1:]是要的
    ls = name.rfind("-")
    #截取自己想要的格式用切片
    new = name[ls+1:]
    old_file_names = folder_name+"/"+name
    new_file_names = folder_name+"/"+new
    os.rename(old_file_names,new_file_names)
