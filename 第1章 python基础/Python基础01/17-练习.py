print("--------------------------矩形-------------------------------")
i = 1
while i<=5:
    j=1
    while j<=5:
         print("*",end="")
         j+=1
    print("")
    i+=1
print("-------------------------三角形-----------------------------")
i = 1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print("")
    i=i+1
print("------------------------九九乘法表-------------------------------")
i = 1
while i<=9:
    j=1
    while j<=i:
        print("x*y=z ",end="")
        j+=1
    print("")
    i+=1
print("-----------------------------------------------------------")
i = 1
while i<=9:
    j=1
    while j<=i:
        print("x*%d=z "%(i),end="")
        j+=1
    print("")
    i+=2
print("-----------------------------------------------------------")
i = 1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=z "%(j,i),end="")
        j+=1
    print("")
    i+=1
print("-----------------------------------------------------------")
i = 1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%d\t"%(j,i,j*i),end="")
        j+=1
    print("")
    i+=1
print("-----------------------------------------------------------")
