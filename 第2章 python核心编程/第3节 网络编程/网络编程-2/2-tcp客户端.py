# -*- coding:utf-8 -*-
from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.4.62",8787))
sendData = input("请输入要发送的数据:")
#注意:
#1.tcp客户端已经链接号了服务器,所以在以后的数据发送中,不需要填写对方的ip和port---------->打电话
#2.udp在发送数据的时候,因为没有之前的链接,所以需要在每次的发送中都要填写接收方的ip和port------>写信
clientSocket.send(sendData.encode("gb2312"))
recvData = clientSocket.recv(1024)

print("接收服务器的消息为:%s"%recvData.decode("gb2312"))
clientSocket.close()
