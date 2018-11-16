import os

os.fork()
os.fork()
os.fork()
'''
#这是fork炸弹，会让电脑瞬间死机
while True:
    os.fork()
'''
print("---1---")
