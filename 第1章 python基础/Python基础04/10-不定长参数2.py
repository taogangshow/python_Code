def test(a,b,c=33,*args,**kwargs):
    print("="*50)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(11,22,33,44,55)
test(11,22,33,90,89)
test(11,22,33,44,55,66,task=90,done=89)
