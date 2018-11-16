from multiprocessing import Process
import time

class MyNewProcess(Process):
    #重写父类Process的run方法
    def run(self):
        while True:
            print("---1---")
            time.sleep(1)

p = MyNewProcess()
p.start()#调用父类的start方法,在strat方法里会去调用run方法
while True:
    print("---main---")
    time.sleep(1)
