import os
love = input("伍彩霞女士你爱陶刚吗:")
if love == "爱":
    i = 1
    while i<=5:
        print("\n".join(["".join([("ILoveYou"[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else" ")for x in range(-30,30)])for y in range(15,-15,-1)]))
        print("亲爱的520么么哒")
        i+=1
    os.system('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" file:///C:/Users/Administrator/Desktop/Love/love.html') 
else:
    print("哼!,人家是可是你的男朋友")
input("")
