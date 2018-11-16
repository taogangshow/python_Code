try:
    11/0
    #print(num)
    #open("xxx.txt")
    print("---1---")
except (NameError,FileNotFoundError):
    print("捕获异常后的处理...")
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定能捕获到")
    print(ret)
else:
    print("没有异常才会执行的功能...")
finally:
    print("---finally---")
print("---2---")
