# -*- coding:utf-8 -*-
from socket import *
from threading import *

def dealWithClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData)>0:
            print("接收[%s]:%s"%(str(destAddr),recvData.decode("gb2312")))
        else:
            print("[%s]客户端已经关闭..."%destAddr)
            break
    newSocket.close()

def main():
    serverSocket = socket(AF_INET,SOCK_STREAM)

    serverSocket.bind(("",7799))

    serverSocket.listen(5)
    try:
        while True:
            newSocket,destAddr = serverSocket.accept()

            client = Thread(target=dealWithClient,args=(newSocket,destAddr))
            client.start()
            #因为线程中共享这个套接字，如果关闭了会导致这个套接字不可用，
            #但是此时在线程中这个套接字可能还在收数据，因此不能关闭
            #newSocket.close()
    finally:
        serverSocket.close()

if __name__ == "__main__":
    main()
