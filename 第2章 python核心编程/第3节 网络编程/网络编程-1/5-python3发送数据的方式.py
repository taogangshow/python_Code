from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
destIp = input("请输入目的IP:")
destPort = int(input("请输入目的端口:"))
sendData = input("请输入要发送的内容:")
#udpSocket.sendto(sendData.encode("utf-8"),(destIp,destPort))
udpSocket.sendto(sendData.encode("gb2312"),(destIp,destPort))
