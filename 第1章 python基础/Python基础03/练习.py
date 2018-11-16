def sum_3_nums(a,b,c):#形参2
    result = a+b+c
    #print("%d+%d+%d=%d"%(a,b,c,result))
    return result
def average_3_nums(a1,a2,a3):#形参1
    result = sum_3_nums(a1,a2,a3)#实参2
    result = result/3
    #print("平均值:%d"%result)
    return result
def square_3_nums(a2,b2,c2):
    result = average_3_nums(a2,b2,c2)
    result = result**2
    print("和的平均值的平方:%d"%result)

num1 = int(input("请输入第1个数:"))
num2 = int(input("请输入第2个数:"))
num3 = int(input("请输入第3个数:"))
#sum_3_nums(num1,num2,num3)
#average_3_nums(num1,num2,num3)#实参1
square_3_nums(num1,num2,num3)
