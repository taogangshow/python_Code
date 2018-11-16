print("===================")
color = input("您高吗？")
money = int(input("请输入您的资产总和:"))
beautiful = input("您帅吗？")
if color == "高"and money>=1000000 and beautiful == "帅":
    print("===================")
    print("您属于高富帅")
    print("===================")
elif color == "高" and money<1000000 and beautiful == "帅":
    print("===================")
    print("您属于高颜值")
    print("===================")
elif color != "高" and money>1000000 and beautiful == "帅":
    print("===================")
    print("您属于富帅,跟高富帅只差了高")
    print("===================")
elif color != "高" and money>1000000 and beautiful != "帅":
    print("===================")
    print("您除了钱，啥都没有")
    print("===================")
elif color != "高" and money<1000000 and beautiful == "帅":
    print("===================")
    print("您除了帅，啥都没有")
    print("===================")
elif color == "高" and money<1000000 and beautiful != "帅":
    print("===================")
    print("您除了高，啥都没有")
    print("===================")
elif color == "高" and money>1000000 and beautiful != "帅":
    print("===================")
    print("你属于高富,跟高富帅只差了帅")
    print("===================")
else:
    print("===================")
    print("您属于穷屌丝")
    print("===================")
input("请按回车<enter>即可关闭窗口")

