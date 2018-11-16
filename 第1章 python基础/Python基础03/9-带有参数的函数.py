#定义一个函数
def sum_1_nums():
    a = 10
    b = 20
    result = a+b
    print("%d+%d=%d"%(a,b,result))
#调用函数
sum_1_nums()
print("="*50)

def sum_2_nums(a,b):
    result = a+b
    print("%d+%d=%d"%(a,b,result))
num1 = int(input("请输入第1个数字:"))
num2 = int(input("请输入第2个数字:"))
sum_2_nums(num1,num2)

