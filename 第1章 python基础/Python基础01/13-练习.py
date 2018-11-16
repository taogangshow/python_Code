sex = input("请输入您的性别(男或女):")
if sex =="男":
    a = input("请输入您老婆的肤色(白-黄-黑):")
    b = int(input("请输入您老婆的存款:"))
    c = input("您老婆美吗:")
    if a=="白" and b>=1000000 and c=="美":
        print("你老婆属于白富美")
    else:
        print("你老婆不属于白富美")
elif sex =="女":
    d = int(input("请输入您老公的身高(cm):"))
    e = int(input("请输入您老公的存款:"))
    f = input("您老公帅吗:")
    if d>=180 and e>=10000000 and f=="帅":
        print("你老公属于高富帅")
    else:
        print("你老公不属于高富帅")
else:
    print("输入错误请重新输入")
