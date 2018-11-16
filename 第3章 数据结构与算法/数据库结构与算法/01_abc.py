# 如果 a+b+c=N且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# a
# b
# c
# c = 1000-a-b

import time

start_time = time.time()
num = 0
# for a in range(0, 1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 num += 1
#                 print("第%d种:a=%d b=%d c=%d" % (num, a, b, c))

# 顺序
# 条件
# 循环


# T = 1000 * 1000 * 1000 * 2
# T = 2000 * 2000 * 2000 * 2
# T = N* N* N*2
#
# T(n) = n^3 * 2
# T(n) = n^3 * 10
#
# T(n) = g(n)
#
# g(n) = n^3
for a in range(0, 1001):
    for b in range(0,1001):
        c = 1000 - a - b
        if a**2+b**2 == c**2:
            num += 1
            print("第%d种:a=%d b=%d c=%d" % (num, a, b, c))
#计算上面程序的时间复杂度(O表示法)
# T(n) = n * n * (1+ max( 1, 0))
#  = n^2 * 2
#  = O(n^2)
end_time = time.time()
time = end_time-start_time
print("一共有%d种组合，程序耗时:%d秒" % (num, time))