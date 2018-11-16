def main():
    count = 0
    c = 0
    while count<=8:
        a = int(input("请输入甲车的数量(0~8):"))
        b = 8-a
        peo_a = 80*a
        peo_b = 290-peo_a
        lu_a = 10*a
        lu_b = 100-lu_a
        if a*80+b*30>=290 and a*10+b*20>=100:
            print("方案可行")
            print("甲车:%d(辆),乙车:%d(辆)"%(a,b))
            print("甲车人数:%d(人),乙车人数:%d(人)"%(peo_a,peo_b))
            print("甲车行李:%d(件),乙车行李:%d(件)"%(lu_a,lu_b))
            c+=1
            #print(c) for test
        elif b<0:
            print("错误输入")
        else:
            print("方案不可行")
        count+=1
    return c
result = main()
print("一共有%d种方案"%result)
input("退出<Enter>")
