def test(a,b,c=33,*args,**kwargs):
    print("="*50)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

A = (44,55,66)
B = {"name":"laowang","age":18}

test(11,22,33,A,B)
test(11,22,33,*A,**B)
