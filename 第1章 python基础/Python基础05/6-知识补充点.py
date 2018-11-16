a = 100
def test(num):
    num+=num
    print(num)
test(a)
print(a)

b = [100]
def test(num):
    num+=num
    print(num)
test(b)
print(b)

c = [100]
def test(num):
    num = num+num
    print(num)
test(c)
print(c)
