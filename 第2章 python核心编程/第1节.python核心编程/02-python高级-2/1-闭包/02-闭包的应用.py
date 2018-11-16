def test(a,b):
    def test_in(x):
        print(a*x+b)
    return test_in

line1 = test(1,2)
line1(0)
line2 = test(3,4)
line2(0)

'''
#以前的方法是:
def creatNum(a,b,x):
    print(a*x+b)

a = 1
b = 2
x = 0
creatNum(a,b,x)
'''
