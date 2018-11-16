from timeit import Timer


def t1():
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    li = []
    for i in range(10000):
        li +=[i]


def t3():
    li = [i for i in range(10000)]


def t4():
    li = list(range(10000))


def t5():
    li = []
    for i in range(10000):
        li.extend([i])


timer1 = Timer("t1()","from __main__ import t1")
print("append:",timer1.timeit(1000))

timer2 = Timer("t2()","from __main__ import t2")
print("+:",timer2.timeit(1000))

timer3 = Timer("t3()","from __main__ import t3")
print("[i for i in range(10000)]:",timer3.timeit(1000))

timer4 = Timer("t4()","from __main__ import t4")
print("list(range(10000)):",timer4.timeit(1000))

timer5 = Timer("t5()","from __main__ import t5")
print("extend:",timer5.timeit(1000))

# append: 1.0749482511166866
# +: 1.045248102540945
# [i for i in range(10000)]: 0.4325180351371367
# list(range(10000)): 0.2468851987930787
# extend: 1.5134574727597987

def t6():
    li = []
    for i in range(10000):
        li.append(i)

def t7():
    li = []
    for i in range(10000):
        li.insert(0, i)


# timer6 = Timer("t6()","from __main__ import t6")
# print("append:",timer6.timeit(1000))
#
# timer7 = Timer("t7()","from __main__ import t7")
# print("insert(0):",timer7.timeit(1000))
# append: 1.051710199937791
# insert(0): 41.39381255457119
