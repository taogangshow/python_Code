#阶层
#5! = 5*4*3*2*1
#4! = 4*3*2*1
i = 1
result = 1
while i<=5:
    result = result*i
    i+=1
print(result)

#5! = 5*4!
#4! = 4*3!

def getNums(num):
    if num>1:
        return num*getNums(num-1)
    else:
        return num

result = getNums(int(input("清输入一个整数:")))
print(result)

'''
def getNums(num):
    i = 1
    result = 1
    while i<=num:
        result=result*i
        i+=1
    return result
ret = getNums(int(input("请输入一个整数:")))
print(ret)
'''
