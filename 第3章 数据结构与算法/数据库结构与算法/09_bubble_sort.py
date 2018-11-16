# -*- coding:utf-8 -*-
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0,n-1):
        #控制班长从头走到尾走多少次
        for i in range(0,n-1-j):
            # 班长从头走到尾
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

    # i 0 ~ n-2   range(0, n-1) j=0
    # i 0 ~ n-3   range(0, n-1-1) j=1
    # i 0 ~ n-4   range(0, n-1-2) j=2
    # j=n  i  range(0, n-1-j)

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("排序前:",li)
    bubble_sort(li)
    print("排序后:",li)
