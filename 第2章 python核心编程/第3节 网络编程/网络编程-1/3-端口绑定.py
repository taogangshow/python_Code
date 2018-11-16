from socket import *
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(("",7788))
udpSocket.sendto("haha", ("192.168.4.62", 2426))
rcvData = udpSocket.recvfrom(1024)
print(rcvData)
udpSocket.close()
