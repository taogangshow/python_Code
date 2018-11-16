def get_wendu():
    wendu = 25
    print("当前温度是:%d"%wendu)
    return wendu
def get_huashi(wendu):
    wendu = wendu*9/5+32
    print("当前华氏温度是:%d"%wendu)
result = get_wendu()#将获取的返回值赋值给result
get_huashi(result)#将result的值传递给变量wendu
#程序运行流程:将第一个函数的值25　return返回给get_wendu()这个函数,然后再将这个值赋值给result这个变量,最后通过get_huashi(result)将result的值传递给def get_huashi(wendu)函数中的wendu
