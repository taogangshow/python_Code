try:
    #print(num)
    open("xxx.txt")
    print("---1---")
except NameError:
    print("捕获异常后的处理...")
except FileNotFoundError:
    print("文件不存在")
print("---2---")
