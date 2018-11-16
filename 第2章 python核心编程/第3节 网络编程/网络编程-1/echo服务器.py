from socket import *

def main():
    num = 0
    while True:
        udpSocket = socket(AF_INET,SOCK_DGRAM)
        udpSocket.bind(("",7788))
        recvData = udpSocket.recvfrom(1024)
        udpSocket.sendto(recvData[0],recvData[1])
        num+=1
        print("已将接收到的第%d条数据返回给对方,内容为:%s"%(num,recvData[0].decode("gb2312")))

if __name__ == "__main__":
    main()
