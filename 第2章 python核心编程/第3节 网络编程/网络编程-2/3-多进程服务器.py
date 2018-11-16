# -*- coding:utf-8 -*-
from socket import *
from multiprocessing import *

def dealWithClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData)>0:
            print("recv[%s]:%s"%(str(destAddr),recvData.decode("gb2312")))
        else:
            print("[%s]客户端已经关闭"%destAddr)
            break
    newSocket.close()


def main():
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("",7788))
    serverSocket.listen(5)
    try:
        while True:
            newSocket,destAddr = serverSocket.accept()
            client = Process(target=dealWithClient,args=(newSocket,destAddr))
            client.start()
            #因为已经向子进程中copy了一份（引用），并且父进程中这个套接字也没有用处了
            #所以关闭
            newSocket.close()
    finally:
    	 #当为所有的客户端服务完之后再进行关闭，表示不再接收新的客户端的链接
        serverSocket.close()

if __name__ == "__main__":
    main()
