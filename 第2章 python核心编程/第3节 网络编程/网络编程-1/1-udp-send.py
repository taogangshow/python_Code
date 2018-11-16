from socket import *
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto("haha", ("192.168.4.62", 8080))
udpSocket.sendto("haha1", ("192.168.4.62", 8080))

#使用ｕｄｐ发送的数据，在每一次的是都需要写上接收方的ip和port

