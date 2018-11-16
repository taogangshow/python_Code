# -*- coding=utf-8 -*-
from socket import *
import struct,time

udpSocket = socket(AF_INET,SOCK_DGRAM)
resquestData = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)
udpSocket.sendto(resquestData,("192.168.4.62",69))
responseData = udpSocket.recvfrom(1024)
recvData,serverInfo = responseData
#print(recvData)
time.sleep(1)
print(serverInfo)
