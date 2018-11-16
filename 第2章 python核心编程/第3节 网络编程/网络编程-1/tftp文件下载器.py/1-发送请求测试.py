from socket import *
import struct

sendData = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)
#udpSocket = socket(AF_INET,SOCK_DGRAM)
#udpSocket.sendto(sendData,("192.168.4.62",69))
#udpSocket.close()
result = struct.unpack("!HH",sendData[:4])
print(result)
