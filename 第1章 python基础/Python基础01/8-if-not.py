a =int(input("请输入一个正整数a："))
if a>=0 and a<=50:
    print("0到50之间的数")
else:
    print("大于50的数")

b =int(input("请输入一个正整数b："))
if not(b>=0 and b<=50):
    print("大于50的数")
else:
    print("0到50之间的数")
