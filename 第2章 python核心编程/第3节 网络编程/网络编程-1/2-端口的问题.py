from socket import *
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto("haha", ("192.168.4.62", 8080))


