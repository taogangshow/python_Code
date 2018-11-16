"""1"""
def test(a,b):
    result = a+b
    print("result=%d"%result)

test(11,22)
test(33,22)
test(44,22)
print("="*50)
"""2"""
def test1(a,b=22):
    result = a+b
    print("result=%d"%result)

test1(11)
test1(33)
test1(44,44)
print("="*50)
"""3"""
def test2(a,b=22,c=33):
    print(a)
    print(b)
    print(c)

test2(11,c=44)
print("="*50)
"""4"""
def test3(a,d,b=22,c=33):
    print(a)
    print(b)
    print(c)
    print(d)

test3(11,22,c=44)
print("="*50)
"""5"""
def test4(a,d,b=22,c=33):
    print(a)
    print(b)
    print(c)
    print(d)

test4(d=11,a=22,c=44)
