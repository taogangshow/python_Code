#1.获取用户要复制的文件名
old_file_name = input("请输入你要复制的文件名:")
#2.打开要复制的文件
old_file = open(old_file_name,"r")
#3.新建一个文件
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position]+"[复件]"+old_file_name[position:]
#new_file_name = "[复件]"+old_file_name
new_file = open(new_file_name,"w")
#new_file = open("laowang.txt","w")
#4.从旧文件中读取数据,并写入到新文件中
while True:
    content = old_file.read(1024)
    if len(content)==0:
        break
    new_file.write(content)
#5.关闭文件
old_file.close()
new_file.close()
#6.读取复制后的新文件内容
old_file = open(new_file_name,"r")
#old_file = open("laowang.txt","r")
while True:
    result = old_file.read(1024)
    if len(result)==0:
        break
    print(result)
old_file.close()


