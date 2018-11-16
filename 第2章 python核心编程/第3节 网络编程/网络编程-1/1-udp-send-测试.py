from socket import *
from threading import Thread,Lock
import time
class Test1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                updSocket = socket(AF_INET,SOCK_DGRAM)
                updSocket.sendto("1:2334323:angelababy:liuss-pc:32:Dear: i love you",("192.168.4.62",2425))
                updSocket.sendto("hello socket",("192.168.4.62",8080))
                time.sleep(1)
                lock2.release()
class Test2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                updSocket = socket(AF_INET,SOCK_DGRAM)
                updSocket.sendto("1:2334323:Cassie:gulnz-pc:32:i miss you",("192.168.4.62",2425))
                updSocket.sendto("hello world",("192.168.4.62",8080))
                time.sleep(1)
                lock3.release()
class Test3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                updSocket = socket(AF_INET,SOCK_DGRAM)
                updSocket.sendto("1:2334323:Gillian:liuy-pc:32:memeda",("192.168.4.62",2425))
                updSocket.sendto("hello python",("192.168.4.62",8080))
                time.sleep(1)
                lock1.release()

if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()
    lock2.acquire()
    lock3 = Lock()
    lock3.acquire()

    t1 = Test1()
    t2 = Test2()
    t3 = Test3()

    t1.start()
    t2.start()
    t3.start()
