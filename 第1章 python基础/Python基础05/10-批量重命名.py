import os
#1.获取重命名文件夹的名字
folder_name = input("请输入要重命名的文件夹:")
#2.获取指定文件夹中所有文件的名字
file_names = os.listdir(folder_name)
#改变默认路径
os.chdir(folder_name)
#print(file_names)#for test
#3.重命名
i = 0
for name in file_names:
    i+=1
    os.rename(name,"金瓶梅"+str(i)+".avi")
test = os.getcwd()
print(test)
new_file_names = os.listdir("./")
print(new_file_names)
