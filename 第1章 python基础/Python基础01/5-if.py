print("===================")
color = input("您白吗？")
money = int(input("请输入您的资产总和:"))
beautiful = input("您美吗？")
if color == "白"and money>=1000000 and beautiful == "美":
    print("===================")
    print("您属于白富美")
    print("===================")
elif color == "白" and money<1000000 and beautiful == "美":
    print("===================")
    print("您属于高颜值")
    print("===================")
elif color != "白" and money>1000000 and beautiful == "美":
    print("===================")
    print("您属于富美,跟白富美只差了白")
    print("===================")
elif color != "白" and money>1000000 and beautiful != "美":
    print("===================")
    print("您除了钱，啥都没有")
    print("===================")
elif color != "白" and money<1000000 and beautiful == "美":
    print("===================")
    print("您除了美，啥都没有")
    print("===================")
elif color == "白" and money<1000000 and beautiful != "美":
    print("===================")
    print("您除了白，啥都没有")
    print("===================")
else:
    print("===================")
    print("您属于穷屌丝")
    print("===================")
input("请按回车<enter>即可关闭窗口")

