# -*- coding:utf-8 -*-
from socket import *

#1.创建socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#2.绑定本地ip以及port
serverSocket.bind(("",7788))
#3.让这个socket变成非堵塞
serverSocket.setblocking(False)
#4.将socket变成监听(被动)套接字
serverSocket.listen(100)
#用来保存所欲偶已经链接上的客户端信息
clientList = []
while True:
    try:
        clientSocket,clientAddr = serverSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来:%s"%str(clientAddr))
        clientSocket.setblocking(False)
        clientList.append((clientSocket,clientAddr))
    for clientSocket,clientAddr in clientList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData)>0:
                print("[%s]:%s"%(str(clientAddr),recvData))
            else:
                clientSocket.close()
                clientList.remove((clientSocket,clientAddr))
                print("%s 已经下线..."%str(clientAddr))



