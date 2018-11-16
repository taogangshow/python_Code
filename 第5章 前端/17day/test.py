from functools import reduce
info1 = [1,2,3,4,5,6]

for i in info1:
	if i%2==0:
		info1.remove(i)
print("info1",info1)


info2 = [1,2,3,4,5,6]
print("info2",[i for i in info2 if i%2==1])

info3 = [1,2,3,4,5,6]
print("info3",info3[0::2])

def test(a,b,func):
	result = func(a,b)
	return result
num = test(11,22,lambda x,y:x+y)
print(num)

s = [(i,j,k) for i in range(3) for j in range(2) for k in range(3)]
print(s)

i = 1
sum=0
while i<101:
	sum+=i
	i+=1
print(sum)

def sum(a, b):
    return a + b
print(reduce(sum, range(1,101)))