'''
def get_wendu():
    wendu = 30
    return wendu
def print_wendu(wendu):#这个wendu与get_wendu()函数里定义的wendu没有任何关系
    print("当前的温度是:%d度"%wendu)
result = get_wendu()#如果一个函数有返回值,但是没有在调用函数之前，用个变量保存的话那么没有任何意义
print_wendu(result)
'''

#定义一个全局变量
#wendu = 0

def get_wendu():
    #如果wendu这个变量已经在全局变量的位置定义了，此时还想再函数中对这个全局变量进行修改的话那么仅仅是wendu=一个值 这还不够,,,此时wendu这个变量是一个局部变量，仅仅是和全局变量的名字相同罢了
    #wendu = 30

    #使用global用来对一个全局变量的声明,那么这个函数中的wendu=33就不是定义一个局部变量,而是对全局变量进行修改
    global wendu
    wendu = 30

def print_wendu():
    print("当前的温度是:%d度"%wendu)
get_wendu()
print_wendu()
